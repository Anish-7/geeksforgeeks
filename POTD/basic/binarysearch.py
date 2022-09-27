#Binary Search
''' Given a sorted array of size N and an integer K, find the position at which K is present in the array using binary search.

Example 1:

Input:
N = 5
arr[] = {1 2 3 4 5} 
K = 4
Output: 3
Explanation: 4 appears at index 3.


Example 2:

Input:
N = 5
arr[] = {11 22 33 44 55} 
K = 445
Output: -1
Explanation: 445 is not present.


'''

class Solution:    
    def binarysearch(self, arr, n, k):
        # code here
        s=0
        l=len(arr)-1
        while(l>=s):
            mid = int((s+l)/2)
            if arr[mid]==k:
                return mid
                
            elif arr[mid]>k:
                l=mid-1
            elif arr[mid]<k:
                s=mid+1
           
        return -1 
