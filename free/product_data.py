# -*- coding: UTF-8 -*-

import datetime

from mysql.online import MySQL as MySQLUtil


class ProductData:
    def __init__(self):
        self.vendor_nums = "'1000008', '1000007', '1000006', '1000004', '1000005', '1000009', '1000010', '1000014', '1000015', " \
                      "'1000016', '1000017', '1000019', '1000011', '1000127', '1000348', '1000126', '1000339', '1000125', " \
                      "'1000108', '1000023', '1000068', '1000135', '1000102', '1000061', '1000342', '1000083', '1000121', " \
                      "'1000034', '1000063', '1000033', '1000052', '1000060', '1000070', '1000069', '1000122', '1000018', " \
                      "'1000020', '1000012', '1000106', '1000117', '1000123', '1000124', '1000128', '1000055', '1000041', " \
                      "'1000029', '1000030', '1000079', '1000130', '1000338', '1000075', '1000092'"
        self.database = MySQLUtil()
        self.date = datetime.datetime.now().strftime('%Y-%m-%d')

    def get_group_dict(self):
        database = self.database
        sql = "select id,group_name from goods_group where id in (select distinct group_id from cover_menu " \
              "where cover_menu_status = 1 and  vendor_id in (select id from vendor where vendor_num in " \
              "(%s))) order by goods_group_num desc;" % self.vendor_nums
        result = database.get_data_by_sql(sql)
        groups = {}
        for row in result:
            groups[row[0]] = row[1]
        return groups

    def get_excel_title(self):
        self.title = {"cover_name": {"columnNum": 0, "titleName": "点位昵称"},
                 "replenishment": {"columnNum": 1, "titleName": "补货量"},
                 "storage": {"columnNum": 2, "titleName": "剩余量"}}
        groups = self.get_group_dict()
        column_num = 3
        for key, value in groups.items():
            self.title[key] = {"columnNum": column_num, "titleName": value}
            column_num += 1
        print self.title

    def get_replenishment_amount(self, vendor_id):
        sql = "select count(distinct storage_id) from replenishment_record where vendor_id = %s and record_type = 1 and date(record_time) = date(%s);" % (vendor_id, self.date)
        result = self.database.get_data_by_sql(sql)
        return result[0]

    def get_replenishment_group_amount(self, vendor_id):
        sql = "select new_value,count(distinct storage_id) from replenishment_record where vendor_id = %s and record_type = 1 and date(record_time) = date(%s) group by new_value" % (vendor_id, self.date)
        results = self.database.get_data_by_sql(sql)
        group = {}
        for result in results:
            group[result[0]] = result[1]
        return group

    def get_storage_amount(self, vendor_id):
        sql = "select count(id) from storage where vendor_id = %s and storage_status = 1;" % vendor_id
        result = self.database.get_data_by_sql(sql)
        return result[0]

    def get_storage_group_amount(self, vendor_id):
        sql = "select group_id,count(id) from storage where vendor_id = %s and storage_status = 1 group by group_id;" % vendor_id
        results = self.database.get_data_by_sql(sql)
        storage = {}
        for result in results:
            storage[result[0]] = result[1]
        return storage









pd = ProductData()
pd.get_excel_title()
