from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver_path = "C:/chromedriver-win64/chromedriver.exe" # 크롬 드라이버 경로
driver = webdriver.Chrome()

try:
    url = "https://www.ticketlink.co.kr/sports/137/57"
    driver.get(url)
    print("티켓링크 접속 접속 성공")
    time.sleep(2)
    
    # 로그인 버튼 클릭
    click_login = driver.find_element(By.CLASS_NAME,'header_util_link')
    click_login.click()
    
    time.sleep(1)
    
    # 로그인 정보 입력
    user_id = "parkik9472@gmail.com"
    user_pw = "p/w"
    
    iframe = driver.find_element(By.ID, 'loginIframe')  # 로그인 iframe의 id 속성 값
        # ID 입력 필드에 값 입력
    id_input = driver.find_element(By.ID, 'loginId')  # ID 입력 필드의 id 속성 값
    id_input.send_keys(user_id)
    
    # 비밀번호 입력 필드에 값 입력
    pw_input = driver.find_element(By.ID, 'password')  # 비밀번호 입력 필드의 id 속성 값
    pw_input.send_keys(user_pw)
    
    # 로그인 버튼 클릭
    login_button = driver.find_element(By.CLASS_NAME, 'btn_login')  # 로그인 버튼의 클래스 이름
    login_button.click()
    
    print("모든 작업이 완료되었습니다.")
    
    time.sleep(500)
    
finally:
    time.sleep(2)
    driver.quit()#브라우저 종료
    print("드라이버를 종료합니다.")