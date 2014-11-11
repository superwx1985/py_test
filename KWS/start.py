# -*- coding: utf-8 -*-
import unittest, time, re, random, HTMLTestRunner, multiprocessing, threading, sys, os
from KWS.test_case import test_smoke_test
from KWS import send_report

#===============================================================================
# #各种快速获取TC的方法
# def make_TC_suite():
#     suite = unittest.TestSuite()
#     suite.addTest(unittest.makeSuite(test_smoke_test.Mytest))
#     return suite
# 
# def discover_TC():
#     TC_folder = 'D:/viwang/workspace/PyTest01/KWS/test_case/'
#     suite = unittest.defaultTestLoader.discover(TC_folder, pattern='*smoke_test.py', top_level_dir='d:/viwang/workspace/PyTest01/KWS/')
#     return suite
# def get_tc_from_name(package='test_case.test_smoke_test',names=['test_smoke_test_CC','test_smoke_test_Paypal','test_smoke_test_Amazon']):
#     def get_module_from_packagename(name):
#         __import__(name)
#         return sys.modules[name]
#     module_smoket_test = get_module_from_packagename(package)
#     for name in names:
#         suite_smoket_test = unittest.loader.findTestCases(module_smoket_test, prefix=name)
#         suite.addTests(suite_smoket_test)
#===============================================================================

def RunCase(suite,multi=0):
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    reportname = 'D:\\vic_test_data\\KWS_test\\result_' + now + '.html'     # 定义个报告存放路径，支持相对路径
    fp = open(reportname, 'wb')
    if multi == 0:
        #定义测试报告
        runner = HTMLTestRunner.HTMLTestRunner(
                                               stream=fp,
                                               title='KWS automation test',
                                               title2=str(suite),
                                               description='Detail list'
                                               )
        runner.run(suite)
    else:
        proclist = []
        s = 1
        for i in suite:
            runner = HTMLTestRunner.HTMLTestRunner(
                                                   stream=fp,
                                                   title='KWS automation test',
                                                   title2=str(i),
                                                   description='Detail list'
                                                   )
            #proc = multiprocessing.Process(target=runner.run, args=(i,))    #多进程运行，windows下会冲突
            proc = threading.Thread(target=runner.run, args=(i,))   #多线程运行
            proclist.append(proc)
            s += 1
        for proc in proclist: proc.start()
        for proc in proclist: proc.join()
    fp.close()

#####################################################################################################################

print(time.strftime('%Y-%m-%d %H:%M:%S'), 'BEGIN')
suite = unittest.TestSuite()

def suite1():
    suite = unittest.TestSuite()
    suite.addTest(test_smoke_test.Mytest('test_smoke_test_CC_logout',1,2))
    suite.addTest(test_smoke_test.Mytest('test_smoke_test_CC_login',1,2))
    return suite

def suite2():
    suite = unittest.TestSuite()
    suite.addTest(test_smoke_test.Mytest('test_smoke_test_Paypal_logout',1,2))
    suite.addTest(test_smoke_test.Mytest('test_smoke_test_Paypal_login',1,2))
    return suite

def suite3():
    suite = unittest.TestSuite()
    #suite.addTest(test_smoke_test.Mytest('sample1',1,3))
    suite.addTest(test_smoke_test.Mytest('test_smoke_test_Amazon_logout',1,3))
    suite.addTest(test_smoke_test.Mytest('test_smoke_test_Amazon_login',1,3))
    return suite

suite.addTest(test_smoke_test.Mytest('sample1',1,3))
#suite.addTest(test_smoke_test.Mytest('sample2',1,1))

#suite.addTest(suite1())     #这样可以把几个 testcase 组合成一组
#suite.addTest(suite2())
#suite.addTest(suite3())

print('test suite: ',suite)
RunCase(suite,0)    #第二位参数代表是否用多线程运行

#send_report.send_report('D:/vic_test_data/KWS_test/')
print(time.strftime('%Y-%m-%d %H:%M:%S'), 'END')




#===============================================================================
# now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
# reportname = 'D:\\vic_test_data\\KWS_test\\result_' + now + '.html'  # 定义个报告存放路径，支持相对路径
# fp = open(reportname, 'wb')
#  
# # 定义测试报告
# runner = HTMLTestRunner.HTMLTestRunner(
#                                        stream=fp,
#                                        title='KWS automation test',
#                                        description='Detail list'
#                                        )
#  
# # 运行测试用例
# runner.run(suite)
# fp.close()  # 关闭报告文件
# send_report.send_report('D:/vic_test_data/KWS_test/')
#  
# print(time.strftime('%Y-%m-%d %H:%M:%S'), 'END')
#===============================================================================
