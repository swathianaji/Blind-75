"""
Problem: 211. Design Add and Search Words Data Structure

URL: https://leetcode.com/problems/design-add-and-search-words-data-structure/description/

Author: Swathi Anaji Revanasiddappa <srevanas@asu.edu>

"""
# It is jus like 36th problem, but when there is '.', we have to go thru every child in the dictionary

class WordDictionary:

    def __init__(self):
        self.children = {}
        self.isEow = False
        
    def addWord(self, word: str) -> None:
        currNode = self
        for letter in word:
            if letter not in currNode.children:
                newTrie = WordDictionary()
                currNode.children[letter] = newTrie
            currNode = currNode.children[letter]
        currNode.isEow = True

    def searchTrie(self, currNode, word):
        if len(word) == 0:
            return currNode.isEow
        letter = word[0]
        if letter == '.':
            for child in currNode.children:
                if self.searchTrie(currNode.children[child],word[1:]):
                    return True
            return False
        else:
            if letter in currNode.children:
                currNode = currNode.children[letter]
                return self.searchTrie(currNode,word[1:])
            else:
                return False
                
    def search(self, word: str) -> bool:
        return self.searchTrie(self,word)