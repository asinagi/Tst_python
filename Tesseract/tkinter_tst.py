import tkinter as tk
from tkinter import filedialog
import Tst_allfolder as tst
def select_folder():
    folder_path = filedialog.askdirectory() # 폴더 선택 다이얼로그를 열어 사용자에게 폴더 선택하도록 함
    folder_path_label.config(text="폴더 주소: " + folder_path) # 선택된 폴더 주소를 라벨에 표시
    tst.Ocr(folder_path)

# Tkinter 윈도우 생성
root = tk.Tk()
root.title("폴더 주소 출력 프로그램")

# 폴더 선택 버튼 생성
select_folder_button = tk.Button(root, text="폴더 선택", command=select_folder)
select_folder_button.pack(pady=10)

# 선택된 폴더 주소를 표시할 라벨 생성
folder_path_label = tk.Label(root, text="폴더 주소: ")

folder_path_label.pack(pady=10)

# 윈도우 실행
root.mainloop()
