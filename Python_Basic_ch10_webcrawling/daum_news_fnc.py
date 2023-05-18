import requests
from bs4 import BeautifulSoup

# 함수
# input: URL
# output: 제목, 본문

# 기존: 제목함수, 본문함수 따로 만든다. 이번에는 실습이니까 그냥 진행
# -> 이유: 함수 만들 때 하나의 함수에 다수의 기능을 넣기 X

def get_news_title_and_content(url):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    title = doc.select("h3.tit_view")[0].get_text()
    contents = doc.select("section > p")
    content = ""
    # contents.pop(-1)
    for tag in contents:
        content = content + tag.get_text()
    print(f"뉴스본문: {content}")

    return title, content  # 튜플 형식으로 리턴