'''
Created on 2014年9月10日

@author: viwang
'''
# -*- coding: utf-8 -*-
import time, random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


environment = ''
browser = ''
baseURL = ''
ff_profile = 'C:\\Users\\viwang\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\yj7r4nzk.tester'
chromeoption1 = webdriver.ChromeOptions()
chromeoption1._arguments = ['test-type', "start-maximized", "no-default-browser-check"]

class Driver(object):
    def __init__(self, environment, browser):
        self.environment = environment
        self.browser = browser
        if self.environment == 1: 
            self.baseURL = 'http://qa.weddingshop.theknot.com/'
        elif self.environment == 2:
            self.baseURL = 'http://stg.weddingshop.theknot.com/'
        elif self.environment == 3:
            self.baseURL = 'http://weddingshop.theknot.com/'
        else:
            print('no such environment, please check your setting')
            exit()
        if self.browser == 1:
            self.br = webdriver.Ie()
            self.br.maximize_window()
        elif self.browser == 2:
            self.br = webdriver.Firefox(firefox_profile=webdriver.FirefoxProfile(ff_profile))
            self.br.maximize_window()
        elif self.browser == 3:
            self.br = webdriver.Chrome(chrome_options=chromeoption1)
        elif self.browser == 4:
            self.br = webdriver.Remote(command_executor='http://172.25.20.19:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
            self.br.maximize_window()
        elif self.browser == 5:
            self.br = webdriver.Remote(command_executor='http://172.26.11.121:4444/wd/hub', desired_capabilities=DesiredCapabilities.SAFARI)
        elif self.browser == 6:
            self.br = webdriver.Remote(command_executor='http://172.25.20.19:4444/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX)
            self.br.maximize_window()
        else:
            print('no such driver, please check your setting')
            exit()  
        self.br.implicitly_wait(30)




def KWS_login_vic(driver):
    driver.br.find_element_by_id('lnkLogin').click()
    driver.br.find_element_by_id('txtUsername').send_keys('vicwangtest@gmail.com')
    driver.br.find_element_by_id('txtPassword').send_keys('123456')
    driver.br.find_element_by_id('divLoginButton').click()
    # print(driver.br.title)
    # print(driver.br.current_url)
    # print(driver.br.find_element_by_id('lnkMyAccount').text)
  

def KWS_change_quantity(driver, quantity=10):
    while True:
        if driver.br.find_element_by_id('ctl00_MainContentArea_ctl00_ctl00_ctl00_txtQty').is_displayed():
            break
        else:
            driver.br.find_element_by_xpath('//a[contains(text(),"QUANTITY")]').click()
            time.sleep(2)
    # WebDriverWait(driver.br, 2).until(lambda x: x.find_element_by_id('ctl00_MainContentArea_ctl00_ctl00_ctl00_txtQty').is_displayed())
    driver.br.find_element_by_id('ctl00_MainContentArea_ctl00_ctl00_ctl00_txtQty').clear()
    driver.br.find_element_by_id('ctl00_MainContentArea_ctl00_ctl00_ctl00_txtQty').send_keys(quantity)
    

def KWS_change_option(driver, value, option=0):
    while True:
        if driver.br.find_element_by_xpath('//select[@id="tkDropdown' + '0' + '"]').is_displayed():
            break
        else:
            driver.br.find_element_by_xpath('//a[contains(text(),"CHOOSE AN OPTION")]').click()
            time.sleep(2)
    # WebDriverWait(br, 2).until(lambda x: x.find_element_by_xpath('//select[@id="tkDropdown0"]').is_displayed())
    driver.br.find_element_by_xpath('//select[@id="tkDropdown' + str(option) + '"]').click()
    driver.br.find_element_by_xpath('//select[@id="tkDropdown' + str(option) + '"]/option[text()="' + value + '"]').click()
    

def KWS_add_product_paddle_fan(driver, quantity=10):
    driver.br.get(driver.baseURL + 'paddle-fan.aspx')
    KWS_change_quantity(driver, quantity)
    KWS_change_option(driver, 'Ivory', 0)
    driver.br.find_element_by_id('ctl00_MainContentArea_ctl00_ctl00_ctl00_addToCart').click()


def KWS_add_product_beer(driver, quantity=10):
    # driver.br.find_element_by_link_text('Engravable Beer Mug').click()
    driver.br.get(driver.baseURL + 'engravable-beer-mug.aspx')
    KWS_change_quantity(driver, quantity)
    while True:
        driver.br.find_elements('id', 'ctl00_MainContentArea_ctl00_ctl00_ctl00_addToCartPersonalized')[1].click()
        time.sleep(5)
        if driver.br.find_element_by_id('tk_modal_container').is_displayed():
            break
        else:
            driver.br.find_elements('id', 'ctl00_MainContentArea_ctl00_ctl00_ctl00_addToCartPersonalized')[1].click()
            time.sleep(5)
    # WebDriverWait(driver.br, 10).until(lambda x: x.find_element_by_id('tk_modal_container').is_displayed())
    # WebDriverWait(driver.br, 30).until_not(lambda x: x.find_element_by_id('spinner').is_displayed())
    WebDriverWait(driver.br, 10).until(lambda x: x.find_element_by_xpath('//a[@data-color-swatch-js-safe-value="Garamond"]/img').is_displayed())
    driver.br.find_element_by_xpath('//a[@data-color-swatch-js-safe-value="Garamond"]/img').click()
    driver.br.find_elements_by_class_name('steplabel')[1].click()
    time.sleep(2)
    driver.br.find_element_by_id('Line 1').clear()
    driver.br.find_element_by_id('Line 1').send_keys('Line 1')
    driver.br.find_element_by_id('Line 2').clear()
    driver.br.find_element_by_id('Line 2').send_keys('Line 2')
    # ActionChains(driver.br).context_click(driver.br.find_elements('class name','steplabel')[2]).perform() #点击右键
    time.sleep(1)
    driver.br.find_element_by_id('tk_modal_container').click()
    driver.br.find_element_by_id('addFromPersonalizationModal').click()


def KWS_go_to_shopping_cart_via_cart_flyout(driver):
    WebDriverWait(driver.br, 30).until(lambda x: x.find_element_by_id('checkoutbtn').is_displayed())
    driver.br.find_element_by_id('checkoutbtn').click()


def KWS_search(driver, kw):
    driver.br.find_element_by_id('ctl00_tkShared_Header_txtHeaderSearchBox').send_keys(kw)
    driver.br.find_element_by_css_selector('.tk_searchbtn.btn.btn-default').click()
    # driver.br.find_element_by_link_text('Engravable Beer Mug').click()

def KWS_shoping_cart_fill_address(driver):
    if not(driver.br.find_element_by_id('chkOneAddress').is_selected()):
        driver.br.find_element_by_css_selector('#chkOneAddress+label').click()
    if driver.br.find_element_by_id('CAMCheckbox1').is_selected():
        driver.br.find_element_by_css_selector('#CAMCheckbox1+label').click()
    driver.br.find_element_by_xpath('//div[@id="tkBillingAddress"]//input[@name="FirstName"]').clear()
    driver.br.find_element_by_xpath('//div[@id="tkBillingAddress"]//input[@name="FirstName"]').send_keys('Mindy')
    driver.br.find_element_by_xpath('//div[@id="tkBillingAddress"]//input[@name="LastName"]').clear()
    driver.br.find_element_by_xpath('//div[@id="tkBillingAddress"]//input[@name="LastName"]').send_keys('Krupp')
    driver.br.find_element_by_xpath('//div[@id="tkBillingAddress"]//input[@name="Email"]').clear()
    driver.br.find_element_by_xpath('//div[@id="tkBillingAddress"]//input[@name="Email"]').send_keys('viwang@xogrp.com')
    driver.br.find_element_by_xpath('//div[@id="tkBillingAddress"]//input[@name="Address1"]').clear()
    driver.br.find_element_by_xpath('//div[@id="tkBillingAddress"]//input[@name="Address1"]').send_keys('2700 W. Anderson Ln. Suite 901')
    driver.br.find_element_by_xpath('//div[@id="tkBillingAddress"]//input[@name="Address2"]').clear()
    driver.br.find_element_by_xpath('//div[@id="tkBillingAddress"]//input[@name="Address2"]').send_keys('Krupp')
    driver.br.find_element_by_xpath('//div[@id="tkBillingAddress"]//input[@name="City"]').clear()
    driver.br.find_element_by_xpath('//div[@id="tkBillingAddress"]//input[@name="City"]').send_keys('Austin')
    driver.br.find_element_by_xpath('//div[@id="tkBillingAddress"]//input[@name="State"]').clear()
    driver.br.find_element_by_xpath('//div[@id="tkBillingAddress"]//input[@name="State"]').send_keys('TX')
    driver.br.find_element_by_xpath('//div[@id="tkBillingAddress"]//input[@name="ZipCode"]').clear()
    driver.br.find_element_by_xpath('//div[@id="tkBillingAddress"]//input[@name="ZipCode"]').send_keys('78757')
    driver.br.find_element_by_xpath('//div[@id="tkBillingAddress"]//input[@name="Phone"]').clear()
    driver.br.find_element_by_xpath('//div[@id="tkBillingAddress"]//input[@name="Phone"]').send_keys('(512) 498-3340')

def KWS_shopping_cart_checkout_as_user(driver):
    #driver.br.find_element_by_xpath('//button[contains(text(),"PROCEED TO CHECKOUT")]').click()
    driver.br.find_element_by_id('txtUsername').clear()
    driver.br.find_element_by_id('txtUsername').send_keys('vicwangtest@gmail.com')
    driver.br.find_element_by_id('txtPassword').clear()
    driver.br.find_element_by_id('txtPassword').send_keys('123456')
    driver.br.find_element_by_id('divLoginButton').click()
    KWS_shoping_cart_fill_address(driver)
    driver.br.find_element_by_id('SaveAndContinue').click()
    if driver.browser == 5:
        input('please accept the alert on the test driver, then press any key to continue')
    elif driver.browser == 0:
        # driver.br.get('javascript:document.getElementById("overridelink").click();')
        driver.br.switch_to_alert().accept()


def KWS_shopping_cart_checkout_as_guest(driver):
    if 'shoppingcart.aspx' in driver.br.current_url:
        driver.br.find_element_by_xpath('//button[contains(text(),"PROCEED TO CHECKOUT")]').click()
    driver.br.find_element_by_id('divCheckoutAsGuestButton').click()
    KWS_shoping_cart_fill_address(driver)
    driver.br.find_element_by_id('SaveAndContinue').click()
    if driver.browser == 5:
        input('please accept the alert on the test driver, then press any key to continue')
    elif driver.browser == 0:
        driver.br.switch_to_alert().accept()


def KWS_shopping_cart_checkout_has_loged_in(driver):
    #driver.br.find_element_by_xpath('//button[contains(text(),"PROCEED TO CHECKOUT")]').click()
    KWS_shoping_cart_fill_address(driver)
    driver.find_element_by_id('SaveAndContinue').click()


def KWS_checkout_via_credit_card(driver):
    WebDriverWait(driver.br, 60).until(lambda x: x.find_element_by_xpath('//p[text()="Total:"]').is_displayed())
    if driver.browser in (2, 6):
        time.sleep(1)
    driver.br.find_element_by_id('CCName').clear()
    driver.br.find_element_by_id('CCName').send_keys('test')
    driver.br.find_element_by_id('CCNumber').clear()
    driver.br.find_element_by_id('CCNumber').send_keys('4111111111111111')
    driver.br.find_element_by_id('CCCCV').clear()
    driver.br.find_element_by_id('CCCCV').send_keys('123')
    driver.br.find_element_by_id('CCExpMon').click()
    driver.br.find_element_by_xpath('//select[@id="CCExpMon"]/option[text()="' + time.strftime('%m') + '"]')
    driver.br.find_element_by_id('CCExpYear').click()
    driver.br.find_element_by_xpath('//select[@id="CCExpYear"]/option[text()="' + time.strftime('%Y') + '"]')
    driver.br.find_elements_by_xpath('//a[contains(text(),"SUBMIT ORDER")]')[random.randint(0, 1)].click()
    print(time.strftime('%Y-%m-%d %H:%M:%S'), 'cc', driver.br.find_element_by_css_selector('span.text-info.underline strong').text)
    
    
def KWS_checkout_via_paypal(driver):
    WebDriverWait(driver.br, 60).until(lambda x: x.find_element_by_xpath('//p[text()="Total:"]').is_displayed())
    if driver.browser in (2, 6):
        time.sleep(1)
    driver.br.find_element_by_xpath('//a[@id="btnPaypal"]').click()
    time.sleep(1)
    while 'paypal' not in driver.br.current_url:
        driver.br.find_element_by_xpath('//a[@id="btnPaypal"]').click()
        time.sleep(2)
    inputs = driver.br.find_elements_by_tag_name('input')
    for input in inputs:
        if input.get_attribute('id') == 'login_email': 
            driver.br.find_element_by_id('login_email').clear()
            driver.br.find_element_by_id('login_email').send_keys('lyi@xogrp.com')
            driver.br.find_element_by_id('login_password').clear()
            driver.br.find_element_by_id('login_password').send_keys('testtest')
            time.sleep(1)
            driver.br.find_element_by_id('submitLogin').click()
            time.sleep(1)
            driver.br.find_element_by_id('continue').click()
            if driver.browser in (2, 6):
                while 'cardinalcommerce' not in driver.br.current_url:
                    time.sleep(1)
                driver.br.switch_to_alert().accept()
            break
        elif input.get_attribute('id') == 'email':
            driver.br.find_element_by_id('email').clear()
            driver.br.find_element_by_id('email').send_keys('lyi@xogrp.com')
            driver.br.find_element_by_id('password').clear()
            driver.br.find_element_by_id('password').send_keys('testtest')
            time.sleep(1)
            driver.br.find_element_by_css_selector('.btn.full.continue').click()
            time.sleep(1)
            driver.br.find_element_by_id('confirmButtonTop').click()
            break
    try:
        while 'cardinalcommerce' not in driver.br.current_url and 'weddingshop.theknot.com' not in driver.br.current_url:
            time.sleep(1)
        print('alert present >>>\n%s' %driver.br.switch_to_alert().text)
        driver.br.switch_to_alert().accept()
    except BaseException as e:
        print(e)
    WebDriverWait(driver.br, 30).until(lambda x: x.find_element_by_xpath('//p[text()="Total:"]').is_displayed())
    time.sleep(1)
    driver.br.find_elements_by_xpath('//a[contains(text(),"SUBMIT ORDER")]')[random.randint(0, 1)].click()
    print(time.strftime('%Y-%m-%d %H:%M:%S'), 'paypal', driver.br.find_element_by_css_selector('span.text-info.underline strong').text)
    

def KWS_checkout_via_amazon(driver):
    WebDriverWait(driver.br, 60).until(lambda x: x.find_element_by_xpath('//p[text()="Total:"]').is_displayed())
    if driver.browser in (2, 6):
        time.sleep(1)
    nowwindow = driver.br.current_window_handle
    driver.br.find_element_by_id('OffAmazonPaymentsWidgets0').click()
    time.sleep(10)
    allwindow = driver.br.window_handles
    for x in allwindow:
        if x == nowwindow:
            continue
        driver.br.switch_to_window(x)
        if driver.br.title == 'Amazon Payments: Sign In':
            break
    driver.br.find_element_by_id('ap_email').clear()
    driver.br.find_element_by_id('ap_email').send_keys('viwang@xogrp.com')
    driver.br.find_element_by_id('ap_password').clear()
    driver.br.find_element_by_id('ap_password').send_keys('testtest')
    driver.br.find_element_by_id('signInSubmit').click()
    driver.br.switch_to_window(nowwindow)
    WebDriverWait(driver.br, 30).until(lambda x: x.find_element_by_css_selector('.btn.btn-default.backToShoppingCart').is_displayed())
    WebDriverWait(driver.br, 30).until(lambda x: x.find_element_by_xpath('//p[text()="Total:"]').is_displayed())
    driver.br.find_elements_by_xpath('//a[contains(text(),"SUBMIT ORDER")]')[1].click()
    print(time.strftime('%Y-%m-%d %H:%M:%S'), 'Amazon', driver.br.find_element_by_css_selector('span.text-info.underline strong').text)

    