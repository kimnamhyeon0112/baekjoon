from sys import stdin

for i in range(3):
    N = int(stdin.readline())
    li = [int(stdin.readline()) for i in range(N)]
    print("+" if sum(li) > 0 else "-" if sum(li) < 0 else "0")