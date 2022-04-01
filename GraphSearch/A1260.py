from queue import Queue

def dfs(index):
    visit[index] = 1
    print(index, end = " ")
    for node in a[index]:
        if visit[node] == 0:
            visit[node] = 1
            dfs(node)

def bfs(index):
    q= Queue()
    q.put(index)
    while not q.empty():
        temp = q.get()
        visit[temp] = 1
        print(temp, end = " ")
        for node in a[temp]:
            if visit[node] == 0:
                visit[node] = 1
                q.put(node)

if __name__ == "__main__":
    n,m,v = map(int, input().split())
    a = [[] for _ in range(n + 1)]
    for _ in range(m):
        v1,v2 = map(int, input().split())
        a[v1].append(v2)
        a[v2].append(v1)
    for i in a:
        i.sort()
    visit = [0] * (n + 1)
    dfs(v)
    print()
    visit = [0] * (n + 1)
    bfs(v)