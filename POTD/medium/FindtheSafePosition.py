''' 
There are n people standing in a circle (numbered clockwise 1 to n) waiting to be executed. The counting begins at point 1 in the circle and proceeds around the circle in a fixed direction (clockwise). In each step, a certain number of people are skipped and the next person is executed. The elimination proceeds around the circle (which is becoming smaller and smaller as the executed people are removed), until only the last person remains, who is given freedom.
Given the total number of persons n and a number k which indicates that k-1 persons are skipped and kth person is killed in circle. The task is to choose the place in the initial circle so that you are the last one remaining and so survive.

Example 1:

Input:
n = 2, k = 1
Output:
2
Explanation:
Here, n = 2 and k = 1, then safe position is
2 as the person at 1st position will be killed.

Example 2:

Input:
n = 4, k = 2
Output:
1
Explanation:
The safe position is 1.

'''

''' 
hint:
The problem has following recursive structure.

  josephus(n, k) = (josephus(n - 1, k) + k-1) % n + 1
  josephus(1, k) = 1

After the first person (kth from begining) is killed, n-1 persons are left. 
So we call josephus(n – 1, k) to get the position with n-1 persons. But the position returned by josephus(n – 1, k) will consider the position starting from k%n + 1.
So, we must make adjustments to the position returned by josephus(n – 1, k).
'''

class Solution:
    def safePos(self, n, k):
#         if(n == 1):
#             return 1
#         return (self.safePos(n-1,k)+k-1)%n+1
        
        cir=[i for i in range(1,n+1)]
        return rec(cir,k)
def rec(cir,k):
    k=k-1   #in terms of index that is if k=32 k-1=31
    index=k # index =31
    while len(cir)>1:
        cir.pop(index) #directly pop the index value first
        index=(index+k)%len(cir) #then calculate the index value adusting
    return cir[0]
