# 과제 안 내신 분..?
# https://www.acmicpc.net/problem/5597
import sys

def solution():
    student = []
    for i in range(1, 31):
        student.append(i)
    for i in range(28):
        student.remove(int(sys.stdin.readline().strip()))
    print(student[0])
    print(student[1])

solution()