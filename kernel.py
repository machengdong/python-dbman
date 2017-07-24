#!/usr/bin/python
# -*- coding: UTF-8 -*-
import utils.mysql as mysql
import utils.utils as utils


class kernel:

    conf = {}
    def __init__(self):
        self.conf = utils.getConfigList('misc')
        self.m = mysql.mysql()

    def __del__(self):
        print '------------- END -------------'


    def update(self):
        database_path = self.conf['data']
        dbFiles = utils.getFileList(database_path)
        for table_name in dbFiles:
            full_file_path = database_path + dbFiles[table_name]
            full_file_content = utils.file2dict(full_file_path)
            # 判断表是否存在
            if self.m.table_exists(table_name):
                # 更新表
                full_db_content = self.m.getTablesInfo(table_name)
                self.update_table_info(full_file_content,full_db_content)
                print '--------- 更新表 ---------'+table_name
            else:
                print '--------- 添加表 ---------'+table_name

    def update_table_info(self,file_content,db_content):
        is_update = False
        for fiedls in file_content['fields']:
            # 如果字段存在，就判断字段其他属性是否相同
            if db_content['fields'].has_key(fiedls) and self.__fields_diff(file_content['fields'][fiedls],db_content['fields'][fiedls]):
                print 1



    def __fields_diff(self,file_fields,db_fields):
        db_fields['type']


