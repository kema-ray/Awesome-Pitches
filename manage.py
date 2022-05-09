from app import create_app,db
from app.models import Pitch
from flask_script import Manager,Server
from  flask_migrate import Migrate

# creating app instance
app = create_app('development')

migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('server',Server)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,Pitch = Pitch )

if __name__=='__main__':
    manager.run()
