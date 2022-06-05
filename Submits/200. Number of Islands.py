class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        no_islands = 0
        island =set()
        
        def dfs(r, c):
            if (r,c) in island: return False
            island.add((r,c))
            # Direction 1
            if c+1 < COLS:
                if grid[r][c+1] != "0":
                    if (r,c+1) not in island: dfs(r,c+1) 
                        
            
            # Direction 2
            if c-1 >= 0:
                if grid[r][c-1] != "0":
                    if (r,c-1) not in island: dfs(r,c-1)
                        
                    
            # Direction 3
            if r+1 < ROWS:
                if grid[r+1][c] != "0":
                    if (r+1,c) not in island: dfs(r+1,c)
                        
                    
            # Direction 4
            if r-1 >= 0:
                if grid[r-1][c] != "0":
                    if (r-1,c) not in island: dfs(r-1,c)
                        
                    
            if r-1 < 0 or (r-1 >= 0 and grid[r-1][c] == "0") or (r-1 >= 0 and (r-1,c) in island):
                if r+1 >= ROWS or (r+1 < ROWS and grid[r+1][c] == "0") or (r+1 < ROWS and (r+1,c) in island):
                    if c-1 < 0 or (c-1 >= 0 and grid[r][c-1] == "0") or (c-1 >= 0 and (r,c-1) in island):
                        if c+1 >= COLS or (c+1 < COLS and grid[r][c+1] == "0") or (c+1 < COLS and (r,c+1) in island):
                            return True
            else:
                return False
                
    
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and dfs(r,c): no_islands += 1
                    
        return no_islands

# Neet Code Soluttion
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        islands = 0
        q = collections.deque()
        visit = set()
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            if (r not in range(rows) or
                c not in range(cols) or
                grid[r][c] == "0" or
                (r, c) in visit):
                return
            
            visit.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1
                    dfs(r, c)
        return islands
'''
