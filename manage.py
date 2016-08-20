import os
from application import create_app
from application import db
from flask_script import Manager
from flask_script import Shell
from flask_migrate import Migrate
from flask_migrate import MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return {}
    # return dict(app=app, db=db,  User=User, Role=Role)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
