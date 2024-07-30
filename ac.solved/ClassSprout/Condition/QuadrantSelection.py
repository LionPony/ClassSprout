# 사분면 고르기
# https://www.acmicpc.net/problem/14681
import sys

def solution():
    x = int(sys.stdin.readline().strip())
    y = int(sys.stdin.readline().strip())
    
    if x > 0:
        if y > 0:
            print('1')
        else:
            print('4')
    else:
        if y > 0:
            print('2')
        else:
            print('3')
        
solution()