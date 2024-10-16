from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


def translate(input_brl_list):
    # WebDriver Manager를 사용하여 chromedriver 자동 설치 및 설정
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    # 해당 페이지로 이동
    driver.get("https://t.hi098123.com/braille")

    # 변환할 텍스트를 입력 (예시: 'happy')
    time.sleep(10)
    # 역점역 버튼 클릭 (버튼의 ID 또는 XPath를 이용할 수 있습니다)
    convert_button = driver.find_element(By.XPATH, "//div[@id='bar']/button[@data-name='역점역 (점자해석/묵역)']")
    convert_button.click()
    
    time.sleep(2)
    
    input_box = driver.find_element(By.ID, "input")  # 입력 필드 ID가 'inputTextId'라고 가정
    input_box.clear()  # 입력 필드 초기화
    
    for input_brl in input_brl_list:
        input_box.send_keys(input_brl)  # 변환할 텍스트 입력
        input_box.send_keys("\n")
        time.sleep(1)
    time.sleep(2)
    

    # 변환된 점자 결과를 가져오기
    # output_box = driver.find_element(By.ID, "braille")
    output_box = driver.find_element(By.ID, "plain")
    result_text = output_box.text  # 결과 텍스트 가져오기

    print(f"입력 텍스트: {input_brl}\n변환된 점자: {result_text}")
    
    # 브라우저 종료
    driver.quit()
    
    return result_text

if __name__ == "__main__":
    with open("OCRloop/L2_BrailleToText/KakaoTalk_20241008_234355161_04.marked.txt", "r", encoding="utf-8") as f:
        for line in f:
            brl = line.strip()
            translate(brl)