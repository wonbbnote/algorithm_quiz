test_num = int(input())
result_list = []

for i in range(test_num):
    score_list = list(map(int, input().split()))
    avg = sum(score_list[1:])/score_list[0]

    over_avg = 0
    for score in score_list[1:]:
        if score > avg:
            over_avg += 1
    
    rate = over_avg / score_list[0] * 100
    result = "%.3f%%"%rate
    result_list.append(result)

for result in result_list:
    print(result)