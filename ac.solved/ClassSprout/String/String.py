# 문자열
# https://www.acmicpc.net/problem/9086
import sys

def solution():
    t = int(sys.stdin.readline().strip())
    for i in range(t):
        word = sys.stdin.readline().strip()
        print(word[0], word[-1], sep='')

solution()