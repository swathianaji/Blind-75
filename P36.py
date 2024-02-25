"""
Problem: 208. Implement Trie (Prefix Tree)

URL: hhttps://leetcode.com/problems/implement-trie-prefix-tree/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""

# Trie: Prefix tree
# Each node has a boolean variable to denote if it is the end of an inserted word
# and children dictionary, where key is character and value is the corresponding node object
# Insert function: traverse through the word, check if each letter is in the trie in that order, if not create a new node
# add it in children dict of the current node, update isEow bool variable at the end
# Search function: Traverse through the word, check if each letter is in the trie in that order, if not return False
# is all letters are there, check if the node with last letter has isEow True (only then it represents a complete word)
# StartsWith function: Works same as the search function, except that isEow need not be True at the last letter of the given prefix.

class Trie:

    def __init__(self):
        self.children = {}
        self.isEow = False

    def insert(self, word: str) -> None:
        currNode = self
        for letter in word:
            if letter not in currNode.children:
                newTrie = Trie()
                currNode.children[letter] = newTrie
            currNode = currNode.children[letter]
        currNode.isEow = True

    def search(self, word: str) -> bool:
        currNode = self
        for letter in word:
            if letter in currNode.children:
                currNode = currNode.children[letter]
            else:
                return False
        return currNode.isEow == True

    def startsWith(self, prefix: str) -> bool:
        currNode = self
        for letter in prefix:
            if letter in currNode.children:
                currNode = currNode.children[letter]
            else:
                return False
        return True

