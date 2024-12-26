import re
# 1.匹配一个数字
reg=r"\d"
m=re.search(reg,"a3lsd2")
print(m)
# 2.匹配一个字符
reg=r"."
n=re.search(reg,"Mom")
print(n)