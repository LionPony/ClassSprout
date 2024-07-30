# 행렬 덧셈
# https://www.acmicpc.net/problem/2738
import sys

def solution():
    n, m = map(int, sys.stdin.readline().split())
    matrixA = []
    matrixB = []
    
    for i in range(n):
        matrixA.append(list(map(int, sys.stdin.readline().strip().split())))
    for i in range(n):
        matrixB.append(list(map(int, sys.stdin.readline().strip().split())))
    
    answer = []
    for i in range(n):
        answerRow = []
        for j in range(m):
            answerRow.append(matrixA[i][j] + matrixB[i][j])
        answer.append(answerRow)
    
    for i in range(n):
        for j in range(m):
            print(answer[i][j], end=' ')
        print('')

solution()