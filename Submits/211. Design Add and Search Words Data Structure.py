class TreeNode(object):  
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for i, c in enumerate(word):
            if c not in cur.children:
                cur.children[c] = TreeNode()
            cur = cur.children[c]
        cur.endOfWord = True
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def dfs(i, cur):
            if i == len(word):
                return cur.endOfWord
            
            if word[i] != ".":
                if word[i] not in cur.children: return False
                else:
                    return dfs(i+1, cur.children[word[i]])
                
            else:
                
                for val in cur.children.values():
                    if dfs(i+1, val): return True                       
                return False
            
        return dfs(0, self.root)


# NeetCode Solution
'''
class TrieNode:
    def __init__(self):
        self.children = {} # a : TrieNode
        self.word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True
        
    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word
        
        return dfs(0, self.root)
'''

'''
Neetcode solution is right as well but exceeds the time limit sometimes
This solution uses the dfs even when character is not "." hence using dfs for both the cases
Neetcode uses iterartive approach for normal character while uses recursive for "." character
Time Complexity - O(N) for Trie building, O(word_len) for searching
Memory Complexity - O(N) for TrieNodes for all the nodes
'''
