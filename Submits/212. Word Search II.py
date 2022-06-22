class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

        
class Solution:
    def findWords(self, board, words):
        #max_len_word = max(words, key = lambda x:len(x))
        root = TrieNode()
        for w in words:
            root.addWord(w)
            
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()
        
        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or 
                r == ROWS or c == COLS or
                board[r][c] not in node.children or (r, c) in visit):  
                # or len(word) > len(max_len_word) ):
                return
            
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
            
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        
        return list(res)
    
S = Solution()
print(S.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]))        


'''
Time Complexity - O(m.n.4^mn) with trie # m.n for traversing the board and 4^mn because we're traversing in 4 directions for DFS. Without the use of Trie it will be O(#ofwords.m.n.4^mn)
Space Complexity - O(#Nooflettersofwords) (To store Trie) + O(m.n) to store the recursion stack
'''
