# (세 자리 수) × (세 자리 수)
# 두 세자리 자연수가 주어지면 곱셈과정에서 나타나는 수식 및 결과 도출

a = int(input())
b = int(input())

first = a * (b%10)
second = a * ((b%100)//10)
third = a * (b//100)

print(first)
print(second)
print(third)

result = first + 10*second + 100*third
print(result)

