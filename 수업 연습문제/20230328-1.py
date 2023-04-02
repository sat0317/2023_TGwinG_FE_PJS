def num_judgement(x):
    return ("짝수", "홀수")[int(x)%2]

def num_judgement_using_if(x):
    if int(x)%2:
        return "홀수"
    else:
        return "짝수"

print(5, num_judgement(5), "입니다")
print(10, num_judgement(10), "입니다")
print("3", num_judgement("3"), "입니다")
print("8", num_judgement("8"), "입니다")
print()
print(5, num_judgement_using_if(5), "입니다")
print(10, num_judgement_using_if(10), "입니다")
print("3", num_judgement_using_if("3"), "입니다")
print("8", num_judgement_using_if("8"), "입니다")
