# parser.py
import requests
from bs4 import BeautifulSoup

req = requests.get('https://kin.naver.com/qna/expertAnswerList.nhn?dirId=7')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

my_titles = soup.select(
    '#au_board_list > tr > td.title > a'
    )

hos_list = soup.select(
    '#au_board_list > tr > td.field > a'
    )


i=0

for hospital in hos_list :
    print(hospital.text)

print()
# my_titles는 list 객체
for title in my_titles :
    
    # Tag안의 텍스트
    print(title.text)



