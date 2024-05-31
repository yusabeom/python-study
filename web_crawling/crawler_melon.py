
'''
- 순위
- 가수명
- 앨범명
- 노래 제목

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
file_path = f'C:/MyWorkspace/upload/멜론일간차트순위_{d.year}년_{d.month}월_{d.day}일_{d.hour}시기준.txt'
# 셀레늄 사용 중 브라우저 꺼짐 현상 방지 옵션
option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
# 크롬 드라이버를 별도로 설치하지 않고 버전에 맞는 드라이버를 사용하게 해주는 코드
service = webdriver.ChromeService(ChromeDriverManager().install())
# 크롬 드라이버를 활용하여 웹 브라우저를 제어할 수 있는 객체를 리턴
driver = webdriver.Chrome(options=option, service=service)
# 물리 드라이버로 사이트 이동 명령
driver.get('https://www.melon.com/')
t.sleep(2)
driver.find_element(By.XPATH, '//*[@id="gnb_menu"]/ul[1]/li[1]/a/span[2]').click()
t.sleep(2)

with codecs.open(file_path, mode='w', encoding='utf-8') as f:
    rank = 1

    # selenium 으로 현재 페이지의 html 소스 코드를 전부 불러오기
    src = driver.page_source
    soup = BeautifulSoup(src, 'html.parser')
    
    while rank <= 100:
        class_name = 'lst100' if rank > 50 else 'lst50'
        tr_list = soup.find_all('tr', class_=class_name)

        for tr in tr_list:
            song_info = tr.select('td')

            song_title = tr.find('div', class_='rank01').find('a').text.strip()
            singer = tr.find('div', class_='rank02').find('a').text.strip()
            album_title = tr.find('div', class_='rank03').find('a').text.strip()

            print(f'순위: {rank}, 가수명: {singer}, 앨범명: {album_title}, 노래 제목: {song_title}')
            f.write(f'순위: {rank}\n가수명: {singer}\n앨범명: {album_title}\n노래 제목: {song_title}\n')
            f.write('-' * 40 + '\n')

            rank += 1

            if rank > 50 and rank <= 51:
                break