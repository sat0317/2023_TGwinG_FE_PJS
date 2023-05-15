# your code 를 지우고 코드를 작성하세요.
# 7주차 과제에는 출력이나 입력을 요구하는 문제가 없습니다. print(), input() 사용하지 마세요.
# 코드 실행 시 컴파일 에러, 런타임 에러가 발생하면 해당 문제 0점 처리하겠습니다.
# 함수 이름 변경하지 마세요. 변경 시 해당 문제 0점 처리 하겠습니다.
# 제출 기한: 2023년 5월 15일 23시 59분
# 지각 제출 기한: 2023년 5월 16일 23시 59분
# 3번 문제는 table을 사용해 풀이해주세요. (dictionary 활용) 다른 방법으로 구현하면 감점 또는 0점 처리하겠습니다.

# 1번
def relativeComp(a: set, b: set):
    c = sorted(list(a - b)) #a - b returns relative complement, and sort it because of problem's requirement.
    if len(c) == 0: #if there is no value of relative complement, the len(c) will be zero.
        c = 0
    return c

# 2번
def alphabetFreq(word):
    table = {}
    for i in word:
        try: #If it is no alphabet, it will occer the error. The problem was limited to the alphabet, but I just added it.
            i = i.upper()
        except:
            pass

        try:
            table[i]+=1 #If it occurs error, the alphabet is not on the table
        except:
            table[i]=1

    mxt, mxv = 0, "?" #default value. mxt means max-counted-times and mxv means max-counted-alphabet
    for v, t in table.items():
        if mxt < t:
            mxt, mxv = t, v
        elif mxt == t: #There are no case the mxv is more than two. So, this case's answer is '?'.
            mxv = "?"
    
    return mxv

