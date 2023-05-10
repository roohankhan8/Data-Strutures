'''
DFS Depth-First Search
search algo for graphs and trees
'''
def dfs(graph, vertex, path=[]):
    path+=[vertex]
    for neighbor in graph[vertex]:
        if neighbor not in path:
            path=dfs(graph, neighbor, path)
    return path

G={1:[2,3], 2: [4,5], 3: [5], 4:[6], 5:[6], 6:[7], 7:[]}
#G={1:[2], 2: [3,5], 3: [5], 4:[1,2,5], 5:[]}
print(dfs(G, 1))

'''
'''
def merge(left, right):
    if not len(left) or not len(right):
        return left or right
    result=[]
    i,j=0,0

    while(len(right)<len(left)+len(right)):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
        if i==len(left) or j==len(right):
            result.extend(left[i:] or right[j:])
            break
    return result
def merge_sort(list):
    if len(list)<2:
        return list
    mid = len(list)//2
    left=merge_sort(list[:mid])
    right=merge_sort(list[mid:])

    return merge(left, right)
a=[3,4,5,1,2,8,3,7,6]

print(merge_sort(a))

