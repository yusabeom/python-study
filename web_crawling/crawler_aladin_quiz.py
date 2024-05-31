
'''
# 순위 //*[@id="lst50"]/td[2]/div/span[1] rank  td 2번째
# 가수명  //*[@id="lst50"]/td[6]/div/div/div[2]  .ellipsis.rank02  td 6번째
# 앨범명  //*[@id="lst50"]/td[7]/div/div .ellipsis.rank03 td 7번째
# 노래 제목  //*[@id="lst50"]/td[6]/div/div/div[1]  .ellipsis.rank01  

#lst50

멜론일간차트순위_2024년_5월_31일_11시기준.txt

'''

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time as t
from datetime import datetime
import codecs
# 뷰티플수프 임포트
from bs4 import BeautifulSoup

d = datetime.today()

file_path = f'C:/MyWorkspace/upload/멜론일간차트순위_{d.year}_{d.month}_{d.day}_{d.hour}시기준.txt'

# 셀레늄 사용 중 브라우저 꺼짐 현상 방지 옵션
option = webdriver.ChromeOptions()
# option.add_experimental_option('detach', True)
# 크롬 드라이버를 별도로 설치하지 않고 버전에 맞는 드라이버를 사용하게 해주는 코드
service = webdriver.ChromeService(ChromeDriverManager().install())
# 크롬 드라이버를 활용하여 웹 브라우저를 제어할 수 있는 객체를 리턴
driver = webdriver.Chrome(options=option, service=service)
# 물리 드라이버로 사이트 이동 명령
driver.get('https://www.melon.com/chart/index.htm')

# selenium 으로 현재 페이지의 html 소스 코드를 전부 불러오기
src = driver.page_source
soup = BeautifulSoup(src, 'html.parser')

div_list = soup.select('tr.lst50')

# print(div_list)

with codecs.open(file_path, mode='w', encoding='utf-8') as f:
    for tr in div_list:
        song_info = tr.select('td')

        # print(song_info)

        song_rank = song_info[1].text
        album_name = song_info[6].text

        name = song_info[5].select('.rank01')
        song_name = name[0].text

        singer = song_info[5].select('.rank02 .checkEllipsis')
        singer_name = singer[0].text


        f.write(f'# {song_rank}\n')
        f.write(f'# 가수명: {singer_name}\n')
        f.write(f'# 앨범명: {album_name}\n')
        f.write(f'# 노래제목: {song_name}\n')
    
        f.write('-' * 40 + '\n')
    

        # song_name = song_info[7].select('.ellipsis.rank01')


        # song_rank = song_info[3].text
        # singer_name = song_info[7].text
        # song_name = song_info[7].text
        # album_name = song_info[8].text