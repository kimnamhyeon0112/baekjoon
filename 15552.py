# jupyter는 stdin이 구성되지 않아 stdin.readline()을 실행할 수 없다.
# 따라서 파이썬으로 처리한다.
import sys
cycle = int(input())

for i in range(cycle):
   A,B = map(int, sys.stdin.readline().split())
   print(A+B)