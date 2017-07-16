#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
#from testcases.login_logout_cases.bugfree_login_or_condition import BugFreeLoginOrCondition
from testcases.bugfree_import_file import BugfreeImportFile
from testcases.product_management.product_add import ProductAdd

def suites():
    suite=unittest.TestSuite()
    loader=unittest.TestLoader()
    #suite.addTests(loader.loadTestsFromTestCase(BugFreeLoginOrCondition))
    #suite.addTests(loader.loadTestsFromTestCase(BugfreeImportFile))
    suite.addTests(loader.loadTestsFromTestCase(ProductAdd))
    return suite


if __name__ == "__main__":
    suite = suites()
    fp = open('./reports/results_%s.html' % time.strftime("%Y-%m-%d %H-%M-%S"), 'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title=u'Bugfree功能测试报告',
        description=u"测试用例执行情况：")
    runner.run(suite)