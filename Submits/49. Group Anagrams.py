class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1: return [strs] 
        ans = {}
        
        for i in strs:
            list_string = list(i)
            list_string.sort()
            dict_key = "".join(map(str, list_string))
            if dict_key not in ans: ans[dict_key] = [i]
            else: ans[dict_key].append(i)
                
        return ans.values()
    
'''
Time Complexity - O(len(n) * mlogm)
Space Complexity - O(len(n))
'''
