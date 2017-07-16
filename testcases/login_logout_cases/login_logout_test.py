#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: samren
import unittest, os
from selenium import webdriver

from config import *
from testcases.common_logic.bussiness_common_steps import *
from lib.utils import read_excel

class LoginLogoutTest(unittest.TestCase):
    """登录后查询或条件"""
    def setUp(self):
        self.executable_path = chrome_driver
        self.driver = webdriver.Chrome(executable_path=self.executable_path)
        self.url = "http://localhost/bugfree"
        open_url(self.driver, self.url)
        self.data_dict = read_excel(os.getcwd()+"/data/login_account.xlsx")

    def test_bugfree_login_success(self):
        """登录Bugfree成功"""
        driver=self.driver
        username, password, flag = self.data_dict[1]
        print username, password, flag
        login_bugfree(driver, username, password)
        self.assertEqual(flag, driver.title)

    def test_bugfree_login_fail_invalid_username(self):
        """登录Bugfree失败，使用无效的用户名"""
        driver = self.driver
        username, password, flag = self.data_dict[2]
        print username, password, flag
        login_bugfree(driver, username, password)
        self.assertIn(flag, driver.page_source)


    def test_bugfree_login_fail_invalid_password(self):
        """登录Bugfree失败，使用无效的密码"""
        driver = self.driver
        username, password, flag = self.data_dict[3]
        print username, password, flag
        login_bugfree(driver, username, password)
        self.assertIn(flag, driver.page_source)

    def tearDown(self):
        self.driver.quit()