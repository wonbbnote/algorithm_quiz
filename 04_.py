
a = input()

cycle = 0
num = a
sum = 0

while True:
    if int(num) < 10:
        sum = 0 + int(num)
        num = str(sum)*2
    else:
        sum = int(num[0]) + int(num[1])
        num = num[-1] + str(sum)[-1]
    cycle += 1
    
    if int(num) == int(a):
        break
    
print(cycle)


