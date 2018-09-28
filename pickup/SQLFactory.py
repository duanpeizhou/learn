# -*- coding: UTF-8 -*-

def main():
    for index in range(1, 32):
        sql = "INSERT INTO `coupon_template_limit` (`coupon_template_id`, `object_id`, `add_time`, `limit_type`) VALUES (%d, '8', now(), 1);" % index
        sql2 = "INSERT INTO `coupon_template_limit` (`coupon_template_id`, `object_id`, `add_time`, `limit_type`) VALUES (%d, '9', now(), 1);" % index
        print sql
        print sql2
main()