import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "C:/Users/user/Desktop/dev/study/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, options=chrome_options)

driver.get('https://cafe.naver.com/sooblim')

cnt = 0
while cnt < 100000:

    for i in range(35, 39):
        time.sleep(5)
        print("5초 대기")

        driver.get('https://cafe.naver.com/sooblim/' + str(i))
        time.sleep(1)
        driver.switch_to.frame("cafe_main")

        title = driver.find_element(
            By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div[1]/div/h3').text
        print(f"{title} 필독 등록 중...")

        setting = driver.find_element(
            By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div[3]/div[2]')
        setting.click()
        time.sleep(1)
        notice = driver.find_element(
            By.XPATH, '//*[@id="articleTool"]/ul/li[1]/a')
        notice.click()
        time.sleep(1)
        import_notice = driver.find_element(
            By.XPATH, '//*[@id="notice03"]')
        import_notice.click()
        confirm = driver.find_element(
            By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div[3]/div[2]/div[1]/div/div/button[2]')
        confirm.click()
        time.sleep(1)

        driver.switch_to.alert

        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(2)

        reAlert = driver.switch_to.alert
        reAlert.accept()
        time.sleep(2)
        print(f"{title} 필독 등록 완료")
        print("〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓")

    cnt += 1
    print(f"{cnt+1} 번째 반복중")
