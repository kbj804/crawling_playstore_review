from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
import time
import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('C:/Users/DBLAB/PycharmProjects/crawl_playstore/chromedriver')
#driver.get('https://play.google.com/store/apps/details?id=com.sundaytoz.kakao.wbb&hl=ko')
driver.get('https://play.google.com/store/apps/details?id=com.sundaytoz.astovekr.joy&hl=ko&showAllReviews=true')

#review_all = driver.find_element_by_css_selector('.XnFhVd')
time.sleep(2)
#review_all.click()
result=[]
print(datetime.datetime.now())

flag = True
endCnt = 0
saveCnt = 0
remove_script = '''
document.querySelectorAll('div[jscontroller="H6eOGe"]').forEach(e => e.parentNode.removeChild(e))
'''

show_commentAll_script = '''
for (const btn of document.getElementsByClassName("LkLjZd ScJHi OzU4dc  ")) btn.click()
'''


def save_reviews():
    # html = driver.page_source
    # soup = BeautifulSoup(html,'html.parser')

    # for div in soup.find_all('div', {'class' : 'UD7Dzf'}):
    #    result.append(div.text)
    reviews = driver.find_elements_by_xpath('//div[@class="UD7Dzf"]/span[@jsname="bN97Pc"]')
    for review in reviews:
        result.append(review.text)


while (flag):
    try:
        time.sleep(2)
        driver.find_element_by_tag_name('body').send_keys(Keys.END)
        endCnt += 1
        saveCnt += 1
        print(saveCnt)
        driver.execute_script(show_commentAll_script)
        more_review = driver.find_element_by_css_selector('.PFAhAf')
        if more_review:  # 더보기
            endCnt = 0
            more_review.click()


    except:
        driver.find_element_by_tag_name('body').send_keys(Keys.END)
        if saveCnt > 5:
            time.sleep(1)
            save_reviews()
            driver.execute_script(remove_script)  # 저장한 댓글 삭제
            saveCnt = 0

        elif endCnt == 10:
            print('###FINISH###')
            print(datetime.datetime.now())
            save_reviews()
            flag = False

