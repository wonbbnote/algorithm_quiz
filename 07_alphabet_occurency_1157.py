# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
# 단, 대문자와 소문자를 구분하지 않는다.

english_word = input().upper()
char_dict = {}

for char in english_word:
    if char not in char_dict:
        char_dict[char] = 1
    else:
        char_dict[char] += 1

max_key_list = [k for k,v in char_dict.items() if max(char_dict.values()) == v]

if len(max_key_list) > 1:
    result = "?"
else:
    result = max_key_list[0]

print(result)