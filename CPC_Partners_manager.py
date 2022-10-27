from re import L
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import os, sys, time, pyautogui, pyperclip, requests

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UI_PATH = "CPC_Partners_manager.ui"

class MainDialog(QDialog) :
    def __init__(self) :
        QDialog.__init__(self, None)
        uic.loadUi(os.path.join(BASE_DIR,UI_PATH), self)

        self.collect_main_radioButton.setChecked(True)
        self.crawling_srt_btn.clicked.connect(self.newspick_crowling_srt)
        self.News_Pick_ID_edit.setText('awldnjs2@naver.com')
        self.News_Pick_PW_edit.setText('wldnjs12#')






    
    def newspick_crowling_srt(self) :
        # 브라우저 꺼짐 방지
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])               # 불필요한 에러 메세지 없애기, 부착된 장치가 작동하지 않습니다 등.....
        service = Service(executable_path=ChromeDriverManager().install())                          #크롬드라이버매니저를 이용해서 크롬드라이버를 최신버전으로 자동으로 설치해줌
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

        # 주소 이동
        self.driver.implicitly_wait(5)   # 웹페이지가 로딩 될때까지 5초는 기다림
        # driver.maximize_window()    # 화면 최대화
        self.driver.set_window_position(0,0)
        self.driver.set_window_size(1920, 1080)
        self.driver.get("https://partners.newspic.kr/login")

        self.newspick_login()

        if self.collect_main_radioButton.isChecked() == 1 :
            self.newspick_crawling()
        
        elif self.collect_category_radioButton.isChecked() == 1 :
            if self.story_checkBox.isChecked() == 1 :
                print('스토리 카레고리 수집')
                self.driver.get("https://partners.newspic.kr/main/index#30")
                self.newspick_crawling()

            if self.joke_checkBox.isChecked() == 1 :
                print('유머 카테고리 수집')
                self.driver.get("https://partners.newspic.kr/main/index#24")
                self.newspick_crawling()

            if self.racy_joke_checkBox.isChecked() == 1 :
                print('응큼세포(15금)카테고리 수집')
                self.driver.get("https://partners.newspic.kr/main/index#35")
                self.newspick_crawling()

            if self.politics_checkBox.isChecked() == 1 :
                print('정치 카테고리 수집')
                self.driver.get("https://partners.newspic.kr/main/index#31")
                self.newspick_crawling()

            if self.entertainment_hot_issue_checkBox.isChecked() == 1 :
                print('연예가화제 카테고리 수집')
                self.driver.get("https://partners.newspic.kr/main/index#36")
                self.newspick_crawling()

            if self.accident_checkBox.isChecked() == 1 :
                print('사건사고 카테고리 수집')
                self.driver.get("https://partners.newspic.kr/main/index#12")
                self.newspick_crawling()

            if self.idol_checkBox.isChecked() == 1 :
                print('아이돌 카테고리 수집')
                self.driver.get("https://partners.newspic.kr/main/index#28")
                self.newspick_crawling()

            if self.sport_checkBox.isChecked() == 1 :
                print('스포츠 카테고리 수집')
                self.driver.get("https://partners.newspic.kr/main/index#7")
                self.newspick_crawling()

            if self.economy_checkBox.isChecked() == 1 :
                print('경제 카테고리 수집')
                self.driver.get("https://partners.newspic.kr/main/index#14")
                self.newspick_crawling()

            if self.vehicle_checkBox.isChecked() == 1 :
                print('자동차 카테고리 수집')
                self.driver.get("https://partners.newspic.kr/main/index#17")
                self.newspick_crawling()

            if self.tip_checkBox.isChecked() == 1 :
                print('꿀팁 카테고리 수집')
                self.driver.get("https://partners.newspic.kr/main/index#23")
                self.newspick_crawling()

            if self.society_checkBox.isChecked() == 1 :
                print('사회 카테고리 수집')
                self.driver.get("https://partners.newspic.kr/main/index#32")
                self.newspick_crawling()

            if self.global_checkBox.isChecked() == 1 :
                print('글로벌 카테고리 수집')
                self.driver.get("https://partners.newspic.kr/main/index#39")
                self.newspick_crawling()

            if self.pet_checkBox.isChecked() == 1 :
                print('반려동물 카테고리 수집')
                self.driver.get("https://partners.newspic.kr/main/index#3")
                self.newspick_crawling()

            if self.entertainment_checkBox.isChecked() == 1 :
                print('연예 카테고리 수집')
                self.driver.get("https://partners.newspic.kr/main/index#6")
                self.newspick_crawling()

            if self.overseas_baseball_checkBox.isChecked() == 1 :
                print('해외야구 카테고리 수집')
                self.driver.get("https://partners.newspic.kr/main/index#16")
                self.newspick_crawling()

            if self.overseas_soccer_checkBox.isChecked() == 1 :
                print('해외축구 카테고리 수집')
                self.driver.get("https://partners.newspic.kr/main/index#15")
                self.newspick_crawling()

            if self.travel_checkBox.isChecked() == 1 :
                print('여행 카테고리 수집')
                self.driver.get("https://partners.newspic.kr/main/index#37")
                self.newspick_crawling()

            if self.life_pick_checkBox.isChecked() == 1 :
                print('생활픽 카테고리 수집')
                self.driver.get("https://partners.newspic.kr/main/index#33")
                self.newspick_crawling()

            if self.NNA_Korea_checkBox.isChecked() == 1 :
                print('NNA코리아 카테고리 수집')
                self.driver.get("https://partners.newspic.kr/main/index#38")
                self.newspick_crawling()

            if self.BBC_News_checkBox.isChecked() == 1 :
                print('BBC News 카테고리 수집')
                self.driver.get("https://partners.newspic.kr/main/index#11")
                self.newspick_crawling()


    def newspick_login(self) : 
        # 로그인
        ID = self.News_Pick_ID_edit.text()
        PW = self.News_Pick_PW_edit.text()

        login = self.driver.find_elements(By.CSS_SELECTOR, ".input-group > .input-m")
        login[0].click()
        login[0].send_keys(ID)
        login[1].click()
        login[1].send_keys(PW)
        self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-confirm.btn-block.mt-16").click()    # 로그인버튼 클릭.

    def newspick_crawling(self) : 
        scroll_down = self.driver.find_element(By.CSS_SELECTOR, "body")         # body 엘리먼트를 찾음.
        scroll_down.send_keys(Keys.END)                                         # 키보드의 END키를 입력 -> 스크롤이 끝까지 내려감.
        time.sleep(2)                                                           # 스크롤 사이 페이지 로딩 시간 -> 한번에 내려버리면 부하가 걸릴 수 있기 때문

        item_info = []
        item_title_list = []
        item_site_uproad_day_list = []
        item_source_list = []
        item_img_url_list = []
        item_detail_page_list = []
        item_share_url_list = []

        if self.collect_main_radioButton.isChecked() == 1 :
            items_element = ".cate-row"

        elif self.collect_category_radioButton.isChecked() == 1 :
            items_element = ".row"

        # 메인페이지에서 아이템 정보 크롤링
        item_amount = int(self.item_amount_edit.text())
        while True :
            items = self.driver.find_elements(By.CSS_SELECTOR, items_element)
            if len(items) > item_amount :
                break
            else :
                scroll_down.send_keys(Keys.END)

        i = 1
        for item in items :
            if i > item_amount :
                break
            item_img_url_list.append(item.find_element(By.CSS_SELECTOR, '.thumb > img').get_attribute('src'))
            item_detail_page_list.append(item.find_element(By.CSS_SELECTOR, '.info > a').get_attribute('href'))
            i += 1

        # 상세페이지에서 공유 url 크롤링
        i = 1
        for item_detail_page in item_detail_page_list :
            print(f'{i}페이지 수집 중')
            self.driver.get(item_detail_page)
            item_title_list.append(self.driver.find_element(By.CSS_SELECTOR, '.tit.text_overflow3').text)
            item_site_uproad_day_list.append(self.driver.find_element(By.CSS_SELECTOR, '.headline_view > .source.en > span:nth-child(2)').text)
            item_source_list.append(self.driver.find_element(By.CSS_SELECTOR, '#divAuthor').text)
            self.driver.find_element(By.CSS_SELECTOR, 'body > div.fixed.bottom_bar_pc > div > ul > li:nth-child(1) > button').click()
            item_share_url_list.append(pyperclip.paste())
            i += 1
        print()

        item_info = [item_title_list, item_site_uproad_day_list, item_source_list, item_img_url_list, item_detail_page_list, item_share_url_list]
        self.print_info(item_info)
        
    def print_info(self, item_info) :
        # 크롤링한 정보 출력.
        for i in range(len(item_info[0])) :
            print(f'{i+1}. 제목 : {item_info[0][i]}')
            print(f'{i+1}. 올라온 날짜 : {item_info[1][i]}')
            print(f'{i+1}. 출처 : {item_info[2][i]}')
            print(f'{i+1}. 이미지url : {item_info[3][i]}')
            print(f'{i+1}. 상세url : {item_info[4][i]}')
            print(f'{i+1}. 공유url : {item_info[5][i]}')
            print()
        
        # response = requests.get(item_info[3][0])
        # print(f'response : {response}')
        # # print(response.content)
        # pixmap = QPixmap(response.text)
        # self.test_label.setPixmap(pixmap)

        self.title_label.setText(item_info[0][0])
        self.posting_date_label.setText(item_info[1][0])
        self.collect_date_label.setText("수집일")
        self.distribution_date_label.setText("배포일")
        self.source_label.setText(item_info[2][0])
        self.detail_URL_label.setText(item_info[4][0])
        self.Share_URL_label.setText(item_info[5][0])








QApplication.setStyle("fusion")
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()

sys.exit(app.exec_())



