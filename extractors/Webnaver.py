from requests import get
from bs4 import BeautifulSoup
import pandas as pd
from extractors.eliminate import my_eliminate

def extract_Web_naver(keyword):
    base_url = "https://ad.search.naver.com/search.naver?"
    search_page = "1"

    response = get(f"{base_url}query={keyword}&pagingIndex={search_page}")

    if response.status_code != 200:
        print("Can't request Web search naver")
    else:
        results = []
        soup = BeautifulSoup(response.text, "html.parser")
        inner = soup.find_all('div', class_ = "inner") 
        del inner[0] #첫번째 리스트는 검색결과에 관한 값이므로 지워준다.
        for inner_list in inner:
            title = inner_list.find_all('span',class_ = "lnk_tit")
            bnk = 'empty'
            title_1 = title[0].text #노출되는 제목이 최대 3개. 1개 또는 2개일 경우 다른것으로 채워야함. 
            title_2 = bnk if len(title) == 1 else title[1].text
            title_3 = bnk if len(title) != 3 else title[2].text
            ad_url = inner_list.find('a', class_ = "url").string #url 가져오기, 경로가 명확해서 string 사용
            event = inner_list.find_all('p', class_ = "ad_dsc")
            ad_promo = bnk if len(event) == 1 else event[0].text
            ad_desc = event[0].text if len(event) == 1 else event[1].text
            ad_period = inner_list.find('em', class_="txt").text
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