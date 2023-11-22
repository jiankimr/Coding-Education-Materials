"""
quizBot.py
기능:
    1) 파일에서 퀴즈와 답 읽기
    2) 퀴즈 풀기 및 정답 카운트
    3) 점수 계산 및 출력
    4) 결과 레포트 만들기
    5) 퀴즈 추가 기능
입력 파일: 넌센스퀴즈.txt
출력 파일: 결과레포트.txt
"""

#Step 1: 파일에서 퀴즈와 답 읽기
# 파일 열기
# 'r'은 읽기 모드입니다. 파일명을 정확히 기입해주세요.
# UTF-8 인코딩을 명시적으로 지정해주세요.
f = open("파일명", "r", encoding='utf-8')


# 파일 내용 읽기
# readlines 함수는 파일의 모든 줄을 리스트로 반환합니다.
lines = f.readlines()

# 파일 닫기
f.close()

# 힌트: '파일명'을 넌센스 퀴즈가 담긴 실제 파일 이름으로 바꿔주세요.


#Step 2: 퀴즈 풀기 및 정답 카운트
"""
# 정답 카운트 변수 초기화
correct_count = 0

# 퀴즈 풀기 로직 구현
# 사용자에게 퀴즈를 보여주고 답을 입력받습니다.
for i in range(0, len(lines), 2):  # 퀴즈와 답이 번갈아 나오므로, 2씩 증가합니다.
    # 퀴즈를 보여줍니다. lines[i]는 퀴즈를 포함하고 있는 줄입니다.
    print("퀴즈:", lines[i])

    # 사용자의 답을 입력받습니다.
    user_answer = input("답을 입력하세요: ")

    # 정답을 확인합니다. lines[i+1]는 답을 포함하고 있는 줄입니다.
    if user_answer == lines[i+1].strip():
        # 여기에 코드를 작성하세요.
        # 정답 카운트 변수에 1을 더하세요.
    else:
        print("틀렸습니다. 정답은", lines[i+1].strip(), "입니다.")
    print("-----") #사용자가 잘 확인할 수 있도록 구분선 삽입

# 힌트: 사용자의 입력을 받은 후 정답과 비교하여 correct_count를 증가시켜야 합니다.

"""

#Step 3: 점수 계산 및 출력
"""
# 점수 계산
# 정답률을 계산하여 score 변수에 저장하세요.
score = 0

# 점수 출력
# 계산된 점수를 출력합니다.
print("점수:", score)

# 힌트: 총 퀴즈 수는 'len(lines) / 2'입니다. 정답률은 'correct_count / (len(lines) / 2) * 100'으로 계산합니다.
"""

#Step 4: 결과 레포트 만들기
"""
# 사용자 이름 입력 받기
user_name = input("당신의 이름을 입력하세요: ")

# 결과 레포트 파일에 기록
# 'w' 모드는 파일이 이미 존재하면 내용을 지우고 새로 씁니다.
with open("output.txt", "w") as file:
    # 파일에 사용자 이름을 기록하세요.
    # 파일에 사용자의 점수를 기록하세요.

# 힌트: 파일에 문자열을 쓸 때는 write 함수를 사용합니다. user_name과 score를 문자열로 변환하여 기록해야 합니다.

"""

#Step 5: 퀴즈 추가 기능
"""
# 퀴즈 추가 여부 물어보기
add_quiz = input("새로운 퀴즈를 추가하시겠습니까? (예/아니오): ")

# 퀴즈와 답 추가 로직 구현
if add_quiz.lower() == "예":
    # 새 퀴즈를 입력받습니다.
    new_quiz = input("추가할 퀴즈를 입력하세요: ")
    # 새 답을 입력받습니다.
    new_answer = input("그 퀴즈의 정답을 입력하세요: ")

    # 파일에 새 퀴즈와 답을 추가합니다.
    # 'a' 모드는 파일의 끝에 내용을 추가합니다.
    # 여기에 코드를 작성하세요.

# 힌트: 파일을 추가 모드('a')로 열고, write 함수를 사용해 새로운 퀴즈와 답을 각각 파일에 씁니다.

"""

