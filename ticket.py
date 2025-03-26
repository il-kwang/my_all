from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver_path = "C:/Users/302/Documents/new/chromedriver-win64/chromedriver.exe" # 크롬 드라이버 경로
driver = webdriver.Chrome()

try:
    url = "https://www.ticketlink.co.kr/home"
    driver.get(url)
    print("티켓링크 접속 접속 성공")
    time.sleep(2)
    
    # 로그인 버튼 클릭
    click_login = driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/div[2]/div[2]/div[1]/a')
    click_login.click()
    
    print("모든 작업이 완료되었습니다.")
    
    time.sleep(500)
    
finally:
    time.sleep(2)
    driver.quit()#브라우저 종료
    print("드라이버를 종료합니다.")