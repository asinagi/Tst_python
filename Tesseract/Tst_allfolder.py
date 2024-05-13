import os
import pytesseract
from PIL import Image

def Ocr(address):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    folder_path = address

    P_keywords = ['Two Handed','primary','secondary', 'Head', 'Hand','Foot','Chest', 'Legs','Back','Accessories','Utilities']
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

    total_score = 0
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        if os.path.isfile(file_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img = Image.open(file_path)
            result = pytesseract.image_to_string(img, lang='eng')
            
            result = result.replace("hand", "head").replace("foot", "head")
            result = result.replace("Back", "chest").replace("Legs", "chest")
            
            # 키워드가 있는지 확인하여 스코어 계산
            score = 0
            keyword_found = False
            for keyword in P_keywords:
                if keyword in result:
                    if keyword == 'primary':
                        # 'Primary'가 발견되었지만 'Two Handed'가 발견되지 않았을 때
                        if 'Two Handed' in result:
                            score += score_seat[P_keywords.index('Two Handed')][R_keywords.index('Common')]
                            keyword_found = True
                            break  # 더 이상 검색하지 않음
                    else:
                        a = P_keywords.index(keyword)
                        for keyword2 in R_keywords:
                            if keyword2 in result:
                                b = R_keywords.index(keyword2)
                                score += score_seat[a][b]
                                keyword_found = True
                                break  # 더 이상 검색하지 않음
                        if keyword_found:
                            break  # 더 이상 검색하지 않음
            total_score += score

    print("Total score:", total_score)
