def gcd(a, b) : 

    # a를 b로 나눈 나머지(b')가 없으면 a는 a와 b의 최대공약수
    if b == 0 :
        return a

    # 재귀함수 호출부
    return gcd(b, a%b)

a = 4
b = 6
print(gcd(a,b))
