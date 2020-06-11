STUDENTS = 10

score = []
scoreSum = 0

i = 0
while (i < STUDENTS):
    sc = int(input("성적 입력 : "))     # << ----------- 여기
    if(sc < 0 or sc > 100):
        print("성적 입력 오류!! 다시 입력하세요")
        continue
    scoreSum += sc
    score.append(sc)
    i += 1

scoreAvg = scoreSum / i

highScoreStudents = 0

for i in score:
    if(int(i) >= 80):
        highScoreStudents += 1
        
print("성적 평균은 {}입니다.".format(scoreAvg))
print("80점 이상 성적을 받은 학생은 {} 명입니다.".format(highScoreStudents))
