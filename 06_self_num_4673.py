# 10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
basic_num_list = []
not_self = 0


for basic_num in range(1, 10000):
    basic_num_list.append(basic_num)


for num in range(1, 10000):
    number_list = []
    for j in str(num):
        number_list.append(int(j))

    not_self = num + sum(number_list)
    if not_self not in basic_num_list:
        continue
    elif not_self < 10000:
        basic_num_list.remove(not_self)
    
    
for self_num in basic_num_list:
    print(self_num)