# 이상한 기호
# https://www.acmicpc.net/problem/15964
import sys

def solution():
    a, b = map(int, sys.stdin.readline().split())
    print((a+b)*(a-b))

solution()