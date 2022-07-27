# 그룹단어 세기

num = int(input())
cnt = 0

for i in range(num):
    word = input()
    for char in range(len(word)):
        if char == len(word)-1:
            break
        elif word[char] == word[char+1]:
            pass
        elif word[char] in word[char+2:]:
            cnt += 1
            break

result_num = num - cnt
print(result_num)  
        