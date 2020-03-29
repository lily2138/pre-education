"""11. 최대공약수를 구하는 함수를 구현하시오

예시
<입력>
print(gcd(12,6))

<출력>
6
"""
def gcd(num1,num2):
    for i in range(num1,0,-1):
        if num1%i==0 and num2%i==0:
            return i
            break

print(gcd(36,48))