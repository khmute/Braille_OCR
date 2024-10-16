import requests

# curl -X POST -F "image=@kakao/KakaoTalk_20241008_234355161_04.jpg" http://127.0.0.1:5000/run_ocr_loop

url = 'http://127.0.0.1:5000'
L1 = '/L1_OCR'
L2 = '/L2_BrailleToText'
L3 = '/L3_ContextualErrorCorrection'
L4 = '/L4_TextToBraille'
L5 = '/L5_FeedbackGenerator'

image_path = 'kakao/KakaoTalk_20241008_234355161_04.jpg'
annotation_path = 'kakao/data/annotations/5434402874708208075275189552403344913.json'

# L5 test
def test_L5():
    with open(annotation_path, 'r') as f:
        # json 파일을 그대로 넘겨주면 됨
        data = f.read()
        response = requests.post(url + L5, json=data)

    print(response.text)
    
if __name__ == '__main__':
    test_L5()