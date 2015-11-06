__author__ = 'Andy'

from app import create_app, db
from app.models import User
from flask_script import Manager, Shell, Server
from flask_migrate import Migrate, MigrateCommand

app = create_app("development")
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db, User=User)

manager.add_command("shell", Shell(make_shell_context))
manager.add_command("db", MigrateCommand)

manager.add_command('runserver', Server())

if __name__ == "__main__":
    manager.run()