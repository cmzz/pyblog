__author__ = 'Andy'

"""
管理脚本，可以启动控制台，启动开发服务器，执行数据库操作等
同时可以你可在这里添加自定义的命令
"""

from app import create_app, db
from app.models import User
from flask_script import Manager, Shell, Server
from flask_migrate import Migrate, MigrateCommand

# 传入开发模式参数
app = create_app("development")
manager = Manager(app)
migrate = Migrate(app, db)


# 创建一个上下文
def make_shell_context():
    return dict(app=app, db=db, User=User)


# 启动控制台命令
manager.add_command("shell", Shell(make_shell_context))
# 数据库的操作命令，如升级还原等
manager.add_command("db", MigrateCommand)

# 启动web服务器， 仅用于开发环境
manager.add_command('runserver', Server())

if __name__ == "__main__":
    manager.run()
