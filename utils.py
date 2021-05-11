from re import *

pattern = compile(r'name\(([a-zA-Z]+)\)')
text = 'name(Bob), hhh, name(Alice), do you'
result = pattern.search(text)
print(result.group())
print(result.pos)
print(len(result.group()))
print(result.endpos)
result = pattern.search(text, result.pos + 1)
print(result.group())