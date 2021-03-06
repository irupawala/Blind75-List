class Solution:
    '''
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")
    '''
    
    
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            #res += n%2 #if the last bit is 1 we will get 1 from the mod result
            res += n & 0b1 # ANDing the last bit with 1
            n = n >> 1
            
        return res

    
'''
NeetCode Solution

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= (n - 1)
            res += 1
        return res
    
'''
    
'''
Time Complexity - O(32)
Space Complexity - O(1)
'''
