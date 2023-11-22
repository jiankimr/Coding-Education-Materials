"""
quizBot.py
기능:
    1) 파일에서 퀴즈와 답 읽기
    2) 퀴즈 풀기 및 정답 카운트
    3) 점수 계산 및 출력
    4) 퀴즈 추가 기능
    5) 퀴즈 추가 기능
입력 파일: 넌센스퀴즈.txt
출력 파일: 결과레포트.txt
"""

# Step 1: 파일에서 퀴즈와 답 읽기
f = open("넌센스퀴즈.txt", "r", encoding='utf-8')
lines = f.readlines()
f.close()
# Step 2: 퀴즈 풀기 및 정답 카운트
correct_count = 0  # 정답을 맞힌 횟수
for i in range(0, len(lines), 2):
    print("퀴즈:", lines[i].strip())
    user_answer = input("답을 입력하세요: ")
    if user_answer == lines[i+1].strip():
        print("정답입니다!")
        correct_count += 1
    else:
        print("틀렸습니다. 정답은", lines[i+1].strip(), "입니다.")
    print("-----")

# Step 3: 점수 계산 및 출력
score = (correct_count / (len(lines) // 2)) * 100
print("당신의 점수는", score, "%입니다.")

# Step 4: 결과 레포트 만들기
user_name = input("당신의 이름을 입력하세요: ")
with open("결과레포트.txt", "w", encoding='utf-8') as file:
    file.write("이름: " + user_name + "\n")
    file.write("점수: " + str(score) + "%")
print("점수가 결과레포트.txt 파일에 저장되었습니다!")

# Step 5: 퀴즈 추가 기능
add_quiz = input("새로운 퀴즈를 추가하시겠습니까? (예/아니오): ")
if add_quiz.lower() == "예":
    new_quiz = input("추가할 퀴즈를 입력하세요: ")
    new_answer = input("그 퀴즈의 정답을 입력하세요: ")
    with open("넌센스퀴즈.txt", "a", encoding='utf-8') as file:
        file.write("\n" + new_quiz + "\n" + new_answer)
    print("퀴즈가 성공적으로 추가되었습니다!")