import re
n, m = map(int, input().split())
arr = ''.join([''.join(t) for t in zip(*[input() for _ in range(n)])])
print(re.sub(r'\b[^a-zA-Z0-9]+\b', r' ', arr))
# Example of input:
# 7 3
# Tsi
# h%x
# i #
# sM 
# $a 
# #t%
# ir!
