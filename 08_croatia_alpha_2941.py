# 크로아티아 알파벳 분리

croatia_word = input()
croatia_alpha_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]


for alpha in croatia_alpha_list:
    croatia_word = croatia_word.replace(alpha, "!")

print(len(croatia_word))