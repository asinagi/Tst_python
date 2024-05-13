import os
import pytesseract
from PIL import Image

# 설정된 테서랙트 실행 경로
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# 폴더 경로
folder_path = "C:/Users/gjgjs/Documents/Tesseract"

# 키워드 및 스코어 시트
P_keywords = ['Two Handed','Main hand','Off Hand', 'Head', 'Hand','Foot','Chest', 'Legs','Back','Accessories','Utilities']
R_keywords = ['Junk', 'Poor', 'Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Unique']
score_seat = [
    [15,22,30,45,60,90,120,175],
    [9,13,18,27,36,54,72,125],
    [7,10,14,21,28,42,56,100],
    [4,6,8,12,16,24,32,40],
    [5,7,10,15,20,30,40,50],
    [0,0,0,9,12,18,24,30],
    [2,3,4,6,8,12,16,20]
]

# 폴더 내 모든 파일에 대해 반복
total_score = 0
for filename in os.listdir(folder_path):
    # 파일 경로 생성
    file_path = os.path.join(folder_path, filename)
    
    # 파일이 이미지 파일인지 확인
    if os.path.isfile(file_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        # 이미지 열기
        img = Image.open(file_path)
        
        # 이미지에서 텍스트 추출
        result = pytesseract.image_to_string(img, lang='eng')
        
        # "hand" 및 "foot"을 "head"로 변경
        result = result.replace("hand", "head").replace("foot", "head")
        
        # 키워드가 있는지 확인하여 스코어 계산
        score = 0
        for keyword in P_keywords:
            if keyword in result:
                a = P_keywords.index(keyword)
                for keyword2 in R_keywords:
                    if keyword2 in result:
                        b = R_keywords.index(keyword2)
                        score += score_seat[a][b]
                        break  # 더 이상 검색하지 않음
                break  # 더 이상 검색하지 않음
        
        # 스코어 누적
        total_score += score

# 총 스코어 출력
print("Total score:", total_score)
