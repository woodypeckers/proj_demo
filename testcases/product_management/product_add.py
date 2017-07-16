#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: samren
import unittest
from selenium import webdriver
from config import *
from testcases.common_logic.bussiness_common_steps import *


class ProductAdd(unittest.TestCase):
    """Bugfree产品添加测试"""
    def setUp(self):
        self.driver = webdriver.Chrome(chrome_driver)
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost"
        driver = self.driver
        open_url(driver, self.base_url + "/bugfree/index.php/site/login")
        login_bugfree(driver, "admin", "123456")

    def test_product001(self):
        """新增产品"""
        driver = self.driver
        driver.get(self.base_url + "/bugfree/index.php/bug/list/1")
        driver.find_element_by_link_text(u"后台管理").click()
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element_by_link_text(u"添加产品").click()
        driver.find_element_by_id("Product_name").clear()
        self.product_id = "Product_%s" % generate_random_num(1,99)
        driver.find_element_by_id("Product_name").send_keys(self.product_id)
        driver.find_element_by_id("Product_display_order").clear()
        driver.find_element_by_id("Product_display_order").send_keys("2")
        driver.find_element_by_id("Product_bug_severity").clear()
        driver.find_element_by_id("Product_bug_severity").send_keys("1,2,3,4,5")
        driver.find_element_by_id("Product_bug_priority").clear()
        driver.find_element_by_id("Product_bug_priority").send_keys("1,2,3,4,5")
        driver.find_element_by_id("Product_case_priority").clear()
        driver.find_element_by_id("Product_case_priority").send_keys("1,2,3,4,5")
        driver.find_element_by_name("yt0").click()
        time.sleep(3)

    def tearDown(self):
        # 删除掉刚刚生成的产品id,   self.product_id
        # 连接到数据库之后，执行delete 语句
        pass