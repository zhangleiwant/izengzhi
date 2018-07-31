import pymysql
# django1.10 默认连接mysql的模块是 mysql-python 而python3 不支持该模块 使用 pymysql模块代替 在初始化模块的时候进行修改默认支持
pymysql.install_as_MySQLdb()