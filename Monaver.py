from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

browser.get("https://m.ad.search.naver.com/search.naver?where=m_expd&query=장기렌트")

while(True):
    pass