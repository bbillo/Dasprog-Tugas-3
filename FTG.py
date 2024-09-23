N, M = map(int, input().split())

for i in range(N):
    for j in range(N):
        if (i < M) or (i >= N - M) or (j < M) or (j >= N - M):
            print("*", end="")
        else:
            print(" ", end="")
    print()
