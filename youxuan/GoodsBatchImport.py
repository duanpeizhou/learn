# -*- coding: UTF-8 -*-

import xlrd
import sys
import uuid
import hashlib
reload(sys)

file = "~/Desktop/美加优选商品信息库.xlsx"

def read_excel():
    workbook = xlrd.open_workbook(filename=file)

    fruits_sheet = workbook.sheet_by_index(2)
    goods_num = 1122
    shop_id = 'c3f31315-c658-49fb-abca-4bea8ba49196'
    for row in range(1,fruits_sheet.nrows):
        goods_name = fruits_sheet.cell_value(row, 3)
        goods_id = uuid.uuid4()
        goods_detail = fruits_sheet.cell_value(row,11)
        goods_num += 1
        goods_product_area = fruits_sheet.cell_value(row,10)
        goods_unit = fruits_sheet.cell_value(row,5)
        sql = """INSERT INTO `goods` (`id`, `goods_num`, `goods_name`,  `customer_id`, `status`, `detail`, `storage_amount`, `delivery_days`, `add_time`, `add_user`, `mod_time`, `mod_user`, `is_sale_limit`, `sold_amount`, `goods_type`, `deduct_percent`, `goods_limit_type`, `limit_amount`, `limit_desc`, `goods_category`, `goods_second_category`, `goods_brand`, `goods_source`, `goods_variety`, `goods_unit`, `goods_tag`, `barcode`, `reserve_storage_amount`, `is_put_on_mini`)
VALUES
	('%s', %d, '%s', '%s', 1, '%s', 10000, NULL, '2019-09-24 21:15:26', 'edfa6aa4-8dd3-11e9-a6c2-7cd30ac20c2c', '2019-09-24 21:15:26', 'edfa6aa4-8dd3-11e9-a6c2-7cd30ac20c2c', 0, 0, 2, 0.0300, 1, NULL, NULL, 1, '', '', '%s', '', '%s', 1, NULL, 10000, 1);
""" % (goods_id, goods_num, goods_name, shop_id,goods_detail, goods_product_area, goods_unit)
        print sql

        sale_channel_sql = """INSERT INTO `goods_sales_channel` (`goods_id`, `sales_channel`) 
        VALUES ('%s', 1);""" % (goods_id)
        print sale_channel_sql

        specs = fruits_sheet.cell_value(row, 4);
        market_price = fruits_sheet.cell_value(row, 6);
        price = fruits_sheet.cell_value(row, 8);

        goods_spec_sql = """INSERT INTO `goods_spec` (`id`, `goods_id`, `spec_name`, `spec_status`, `mod_user`, `mod_time`, `market_price`, `sale_price`, `buy_price`, `amount`, `reserved_amount`, `is_default`, `barcode`)
VALUES
	('%s', '%s', '%s', 1, 'edfa6aa4-8dd3-11e9-a6c2-7cd30ac20c2c', '2019-08-31 19:07:28', %s, %s, %s, 10000, 10000, 1, '');
""" % (uuid.uuid4(),goods_id,specs,market_price,price,price)

        print goods_spec_sql
        data = "%s%s" % (shop_id,goods_id);
        shop_goods_id = hashlib.md5(data).hexdigest()

        shop_goods_sql = """INSERT INTO `shop_goods` (`id`, `shop_id`, `goods_id`, `sale_status`, `sale_tag`, `add_user`, `add_time`, `mod_user`, `mod_time`, `top_index`)
VALUES
	('%s', '%s', '%s', 1, 'edfa6aa4-8dd3-11e9-a6c2-7cd30ac20c2c', NULL, '2019-09-10 19:02:39', 'edfa6aa4-8dd3-11e9-a6c2-7cd30ac20c2c', '2019-09-10 19:02:39', NULL);
""" % (shop_goods_id,shop_id,goods_id)

        print shop_goods_sql


read_excel()
