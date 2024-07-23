<h1 align="center">MoreChoice</h1>

# Python环境配置
- python版本: `3.10.*` (鉴于issue里面的某些问题, 建议自己去搜索一下或询问ai也是一种解决办法, 至于运行, 子文件夹中的`readme.md`应该会写)
- 库包: `requests`, `tqdm`, `rich`

## Change Log
### v0.1.5 (2024/7/23)
- 删除部分冗余文件, 重写部分代码
### v0.1.4 (2024/1/15)
- 修正了**FanQieNovel**中许多未解决的问题
### v0.1.3 (2023/3/17)
- **meth.py**兼容性增强, 采用更优雅的方式
### v0.1.2 (2023/3/13)
- **meth.py**兼容3.10以下不支持`match-case`语句版本
### v0.1.1 (2023/1/31)
- **Bilibili.reptile**新增**Cookie**及多线程下载
- **meth.py**增加支持大文件下载
### v0.1.0 (2023/1/30)
- 更正目录结构，增加可读性  
- 新增**Pixivel.reptile**, **Bilibili.reptile**
- 优化**FanQie.Novel.reptile**结构
- 重构代理爬取**Proxy.reptile**
- python版本需要3.10+来支持**match-case**语句

# 成品展示
## BiliBili视频下载器v2.1
这是通过**Bilibili.reptile**做出来的一个成品, 下面的`fix_m4s`算是针对电脑客户端下载的情况.  
> 下载地址: [releases/tag/v2.1 ](/releases/tag/v2.1)  
> 通过`pyside6`进行开发, 关于`m3u8`的直播录制暂时没有实现.   
> 最新通过`inno setup`进行二次封装.  
> 支持扫码登录, 优化了**多线程下载**的思路.
> 后面改进好了会**开源**供大家参考.  

![图片1](/image/1.png)
![图片2](/image/2.png)

## LICENSE
MIT
