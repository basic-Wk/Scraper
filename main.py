from Web_naver import extract_Web_naver, total_Web_search_count
from Mo_naver import extract_Mobile_naver, total_Mobile_search_count

keyword = "장기렌트"
Web_naver = extract_Web_naver(keyword)
Web_count = total_Web_search_count(keyword)
Mobile_naver = extract_Mobile_naver(keyword)
Mobile_count = total_Mobile_search_count(keyword)
file = open(f"search_{keyword}_Web_naver.csv", "w", encoding="utf-8-sig")
file.write(f"총 검색건수는 {Web_count}건 입니다.\n")
file.write("title1, title2, title3, ad_url, ad_event, ad_desc, ad_period\n")

for i in Web_naver:
    file.write(f"{i['title1']},{i['title2']},{i['title3']},{i['ad_url']},{i['ad_event']},{i['ad_desc']},{i['ad_period']}\n")
file.close()

file = open(f"search_{keyword}_Mobile_naver.csv", "w", encoding="utf-8-sig")
file.write(f"총 검색건수는 {Mobile_count}건 입니다.\n")
file.write("title1, title2, title3, ad_url, ad_event, ad_desc, ad_period\n")

for j in Mobile_naver:
    file.write(f"{j['title1']},{j['title2']},{j['title3']},{j['ad_url']},{j['ad_event']},{j['ad_desc']},{j['ad_period']}\n")
file.close()