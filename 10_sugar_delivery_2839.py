# 상근이가 배달하는 봉지의 최소 개수를 출력한다. 
# 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.
# 3, 5 킬로그램 봉지

N = int(input())


count = 0 
while True:
    if N%5 ==0:
        count += N//5
        print(count)
        break
    N = N -3
    count += 1
    if N < 0:
        print(-1)
        break

 