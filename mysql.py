#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

import utils

class mysql:

    conf = {}

    def __init__(self):
        mysql.conf = utils.getConfigList()
        self.connect()

    def __del__(self):
        if mysql.db :
            mysql.db.close()

    def connect(self):
        # 打开数据库连接
        mysql.db = MySQLdb.connect(mysql.conf['host'],mysql.conf['user'],mysql.conf['pass'],mysql.conf['database'])

    def get_version(self):
        # 使用cursor()方法获取操作游标
        cursor = mysql.db.cursor()
        # 使用execute方法执行SQL语句
        cursor.execute("SELECT VERSION()")
        # 使用 fetchone() 方法获取一条数据库。
        data = cursor.fetchone()
        # 返回数据
        return data

    def getList(self,sql):
        # 使用cursor()方法获取操作游标
        cursor = mysql.db.cursor()
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 表头
            title = cursor.description
            # 获取所有记录列表
            results = cursor.fetchall()
            # 定义返回值
            list = []
            for row in results:
                # 定义一行
                ir = {}
                # 取出所有表头
                for i in range(len(title) - 1):
                    ir[title[i][0]] = row[i]
                # 追加到list里面
                list.append(ir)
            # 返回结果
            return list
        except:
            print "Error: unable to fecth data"


    def getRow(self,sql):
        # 调用本类getList方法
        data = self.getList(sql)
        if data:
            return data[0]
        return {}
