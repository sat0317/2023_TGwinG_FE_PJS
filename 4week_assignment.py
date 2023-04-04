# # your code 를 지우고 그 부분에 본인의 코드를 작성해주세요.
# 4주차 과제에는 출력이나 입력을 요구하는 문제가 없습니다. print(), input() 사용하지 마세요.
# 코드 실행 시 컴파일 에러, 런타임 에러가 발생하면 해당 문제 0점 처리하겠습니다.
# 함수 이름 변경하지 마세요. 변경 시 해당 문제 0점 처리 하겠습니다.
# 제출 기한 : 2023년 4월 10일 23시 59분
# 지각 제출 기한 : 2023년 4월 11일 23시 59분

# 1번
def double(lst):
    data = tuple(sorted(lst))
    cnt  = 0

    for x in range(len(data)):
        t = data[x]*2
        for j in data[x+1:]:
            if j==t:
                cnt+=1
                break
            if j>t:
                break

    return cnt

# 2번    
def pascal(n):
    ans = []
    for r in range(n):
        nCr = 1
        for _ in range(1, r+1):
            nCr *= n-_
        for _ in range(1, r+1):
            nCr //= _
        ans.append(nCr)
    return ans

# 3번
def beerRefrigerator(n):
    best = []
    mx   = -1
    for a in range(1, n+1):
        if n % a == 0:
            for b in range(1, n//a+1):
                if (n//a)%b == 0:
                    c = n//a//b
                    t = a*b + b*c + c*a
                    if mx > t or mx == -1:
                        mx   = t
                        best = [a, b, c]
    best.sort(reverse=True)
    return str(best[0])+" X "+str(best[1])+" X "+str(best[2])

# 4번
def matrixMul(mat1, mat2):
    m = len(mat1)
    n = len(mat2)
    p = len(mat2[0])
    ans = [[0 for _ in range(p)] for __ in range(m)]
    for i in range(m):
        for j in range(n):
            for k in range(p):
                ans[i][k] += mat1[i][j] * mat2[j][k]
    return ans