#!/usr/bin/python
#coding=utf-8
import  xml.dom.minidom

def file2dict(file_path):
    #打开xml文档
    dom = xml.dom.minidom.parse('demo.xml')

    #得到文档元素对象
    root = dom.documentElement

    #定义一个数据表描述字典
    database = {'tablename':'','fields':{},'index':{},'v':'','comment':''}

    #遍历文档的每个节点
    for node in root.childNodes:
        if node.nodeType == node.ELEMENT_NODE:

            #得到数据表名称
            if node.nodeName == 'tablename':
                database['tablename'] = node.nodeName

            #得到数据表字段
            if node.nodeName == 'fields':
                for n in node.childNodes:
                    if n.nodeName == 'item':
                        #得到字段名称
                        cc=n.getElementsByTagName('fieldsname')
                        c1=cc[0]
                        #得到字段类型
                        tt=n.getElementsByTagName('fieldstype')
                        t1=tt[0]
                        tmp = {'name':c1.firstChild.data,'type':t1.firstChild.data}
                        database['fields'][c1.firstChild.data] = tmp


    return database


database = file2dict('xxx')
for k,val in database.items():
    if k == 'fields':
        for k,v in val.items():
            print v['type'],'---',v['name']