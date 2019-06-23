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
10. app = Flask(__name__, static_folder='statics')
11. render_template Flask(template_folder)
12. super() 调用父类模板内容
13. {{x.school | default(x.school) | default('为空')}}
14. url_for endpoint {{url_for('static', filename='test.css')}}
15. SECRET_KEY get_flashed_messages with set jinja2 文档
16. sqlalchemy: base未指定主键 __abstract__=True
17. methods=['GET', 'POST']
18. model.Base:set_attrs(self, attrs_dict)
20. db.session.add(user) db.session.commit
21. 安装flask-login 注册login_manager user继承login_user
22. 适当重复，孰能生效，温故知新
23. http://127.0.0.1:5000/login?next=%2Fmy%2Fgifts http://127.0.0.1:5000/login?next=http://www.qq.com
24. @login_required:指明访问控制的接口
25. @login_manager.user_loader：根据session信息（通常为use_id）返回用户信息