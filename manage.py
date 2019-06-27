from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from fisher import app
from mapp.models.base import db
from mapp.models import user,gift,book

manager: Manager = Manager(app)

# 要使用flask-migrate，必须先绑定db和app

migrate = Migrate(app, db)

# 将MigrateCommand添加到manager中，"db"是自定义命令

manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()
