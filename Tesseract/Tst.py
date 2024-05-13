import pytesseract
from PIL import Image

# 설정된 테서랙트 실행 경로
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# 이미지 열기
a = Image.open("RogueCowl.jpg")

# 이미지에서 텍스트 추출
result = pytesseract.image_to_string(a, lang='eng')

# 추출된 텍스트에서 특정 키워드 찾기
P_keywords = ['Two Handed','Main hand','Off Hand', 'Head', 'Hand','Foot','Chest', 'Legs','Back','Accessories','Utilities']
R_keywords = ['Junk', 'Poor', 'Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Unique']
found_R_keywords = []
found_P_keywords=[]
score_seat = [
    [15,22,30,45,60,90,120,175],
    [9,13,18,27,36,54,72,125],
    [7,10,14,21,28,42,56,100],
    [4,6,8,12,16,24,32,40],
    [5,7,10,15,20,30,40,50],
    [0,0,0,9,12,18,24,30],
    [2,3,4,6,8,12,16,20]
]
result = result.replace("hand", "head").replace("foot", "head")
for keyword in R_keywords:
    if keyword in result:
        found_R_keywords.append(keyword)
for keyword2 in P_keywords:
    if keyword2 in result:
        found_P_keywords.append(keyword2)

# 찾은 키워드 출력
print("Found keywords:", found_R_keywords)
print("Found keyword2 : ", found_P_keywords)

a=P_keywords.index(found_P_keywords[0])
b=R_keywords.index(found_R_keywords[0])

score=score_seat[a][b]
print(score)