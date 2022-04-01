import sys
def dfs(a, cnt):
    global answer
    if a > b:
        return
    elif a == b:
        if cnt < answer:
            answer = cnt
    dfs(a * 2, cnt + 1)
    dfs(a * 10 + 1, cnt + 1)
    

if __name__ == "__main__":
    a,b = map(int, input().split())
    answer = 100000000
    dfs(a, 1)
    if answer == 100000000:
        print(-1)
    else:
        print(answer)
