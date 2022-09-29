'''Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.


Example 1:

Input: 
N = 5
arr[]= {0 2 1 2 0}
Output:
0 0 1 2 2
Explanation:
0s 1s and 2s are segregated 
into ascending order.

Example 2:

Input: 
N = 3
arr[] = {0 1 0}
Output:
0 0 1
Explanation:
0s 1s and 2s are segregated 
into ascending order. ''''


''' hint 



These are the folowing steps:

    Maintain 3 variables low, high and mid
        low - all elements before low are 0
        mid - all elements between low and mid are 1
        high - all elements after high are 2
    Initially low, mid are set at 0 and high is at n-1
    Now, we iterate mid from 0 to high, and for every element
        if it is equal to 0, we swap it with element at low, and increement low and mid
        else if it is equal to 2, we swap it with element at high, and decreement high
        else we just increement mid (i.e element is equla to 1)
    This method ensures partition, as low and high maintain elements according to their values, and then change their positions, ensuring all elements before low are lower than low_value and all elements after high are higher than high_value
'''
#User function Template for python3

class Solution:
    def sort012(self,arr,n):
                # code here
        l=0
        m=0
        h=n-1
        while m<=h:
            if arr[m]==0:
                # arr[l],arr[m]=arr[m],arr[l]
                t=arr[l]
                arr[l]=arr[m]
                arr[m]=t
                l+=1
                m+=1
            elif arr[m]==2:
                arr[h],arr[m]=arr[m],arr[h]
                h-=1
            else:
                m+=1
        return arr
                
                
                
            
    #   l=0
    #     r=n-1
    #     m=0
    #     while(m<=r):
    #         if(arr[m]==1):
    #           m+=1
    #         elif(arr[m]==0):
    #             t=arr[l]
    #             arr[l]=arr[m]
    #             arr[m]=t
    #             l+=1
    #             m+=1
    #         elif(arr[m]==2):
    #             arr[r],arr[m]=arr[m],arr[r]
    #             r-=1  
    
    
        # sorted=True
        # while sorted == False:
        #     for i in range(n-1):
        #         if arr[i]>arr[i+1]:
        #             arr[i],arr[i+1]=arr[i+1],arr[i]
        #             sorted =False
        # return arr
        
        # zer=arr.count(0)
        # one=arr.count(1)
        # two=arr.count(2)
        # res= [0]*zer+[1]*one+[2]*two
        # # return res
        # zer=[arr[i] for i in range(n) if arr[i]==0 ]
        # one=[arr[i] for i in range(n) if arr[i]==1 ]
        # two=[arr[i] for i in range(n) if arr[i]==2 ]
        # arr=zer+one+two
        
        # return arr
#         if len(arr)<=1:
#             return arr
        
#         pivot =arr[0]
#         less_half,great_half = split(arr)
#         less=self.sort012(less_half,len(less_half))
#         great=self.sort012(great_half,len(great_half))
        
#         return less+[pivot]+great
        
# def split(list):
#     less_half =[]
#     great_half= []
        
#     for i in range(1,len(list)):              # compare from the 1st element as the first element is pivot
#         if list[i]<list[0]:
#             less_half.append(list[i])
#         else:
#             great_half.append(list[i])
    
#         return less_half,great_half 


