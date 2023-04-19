# your code 를 지우고 코드를 작성하세요.
# 5주차 과제에는 출력이나 입력을 요구하는 문제가 없습니다. print(), input() 사용하지 마세요.
# 코드 실행 시 컴파일 에러, 런타임 에러가 발생하면 해당 문제 0점 처리하겠습니다.
# 함수 이름 변경하지 마세요. 변경 시 해당 문제 0점 처리 하겠습니다.
# result, answer 변수를 사용하여 문제를 풀이하세요. 반환값은 result나 answer 변수입니다.
# 제출 기한: 2023년 4월 17일 23시 59분
# 지각 제출 기한: 2023년 4월 18일 23시 59분

import math

def calcCircleArea(r):
    area = math.pi*r*r
    result = float("%.2f"%area)
    return result

def calcLog(a, b):
    if a=='e':
        result = float("%.2f"%(math.log(int(b))))
    else:
        result = float("%.2f"%(math.log(int(b), int(a))))
    return result

def calcSin(x):
    result = float("%.2f"%(math.sin(x)))
    return result

def calcFactorial(x):
    result = math.factorial(x)
    return result

def calcCombination(n, r):
    result = math.comb(n, r)
    return result

def calculator(order):
    orders, *data = order.split()

    if orders == "원넓이:":
        answer = calcCircleArea(int(data[0]))
    elif orders == "로그:":
        answer = calcLog(data[0], data[1])
    elif orders == "사인:":
        answer = calcSin(int(data[0]))
    elif orders == "팩토리얼:":
        answer = calcFactorial(int(data[0]))
    elif orders == "조합:":
        answer = calcCombination(int(data[0]), int(data[1]))
    else:
        raise ValueError
    
    return answer

# print(calculator("원넓이: 10"))
# print(calculator("로그: e 10"))
# print(calculator("사인: 100"))
# print(calculator("팩토리얼: 5"))
# print(calculator("조합: 3 2"))