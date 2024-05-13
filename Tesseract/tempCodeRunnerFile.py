import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

a=Image.open("roguehead.png")
result=pytesseract.image_to_string(a, lang='eng')
print(result)