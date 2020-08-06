'''
Author: Goog Tech
Date: 2020-08-05 21:09:36
LastEditTime: 2020-08-06 22:38:46
Description: CURD of Python With SQlite
FilePath: \py-beginner\SQLite\Curd.py
'''

# 导入 sqlite3 模块
import sqlite3


class Curd:

    # 定义全局变量
    cursor = None
    connection = None
    ''' 初始化 '''
    def __init__(self, sqlpath):
        global connection
        connection = sqlite3.connect(sqlpath)  # 创建数据库链接对象

    ''' 释放资源 '''
    def close(self):
        global cursor
        global connection
        cursor.close
        connection.close

    ''' 连接数据库 '''
    def getConnection(self):
        global cursor
        cursor = connection.cursor()  # 创建游标对象
        return cursor

    ''' 创建表结构 '''
    def create(self, sql):
        # 执行 SQL 语句并释放资源
        try:
            cursor = self.getConnection()
            cursor.execute(sql)
            print("created the table successfully")
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
            print('updated the user info successfully')
        except Exception as e:
            print(e)
            connection.rollback()
        finally:
            self.close()


# 测试
curd = Curd('the file path of sqlite.db')

curd.create(
    "create table t_user(uid integer primary key autoincrement, name varchar not null, age integer)"
)
curd.insert("insert into t_user(name, age) values(?, ?)", ('sqlite3', 23))
curd.select('select uid, name, age from t_user')
curd.delete('delete from t_user where uid = 1')
curd.update('update t_user set name = ? where uid = ?', ('newname', 1))
