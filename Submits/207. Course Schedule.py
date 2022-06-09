class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i:[] for i in range(numCourses)}
        visited = [False for i in range(numCourses)] # To not revisit the node
        
        # populate adjaceny list
        for lst in prerequisites:
            adj_list[lst[0]].append(lst[1])        
        
        def dfs(i, traversal_list):            
            if i in traversal_list:
                return False
            
            visited[i] = True
            
            traversal_list.append(i)            
            for j in adj_list[i]:
                if not dfs(j, traversal_list): return False            
            traversal_list.remove(i)
            
            adj_list[i] = [] # This line is super-crucial. After visiting the node we want to make its adjacency list empty so that we 
            # do not have revisit all of its neighbors again because we have checeked once that there is no loop ending on this node.
            # this one-line plays a crucial role in passing the time-complexity
            return True
        
        for i in range(numCourses):
            traversal_list = []
            if not visited[i]:
                if not dfs(i, traversal_list): return False
  
        return True        

'''
Time Complexity - O(|V|+|E|)
Space Complexity - O(|V|+|E|) for adjacency list
'''
