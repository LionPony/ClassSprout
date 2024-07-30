# 그대로 출력하기
# https://www.acmicpc.net/problem/11718
import sys

def solution():
    while True:
        line = sys.stdin.readline()
        if line == '':
            break
        else:
            print(line, end='')

solution()