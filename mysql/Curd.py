'''
Author: Goog Tech
Date: 2020-08-07 08:55:01
LastEditTime: 2020-08-07 09:50:00
Description: CURD of Python3 With MySQL8
FilePath: \py-beginner\mysql\Curd.py
'''

# 导入 pymysql 模块
import pymysql


class Curd:

    # 定义全局变量
    cursor = None
    connection = None
    
    ''' 初始化 '''
    def __init__(self, host, user, password, database):
        global connection
        connection = pymysql.connect(host, user, password, database)

    ''' 释放资源 '''
    def close(self):
        global cursor
        global connection
        cursor.close()
        connection.close()

    ''' 连接数据库 '''
    def getConnection(self):
        global cursor
        global connection
        cursor = connection.cursor()  # 创建游标对象
        return cursor

    ''' 创建表结构 '''
    def create(self, sql):
        # 执行 SQL 语句并释放资源
        try:
            cursor = self.getConnection()
            cursor.execute(sql)
            print('created the table successfully')
        except Exception as e:
            print(e)
        finally:
            self.close()

    ''' 插入数据 '''
    def insert(self, sql, user):
        global connection
        try:
            cursor = self.getConnection()
            cursor.execute(sql, user)
            connection.commit()
            print('inserted the user info to database successfully')
        except Exception as e:
            print(e)
            connection.rollback()
        finally:
            self.close()

    ''' 查找数据 '''
    def select(self, sql):
        try:
            cursor = self.getConnection()
            cursor.execute(sql)
            users = cursor.fetchall()
            print('selected the user infos be shown as below :')
            for user in users:
                print(user)
        except Exception as e:
            print(e)
        finally:
            self.close()

    ''' 删除数据 '''
    def delete(self, sql):
        global connection
        try:
            cursor = self.getConnection()
            cursor.execute(sql)
            connection.commit()
            print('deleted the user info successfully')
        except Exception as e:
            print(e)
            connection.rollback()
        finally:
            self.close()

    ''' 更新数据 '''
    def update(self, sql, user):
        global connection
        try:
            cursor = self.getConnection()
            cursor.execute(sql, user)
            connection.commit()
            print('updated the user info succesfully')
        except Exception as e:
            print(e)
            connection.rollback()
        finally:
            self.close()


# 测试
curd = Curd('localhost-or-ip', 'user-name', 'user-password', 'database-name')
curd.create(
    "create table t_user(uid integer primary key auto_increment, name varchar(45) not null, age integer)"
)
curd.insert("insert into t_user(name, age) values(%s, %s)", ('mysql8', 23))
curd.select('select uid, name, age from t_user')
curd.delete('delete from t_user where uid = 2')
curd.update('update t_user set name = %s where uid = %s', ('newname', 1))
