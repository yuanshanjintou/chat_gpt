class Config:
    HOST = '0.0.0.0'
    PORT = '8080'
    DEBUG = False
    NAME = "mission"
    SECRET_KEY = "ansoiohfao"
    MYSQL_HOST = '192.168.0.205'
    MYSQL_PORT = 3306
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '123456'
    from urllib import parse
    pwd = parse.quote(MYSQL_PASSWORD)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/chat_gpt'.format(MYSQL_USER, pwd, MYSQL_HOST, MYSQL_PORT)
    # 数据库类型+数据库操作引擎://用户名:密码@主机名:端口/数据库名

    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 追踪数据的修改信号
    SQLALCHEMY_ECHO = False  # 是否在控制台打印输出sql语句
    JSON_AS_ASCII = False  # 不转移中文字符

    LOGGING_LEVEL = 'INFO'
    LOGGING_HANDLER_CONSOLE_LEVEL = 'INFO'

    # redis相关配置
    REDIS_HOST = '127.0.0.1'
    REDIS_PASSWORD = ''
    REDIS_PORT = 6379
    REDIS_DB = 2

    # mongodb配置
    MONGODB_DB = 'keliu'  # 数据库名称
    MONGODB_HOST = '192.168.0.222'  # 服务器地址
    MONGODB_PORT = 27017  # 服务器端口号
    MONGODB_USERNAME = 'root'  # 用户名
    MONGODB_PASSWORD = '1234qwer'  # 用户密码
