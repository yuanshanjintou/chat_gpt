from flask_script import Manager, Server  # 导入命令类和管理类
from flask_migrate import MigrateCommand, Migrate  # 导入迁移类和迁移命令类
from app import app, db
# from utils.mysql_conn import db

# 1. 实例化一个管理对象 传入app,不能是蓝图
manage = Manager(app)

# 2. 把数据库对象告诉迁移命令
migrate = Migrate(app, db)  # 把app和数据库连接对象都初始化到迁移对象上

# 3. 把迁移的命令添加到管理对象上面
manage.add_command("db", MigrateCommand)  # db是一个命令分组

manage.add_command('runserver', Server(threaded=True))


# 4. 把命令启动起来
if __name__ == '__main__':
    manage.run()

