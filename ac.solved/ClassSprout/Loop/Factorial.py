# 팩토리얼
# https://www.acmicpc.net/problem/10872
import sys

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

def solution():
    n = int(sys.stdin.readline().strip())
    print(factorial(n))

solution()