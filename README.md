# fish_flask
学习flask框架
1. http.py -> mhttp.py: 模块名称冲突影响导入
2. url->endpoint(未指定的情况下为视图函数名称) ->viewfunc
3. 视图文件book分离后出现404错误 （python中模块只能导入一次）
4. 引入蓝图解决404问题
5. app关键字段 url_map,view_functions
6. request代理模式 request.args
7. wtforms 插件 验证层 errors 属性
8. json.dumps(yushu_book, default=lambda o: o.__dict__)
9. local localstack app_ctx request_ctx local_proxy