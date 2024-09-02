# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):
        """Returns a list of words that are anagrams of the initialized word."""
        # Normalize the word by sorting its letters
        sorted_word = sorted(self.word)
        # Find and return all matching anagrams from the input list
        return [w for w in words if sorted(w) == sorted_word]