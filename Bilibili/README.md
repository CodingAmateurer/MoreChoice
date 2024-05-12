# Concise Introduction
`Getself` is used by Cookie of Bilibili to verity state of account, and the `Getself('FILE:Cookie.txt')` can pass the file to do. Of course, you can direct to use text of Cookie such as `Getself('text of Cookie')`.Then, we can use `Getself('FILE:Cookie.txt').sign_in()` to verity Cookie whether is valid.
`BilibiliRun` can help you to download the vedio fastly. The `BilibiliRun().run(session, vedio_list)` including two parameters that are `Session` and `List[tuple]`, which can pass the `Getself('text of Cookie').session` and `BilibiliRun().load_vedio_list(file_name)` to get it. The example of file of `BilibiliRun().load_vedio_list(file_name)` as follow: 
```[txt]
BV1Qt421u7eb 120
BV1KZ421j7N4 120
```

And the example of using code as follow:
```[python]
session: Session = GetSelf('FILE:Cookie.txt').session
poll = BilibiliRun()
vedio_list = poll.load_vedio_list('vedio_list.txt')
# vedio_list = [('BV1Qt421u7eb', 120), ('BV1KZ421j7N4', 120)]
poll.run(session, vedio_list)
```
