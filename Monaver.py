import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
import math
from bs4 import BeautifulSoup
from eliminate import my_eliminate

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = chrome_options)

browser.get("https://m.ad.search.naver.com/search.naver?where=m_expd&query=장기렌트")

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

for i in results:
    print(i)
    print('\n')
    #print(ad_url)

#                 title = inner_list.find_all('span',class_ = "lnk_tit")
#                 bnk = 'empty'
#                 title_1 = title[0].text #노출되는 제목이 최대 3개. 1개 또는 2개일 경우 다른것으로 채워야함. 
#                 title_2 = bnk if len(title) == 1 else title[1].text
#                 title_3 = bnk if len(title) != 3 else title[2].text
#                 ad_url = inner_list.find('a', class_ = "url").string #url 가져오기, 경로가 명확해서 string 사용
#                 event = inner_list.find_all('p', class_ = "ad_dsc")
#                 ad_promo = bnk if len(event) == 1 else event[0].text
#                 ad_desc = event[0].text if len(event) == 1 else event[1].text
#                 ad_period = inner_list.find('em', class_="txt").text
# from requests import get
# from bs4 import BeautifulSoup
# import pandas as pd
# from eliminate import my_eliminate
# import math

# def total_search_count(keyword):
#     base_url = "https://ad.search.naver.com/search.naver?"
#     response = get(f"{base_url}query={keyword}&pagingIndex=1")

#     if response.status_code != 200:
#         print("Can't request Web search naver")
#     else:
#         soup = BeautifulSoup(response.text, "html.parser")
#         inner = soup.find_all('div', class_ = "inner")[0]
#         total_search = inner.find('span', class_="num_result").text
#         total = total_search.split('/')[1].strip("건")
#         search_count = int(total)
#         return search_count

# def page_count(keyword):
#     page_count = math.ceil(total_search_count(keyword)/25)
#     return page_count

# def extract_Web_naver(keyword):
#     results = []
#     search_page = page_count(keyword)
#     for page in range(1, search_page + 1):
#         base_url = "https://ad.search.naver.com/search.naver?"

#         response = get(f"{base_url}query={keyword}&pagingIndex={page}")

#         if response.status_code != 200:
#             print("Can't request Web search naver")
#         else:
#             soup = BeautifulSoup(response.text, "html.parser")
#             inner = soup.find_all('div', class_ = "inner") 
#             del inner[0] #첫번째 리스트는 검색결과에 관한 값이므로 지워준다.
#             for inner_list in inner:
#                 title = inner_list.find_all('span',class_ = "lnk_tit")
#                 bnk = 'empty'
#                 title_1 = title[0].text #노출되는 제목이 최대 3개. 1개 또는 2개일 경우 다른것으로 채워야함. 
#                 title_2 = bnk if len(title) == 1 else title[1].text
#                 title_3 = bnk if len(title) != 3 else title[2].text
#                 ad_url = inner_list.find('a', class_ = "url").string #url 가져오기, 경로가 명확해서 string 사용
#                 event = inner_list.find_all('p', class_ = "ad_dsc")
#                 ad_promo = bnk if len(event) == 1 else event[0].text
#                 ad_desc = event[0].text if len(event) == 1 else event[1].text
#                 ad_period = inner_list.find('em', class_="txt").text
#                 search_data = {
#                     'title1' : my_eliminate(title_1),   #줄바꿈, 공백, 쉼표, 탭과 같은 파일변환시 문제되는 문자열 삭제함수
#                     'title2' : my_eliminate(title_2),
#                     'title3' : my_eliminate(title_3),
#                     'ad_url' : ad_url,
#                     'ad_event' : my_eliminate(ad_promo),
#                     'ad_desc' : my_eliminate(ad_desc),
#                     'ad_period': my_eliminate(ad_period)
#                 }
#                 results.append(search_data)
#     return results