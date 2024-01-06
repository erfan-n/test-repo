n = input().split()
m = int(n[1])
n = int(n[0])
matrix = []
temp_list = []
for i in range(n):
    matrix.append(list(input().split()))
graph = {}
tetsts = 0
syiayiua = ''
for i in range(n):
    for j in range(m): #djdlhh
        if matrix[i][j]=='1':
            graph[str(i)+str(j)] = []
            if j-1>=0 and matrix[i][j-1]=='1':
                if str(i)+str(j) in graph:
                    graph[str(i)+str(j)].append(str(i)+str(j-1))
                else:
                    graph[str(i)+str(j)].append(str(i)+str(j-1))
            if j+1<m and matrix[i][j+1]=='1':
                if str(i)+str(j) in graph:
                    graph[str(i)+str(j)].append(str(i)+str(j+1))
                else:
                    graph[str(i)+str(j)] = list(str(i)+str(j+1))
            if i-1>=0 and matrix[i-1][j]=='1':
                if str(i)+str(j) in graph:
                    graph[str(i)+str(j)].append(str(i-1)+str(j))
                else:
                    graph[str(i)+str(j)] = list(str(i-1)+str(j))            
            if i+1<n and matrix[i+1][j]=='1':
                if str(i)+str(j) in graph:
                    graph[str(i)+str(j)].append(str(i+1)+str(j))
                else:
                    graph[str(i)+str(j)] = list(str(i+1)+str(j))
visited = set()
color = []
khkas = 0
colour = 0
def dfs(visited,graph,root,colour):
    if root not in visited:
        if colour not in color:
            color.append(colour)
        visited.add(root)
        for neighbor in graph[root]:
            dfs(visited,graph,neighbor,colour)
for i in graph:
    dfs(visited,graph,i,colour)
    colour += 1
print(color.__len__()+(len(graph.keys())-visited.__len__()))
