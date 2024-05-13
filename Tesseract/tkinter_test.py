import tkinter as tk

def show_input(widget, output_label):
    input_text = widget.get()
    output_label.config(text="입력한 내용: " + input_text if input_text else "입력이 없습니다.")

# Tkinter 윈도우 생성
root = tk.Tk()
root.title("다중 입력창 예제")

# 입력창과 버튼을 담을 프레임 생성
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# 입력창과 버튼을 여러 개 생성하여 프레임에 배치
for i in range(3):
    # 입력창
    entry = tk.Entry(frame, width=30)
    entry.grid(row=i, column=0, padx=5, pady=5)

    # 버튼
    button_text = "입력 확인 " + str(i+1)  # 버튼 텍스트 지정
    button = tk.Button(frame, text=button_text, command=lambda widget=entry: show_input(widget, output_label))
    button.grid(row=i, column=1, padx=5, pady=5)

# 출력 레이블 추가
output_label = tk.Label(root, text="", width=40)
output_label.pack(pady=10)

# 윈도우 크기 설정
root.geometry("400x300")

# 윈도우 실행
root.mainloop()
