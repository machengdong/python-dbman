#!/usr/bin/python
# -*- coding: UTF-8 -*-
import utils
import mysql

#print utils.getConfigList()

m = mysql.mysql()
sql = "SELECT * FROM phinxlog"

print m.getRow(sql)
print '\r\n--------------\r\n'
print m.getList(sql)


print m.drop_table('t201704241')