import requests
from bs4 import BeautifulSoup
from daum_news_fnc import get_news_title_and_content


# 다음 뉴스 목록 페이지에서 여러건의 뉴스 (제목+본문) 수집
url="https://news.daum.net/breakingnews/digital"    # 뉴스 목록 URL

# 1. 뉴스 목록 URL에서 1건의 뉴스 URL 추출
result = requests.get(url)  # 해당 URL의 전체 소스코드 get
soup = BeautifulSoup(result.text,"html.parser") # 전체 소스코드 BS4 읽기!

title_list = soup.select("ul.list_news2 a.link_txt")    # BS4로 뉴스 제목 목록 추출

for i, tag, in enumerate(title_list):
    new_url = tag["href"] # 해당 기사의 URL만 추출
    title, content = get_news_title_and_content(new_url)  # 튜플 언패킹
    print("=" * 100)
    print(f"URL: {new_url}")
    print(f"{i+1}뉴스제목: {title}")
    print("=" * 100)
    print(f"{i + 1}뉴스본문: {title}")
    # TODO: 태그 목록에서 URL 추출 + 단건 뉴스 수집
