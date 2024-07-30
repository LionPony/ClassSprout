# 개수 세기
# https://www.acmicpc.net/problem/10807
import sys

def solution():
    n = int(sys.stdin.readline().strip())
    sequence = list(map(int, sys.stdin.readline().split()))
    v = int(sys.stdin.readline().strip())
    print(sequence.count(v))

solution()