# 빠른 A+B
# https://www.acmicpc.net/problem/15552
import sys

def solution():
    t = int(sys.stdin.readline().strip())
    for i in range(t):
        a, b = map(int, sys.stdin.readline().split())
        print(a+b)

solution()