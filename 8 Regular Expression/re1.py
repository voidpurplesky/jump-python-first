# | : or
from re import compile

p = compile('aaa|bbb')
print(p.match('aaaccc')) #<re.Match object; span=(0, 3), match='aaa'>
print(p.match('bbbccc')) #<re.Match object; span=(0, 3), match='aaa'>
print(p.match('aaccc')) #
print(p.match('cccbbb')) #None


# ^ : 맨처음