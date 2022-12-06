import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import math
from bs4 import BeautifulSoup
from eliminate import my_eliminate
from requests import get

def extract_Mobile_naver(Keyword):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = chrome_options)

    browser.get(f"https://m.ad.search.naver.com/search.naver?where=m_expd&query={Keyword}")

    #response = get(f"{base_url}query={keyword}&pagingIndex=1")

    more_count = math.ceil(int(browser.find_element(By.ID, '_total_count').text)/15)

    for i in range(1, more_count):
        browser.find_element(By.ID, "_get_more").click()
        time.sleep(2)

    source_code = browser.execute_script("return document.body.innerHTML;")
    soup = BeautifulSoup(source_code, 'html.parser')

    inner = soup.find_all('div', class_= 'lst_cont')
    results = []

    for inner_list in inner:
        title = inner_list.find_all('span', class_ = 'tit')
        bnk = 'empty'
        title_1 = title[0].text
        title_2 = bnk if len(title) == 1 else title[1].text
        title_3 = bnk if len(title) != 3 else title[2].text
        ad_url = inner_list.find('span', class_ = 'url_link').text
        event = inner_list.find_all('div', class_ = 'pr')
        ad_promo = event[0].text if len(event) == 1 else bnk
        ad_desc = inner_list.find('div', class_ = 'desc_area').text
        ad_period_area = inner_list.find('div', class_ = 'period_area')
        ad_period = ad_period_area.find('em').text
        search_data = {
        'title1' : my_eliminate(title_1),   #줄바꿈, 공백, 쉼표, 탭과 같은 파일변환시 문제되는 문자열 삭제함수
        'title2' : my_eliminate(title_2),
        'title3' : my_eliminate(title_3),
        'ad_url' : ad_url,
        'ad_event' : my_eliminate(ad_promo),
        'ad_desc' : my_eliminate(ad_desc),
        'ad_period': my_eliminate(ad_period)
        }
        results.append(search_data)
    return results

def total_Mobile_search_count(Keyword):
    response = get(f"https://m.ad.search.naver.com/search.naver?where=m_expd&query={Keyword}")
    soup = BeautifulSoup(response.text, "html.parser")
    total_count = soup.find('em', class_ = 'total').text
    return total_count