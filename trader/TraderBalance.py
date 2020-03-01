# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from mysql.online import MySQL


db = MySQL()
employee_id = "70b7ec63-99bc-4f24-b0bf-4efb5fc01e72"

cover_sql = "select c.nick_name,v.vendor_num from cover c join vendor v on c.vendor_id = v.id where c.id in (select cover_id from cover_employee_manager where employee_id = '%s')" % employee_id

cover_rows = db.get_data_by_sql(cover_sql)

for cover in cover_rows:
    print "点位编号：%s  昵称：%s" % (cover[1],cover[0])

trader_sql = "select jt.balance,e.employee_name from joining_trader jt join employee e on jt.employee_id = e.id where e.id = '%s'" % employee_id

trader = db.get_data_by_sql(trader_sql)

print "加盟商：%s   余额：%s" % (trader[0][1],trader[0][0])






