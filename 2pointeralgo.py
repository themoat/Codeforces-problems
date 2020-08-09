# # To make the complexity better from O(n3) or better than O(n2), we use Two pointer algo, now how it works?
# # We make two pointers, i and j where i starts from, the beginning, while j starts from the end. So till how
# # long does it continue. So, basically, we move the i pointer forward if the sum of the i'th element and the jth
# # element is less than the given sum we wanna see for. But if at any point the sum exceeds, we bring the j pointer
# # backwards. and at any point when it's equal we break the loop and return true. That simple.
#
# t = int(input())
# for i in range(0,t):
#     n = int(input())
#     a = list(map(int,input().split()))
#
#     a.sort()
#
#     for i in range(0,n-2):
#         if twosum(a,1,-a[i]) is true:
#             print("True")
#         else:
#             print("False")
#
# def twosum(a,i,x):
#
#     j = len(a)-1
#
#     while(i<j):
#         if a[i] + a[j]<x:
#             i+=1
#         elif a[i] + a[j]>x:
#             j-=1
#         else:
#
#             return True
#

#Longest length of substring without repeated characters.

def Solution():

    n = len(string)
    visited={}
    max_length = 0
    start = 0

    for i in range(0,n):
        if string[i] in visited:
            start=max(start,visited[string[i]] + 1)

        visited[string[i]] = i
        max_length = max(max_length,i-start + 1)
    return max_length



