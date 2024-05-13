# 텍스트 파일 경로
file_path = "test.txt"

try:
    # 텍스트 파일 열기
    with open(file_path, "r") as file:
        # 파일의 각 줄을 읽어서 터미널에 출력
        for line in file:
            print(line, end="")
except FileNotFoundError:
    print(f"파일을 찾을 수 없습니다: {file_path}")
except Exception as e:
    print("오류 발생:", e)
