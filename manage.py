import gevent.monkey
gevent.monkey.patch_all()

from app import create_app
from flask_script import Manager
from flask_script.commands import Shell
from flask_script import Server

app = create_app()
app.debug = True
manager = Manager(app)


def make_shell_context():
    return dict(app=app)
manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
