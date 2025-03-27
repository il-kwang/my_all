from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

# ChromeDriver 경로 설정
driver_path = "C:/chromedriver-win64/chromedriver.exe"  # ChromeDriver의 정확한 경로
chrome_service = Service(driver_path)

# WebDriver 실행
driver = webdriver.Chrome(service=chrome_service)

try:
    # 티켓 예매 페이지로 이동
    url = "https://www.ticketlink.co.kr/sports/137/57"
    driver.get(url)
    print("티켓링크 접속 성공")
    time.sleep(2)

    # 사용자가 원하는 날짜 입력
    target_date = input("원하는 경기 날짜를 입력하세요 (예: 04.04): ").strip()

    # 예매 버튼 활성화 대기
    button_found = False
    while not button_found:
        try:
            # 원하는 날짜의 요소 찾기
            date_elements = driver.find_elements(By.CLASS_NAME, "date_num")  # 날짜 요소 클래스 이름
            for date_element in date_elements:
                if date_element.text == target_date:  # 날짜가 일치하는지 확인
                    print(f"{target_date} 경기를 찾았습니다.")
                    parent_li = date_element.find_element(By.XPATH, "./ancestor::li")  # 부모 <li> 요소 찾기
                    if parent_li.get_attribute("class") == "true":  # 버튼 활성화 여부 확인
                        print(f"{target_date} 경기의 예매 버튼이 활성화되었습니다!")
                        parent_li.click()  # 버튼 클릭
                        button_found = True
                        break
                    else:
                        print(f"{target_date} 경기의 예매 버튼이 아직 비활성화 상태입니다.")
        except NoSuchElementException:
            print("예매 버튼을 찾을 수 없습니다. 새로고침 중...")

        # 페이지 새로고침
        if not button_found:
            driver.refresh()
            time.sleep(2)  # 새로고침 간격 (필요에 따라 조정)

    print("예매 버튼 클릭 완료!")

finally:
    time.sleep(2)
    driver.quit()  # 브라우저 종료
    print("드라이버를 종료합니다.")