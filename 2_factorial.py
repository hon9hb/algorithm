def factorial(n) :

    # 1이하일 때 1을 리턴한다.
    if n <= 1 :
        return 1

    # 재귀함수 호출부
    return n * factorial(n-1)

n = 5
print(factorial(n))
