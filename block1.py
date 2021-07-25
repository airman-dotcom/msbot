from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import time, selenium  
with open("C:/Users/Ali/Documents/Projects/MS bot/config.txt") as config:
    read = config.readlines()
    read1 = read[0]
    read2 = read[1]
    usr = read[6]
    pswd = read[7]
    if read1==read2:
        read3 = 1
    else:
        read3 = 2
for i in range(read3):
    with open("C:/Users/Ali/Documents/Projects/MS bot/config.txt") as config:
        input = config.readlines()
        lnk = input[i]
    if read3 == 1:
        sleep = 5520 #100 min period (starts detection script at 92 )
        print("100 min period")
        print(lnk) 
        print(int(sleep/60))       
    elif i % 2==0:
        sleep = 3120 #60 min period (starts detection script at 52)
        print("60 min period")
        print(lnk) 
        print(int(sleep/60))   
    else:
        sleep = 1920 #40 min period (starts detection script at 32)
        print("40 min period") 
        print(lnk)   
        print(int(sleep/60))   
    opt = Options()
    opt.add_experimental_option("prefs", { \
        "profile.default_content_setting_values.media_stream_mic": 1, 
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 1, 
        "profile.default_content_setting_values.notifications": 0        
    })
    driver = webdriver.Chrome('C:/Users/Ali/Documents/Projects/MS bot/chromedriver.exe',options=opt)
    wait = WebDriverWait(driver, 120)
    driver.maximize_window()
    driver.get("https://login.microsoftonline.com/common/oauth2/authorize?response_type=id_token&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346&redirect_uri=https%3A%2F%2Fteams.microsoft.com%2Fgo&state=aa568b52-8d21-4c9f-bafe-35c306905a68&&client-request-id=f39de55f-b3e9-46da-b12d-2d20a8b999d8&x-client-SKU=Js&x-client-Ver=1.0.9&nonce=a421aba0-a6c6-47c2-891e-c36a7a551b76&domain_hint=")
    time.sleep(1)
    wait.until(ec.presence_of_element_located((By.NAME,"loginfmt")))
    driver.find_element_by_name("loginfmt").send_keys(usr+ Keys.ENTER)
    time.sleep(5)
    wait.until(ec.presence_of_element_located((By.NAME,"passwd" )))
    driver.find_element_by_name("passwd").send_keys(pswd+ Keys.ENTER)
    time.sleep(1)
    wait.until(ec.url_contains("https://teams.microsoft.com/_#/"))
    time.sleep(5)
    driver.get(lnk)
    dup = driver.current_url
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[0])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.get(dup)
    time.sleep(3)
    wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="buttonsbox"]/button[2]'))).click()
    time.sleep(10)
    wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[2]/toggle-button[1]')))
    driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[2]/toggle-button[1]').click()
    driver.find_element_by_xpath('//*[@id="preJoinAudioButton"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button').click()
    wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="roster-button"]'))).click()
    parts = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-screen/div/div[2]/meeting-panel-components/calling-roster/div/div[3]/div/div[1]/accordion/div/accordion-section[2]/div/calling-roster-section/div/div[1]/button/span[3]')
    partsi = int(parts.text)
    print(partsi)
    time.sleep(sleep)
    while(1<2):
        parts = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-screen/div/div[2]/meeting-panel-components/calling-roster/div/div[3]/div/div[1]/accordion/div/accordion-section[2]/div/calling-roster-section/div/div[1]/button/span[3]')
        slc = slice(1,-1)
        partsi = int(parts.text[slc])
        print(partsi)
        time.sleep(1)
        if partsi<15:
            driver.find_element_by_xpath('//*[@id="hangup-button"]').click()
            driver.quit()