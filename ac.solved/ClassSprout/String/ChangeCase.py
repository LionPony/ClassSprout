# 대소문자 바꾸기
# https://www.acmicpc.net/problem/2744
import sys

def solution():
    word = sys.stdin.readline().strip()
    answer = ''
    for i in range(len(word)):
        if word[i].isupper():
            answer += word[i].lower()
        else:
            answer += word[i].upper()
    print(answer)

solution()