import asyncio
import logging

from dataclasses import dataclass
from requests import Session, utils
from tqdm.rich import tqdm

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

@dataclass
class Config:
    def __init__(self, url: str, method: str, headers: dict = {}):
        self.url = url
        self.method = method

        self.headers: dict = {
				'origin': 'https://www.bilibili.com/',
				'referer': 'https://www.bilibili.com/',
				'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
				'accept': 'application/json, text/plain, */*'
			} if headers == {} else headers
        self.req_params: dict = {
        'method': self.method,
        'url': self.url
        }

class GetSelf:
    '''
    处理cookie获取用户信息
    '''
    def __init__(self, cookie: str):
        if cookie[:5] == 'FILE:':
            with open(cookie[5:], 'r+') as f: self.cookie = f.read()
        else:
            self.cookie = cookie
        self.cookie = dict([l.split("=", 1) for l in self.cookie.split("; ")])
        self.session = Session()
        self.config = Config('https://api.bilibili.com/x/space/myinfo', 'GET')

        self.session.headers.update(self.config.headers)
        self.state_code_dict: dict = {
            -101: False,
            0: True
        }

        self.session.cookies = utils.cookiejar_from_dict(self.cookie)

    def __call__(self) -> bool:
        if self.session.cookies is None:
            logging.error('Cookie未配置')
            return False

        state: dict = self.session.request(**self.config.req_params).json()

        if self.state_code_dict[state['code']]:
            logging.info(f'UserName: {state["data"]["name"]}, Mid: {state["data"]["mid"]}')
            return True
        
        logging.error('Cookie无效')
        return False

class DownloadStrategy:
    def __init__(self, session: Session):
        self.session = session
        self.config = Config('https://api.bilibili.com/x/web-interface/view', 'GET')
        self.config_vedio = Config('https://api.bilibili.com/x/player/playurl', 'GET')

    async def download_vedio(self, bvid: str, quality: int):
        fnval, fourk = 1, 0
        block_size = 4096
        if quality == 120:
            fnval, fourk = 128, 1
        
        cid: str = self.session.request(**self.config.req_params, params={'bvid': bvid}).json()['data']['cid']
        url_list = self.session.request(**self.config_vedio.req_params, params={
            'bvid': bvid,
            'cid': cid,
            'qn': quality,
            'fnval': fnval,
            'fourk': fourk
        }).json()
        logging.info(f"Quality:{quality}, Url:{url_list['data']['durl'][0]['url']}, Size:{url_list['data']['durl'][0]['size']/(2**20)}M")

        process_bar = tqdm(total=url_list['data']['durl'][0]['size'], unit='iB', unit_scale=True,desc=f"Downloading {bvid}.mp4", ascii=True)

        data = self.session.request('GET', url_list['data']['durl'][0]['url'], stream=True)
        with open(f'{bvid}.mp4', 'wb') as f:
            for chunk in data.iter_content(block_size):
                process_bar.update(len(chunk))
                f.write(chunk)
        
        process_bar.close()

class BilibiliRun:
    async def run_task(self, session: Session, vedio_list: list):
        tasks:list = [asyncio.create_task(DownloadStrategy(session).download_vedio(bvid, quality)) for bvid, quality in vedio_list]
        await asyncio.gather(*tasks)
    
    def load_vedio_list(self, file_name: str) -> list[tuple]:
        with open(file_name, 'r+') as f:
            return [tuple(line.split()) for line in f.readlines()]
        
    def __call__(self, session: Session, vedio_list: list[tuple]):
        asyncio.run(self.run_task(session, vedio_list))

# 简单测试部分
if __name__ == '__main__':
    session: Session = GetSelf('FILE:Cookie.txt').session
    GetSelf('FILE:Cookie.txt')()
    # poll = BilibiliRun()
    # # vedio_list = poll.load_vedio_list('vedio_list.txt')
    # vedio_list = [('BV1Qt421u7eb', 120), ('BV1KZ421j7N4', 120)]
    # poll(session, vedio_list)
