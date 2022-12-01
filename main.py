from Webnaver import extract_Web_naver,total_search_count

keyword = "장기렌트"
naver = extract_Web_naver(keyword)
count = total_search_count(keyword)
print("총 검색건수는", count, "건 입니다.")
file = open(f"search_{keyword}_Web_naver.csv", "w", encoding="utf-8-sig")
file.write("title1, title2, title3, ad_url, ad_event, ad_desc, ad_period\n")

for resultfile in naver:
    file.write(f"{resultfile['title1']},{resultfile['title2']},{resultfile['title3']},{resultfile['ad_url']},{resultfile['ad_event']},{resultfile['ad_desc']},{resultfile['ad_period']}\n")
file.close()