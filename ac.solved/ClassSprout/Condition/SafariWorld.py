# 사파리월드
# https://www.acmicpc.net/problem/2420
import sys

def solution():
    n, m = map(int, sys.stdin.readline().split())
    if n > m:
        print(n-m)
    elif m > n:
        print(m-n)
    else:
        print('0')

solution()