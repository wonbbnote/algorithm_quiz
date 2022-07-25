# 시간 계산
# 45분 전 시간 도출

h, m = map(lambda x : int(x) , input().split())

if m >= 45:
    result_h = h
    result_m = m-45
elif m < 45:
    if h ==0:
        result_h = 23
    else:
        result_h = h-1
    result_m = 60-(45-m)

print(result_h, result_m)