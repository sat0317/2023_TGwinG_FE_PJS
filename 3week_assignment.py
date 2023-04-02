# 1번
def grade(score):
    if 90<=score<=100:
        return "A"
    elif 80<=score:
        return "B"
    elif 70<=score:
        return "C"
    elif 60<=score:
        return "D"
    else:
        return "F"

#이렇게도 풀 수 있음
def gradeAnotherSolution(score):
    if 0<=score<=100:
        return "FFFFFFDCBAA"[score//10]
    return "F"


# 2번
def quadrant(x, y):
    if y>0:
        if x>0:
            return "제 1사분면"
        else:
            return "제 2사분면"
    else:
        if x>0:
            return "제 4사분면"
        else:
            return "제 3사분면"

#이렇게도 풀 수 있음
def quadrantAnotherSolution(x, y):
    return [["제 2사분면", "제 1사분면"], ["제 3사분면", "제 4사분면"]] [y<0][x>0]


# 3번
def leapYear(year):
    if year%400==0:
        return "윤년입니다."
    elif year%100==0:
        return "윤년이 아닙니다."
    elif year%4==0:
        return "윤년입니다."
    else:
        return "윤년이 아닙니다."

#이렇게도 풀 수 있음
def leapYearAnotherSolution(year):
    return ("윤년입니다.","윤년이 아닙니다.","윤년이 아닙니다.")[bool(year%4)+(year%400 and not year%100)]


# 4번
def dice(a, b, c):
    if a==b==c:
        return 10000+a*1000
    elif a==b:
        return 1000+a*100
    elif b==c:
        return 1000+b*100
    elif a==c:
        return 1000+c*100
    else:
        return max((a, b, c))*100

#튜플을 이용해 간결하게 처리하기
def diceAnotherSolution(a, b, c):
    if a==b==c:
        return 10000+a*1000
    t=(a, b, c, a)
    for i in range(3):
        if t[i]==t[i+1]:
            return 1000+t[i]*100
    return max(t)*100


# 5번
def alarm(time):
    TIME_SEPARATE = 45
    time += 2400
    minute = (time//100) * 60 + (time%100) - TIME_SEPARATE
    hh = (minute // 60) % 24
    mm = minute % 60
    return str(hh) + "시 " + str(mm)+"분"
