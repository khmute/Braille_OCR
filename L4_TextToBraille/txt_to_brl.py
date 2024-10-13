from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


def translate(input_text):
    # WebDriver 설정
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # 헤드리스 모드
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    # WebDriver Manager를 사용하여 chromedriver 자동 설치 및 설정
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    # 해당 페이지로 이동
    driver.get("https://t.hi098123.com/braille")

    # 변환할 텍스트를 입력 (예시: 'happy')
    time.sleep(5)
    input_box = driver.find_element(By.ID, "input")  # 입력 필드 ID가 'inputTextId'라고 가정
    input_box.clear()  # 입력 필드 초기화
    input_box.send_keys(input_text)  # 변환할 텍스트 입력
    time.sleep(5)
    
    # 점역 버튼 클릭 (버튼의 ID 또는 XPath를 이용할 수 있습니다)
    # convert_button = driver.find_element(By.XPATH, "//div[@id='bar']/button[@data-name='점역 (점자로 변환)']")
    # if convert_button.is_enabled():
    #     convert_button.click()
    
    time.sleep(5)

    # 변환된 점자 결과를 가져오기
    
    output_box = driver.find_element(By.ID, "braille")
    # output_box = driver.find_element(By.ID, "plain")
    result_braille = output_box.text  # 결과 텍스트 가져오기

    print(f"입력 텍스트: {input_text}\n변환된 점자: {result_braille}")

    # 브라우저 종료
    # driver.quit()

if __name__ == "__main__":
    translate("안녕하세요, Hello world 밟지 밥지 국찌 123 \"Open\"")
    
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


def translate(input_txt_list):
    # WebDriver Manager를 사용하여 chromedriver 자동 설치 및 설정
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    # 해당 페이지로 이동
    driver.get("https://t.hi098123.com/braille")

    # 변환할 텍스트를 입력 (예시: 'happy')
    time.sleep(2)
    input_box = driver.find_element(By.ID, "input")  # 입력 필드 ID가 'inputTextId'라고 가정
    input_box.clear()  # 입력 필드 초기화
    
    for input_txt in input_txt_list:
        input_box.send_keys(input_txt)  # 변환할 텍스트 입력
        input_box.send_keys("\n")
        time.sleep(1)
    time.sleep(2)

    # 변환된 점자 결과를 가져오기

    # output_box = driver.find_element(By.ID, "braille")
    output_box = driver.find_element(By.ID, "braille")
    result_brl = output_box.text  # 결과 텍스트 가져오기

    print(f"입력 텍스트: {input_txt}\n변환된 점자: {result_brl}")
    
    # 브라우저 종료
    driver.quit()
    
    return result_brl

if __name__ == "__main__":
    with open("OCRloop/L2_BrailleToText/KakaoTalk_20241008_234355161_04.marked.txt", "r", encoding="utf-8") as f:
        for line in f:
            brl = line.strip()
            translate(brl)