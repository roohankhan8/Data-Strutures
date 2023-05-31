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
Merge Sort
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

'''Hashing'''
import hashlib
# Create a hashlib object for a specific hash algorithm (e.g., SHA-256)
hash_object = hashlib.sha256()
# Convert the input data to bytes (hashlib functions require bytes)
data = "Hello, World!".encode()
# Update the hash object with the data
hash_object.update(data)
# Get the hash value as a hexadecimal string
hash_value = hash_object.hexdigest()
print("Hash value:", hash_value)
data = "Hello, World!"
hash_value = hash(data)
print("Hash value:", hash_value)

#Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    # Recursively sort the two halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    # Merge the sorted halves
    merged = merge(left_half, right_half)
    return merged
def merge(left, right):
    merged = []
    i = j = 0
    # Merge the two halves by comparing elements
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # Add the remaining elements from either left or right
    while i < len(left):
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1
    return merged
array = [9, 5, 1, 3, 8, 4, 2, 7, 6]
sorted_array = merge_sort(array)
print(sorted_array)