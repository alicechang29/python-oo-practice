import random
import math


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, filepath):
        """Take a filepath and read a file that contains 1 word per line,
        create a list of the words, and prints the number of words read"""
        self.filepath = filepath
        self.file = open(self.filepath)
        self.word_list = self.get_lines_in_file(self.file)
        print(f"{len(self.word_list)} words read")

    def __repr__(self):
        return f"<WordFinder filepath={self.filepath}>"

    def get_lines_in_file(self, file):
        """Return a list of the lines in a file"""
        return [line.rstrip() for line in file]

    def random(self):
        """Generate a random index for a list and return the element at that
         index"""
        rand_index = math.floor(random.random() * len(self.word_list))
        return self.word_list[rand_index]

# create a subclass RandomWordFinder


class SpecialWordFinder(WordFinder):
    def __init__(self, filepath):
        super().__init__(filepath)  # gives self.word_list
        self.word_list = self.filter_word_list(self.word_list)
# skip line if blank

    def __repr__(self):
        return f"<SpecialWordFinder filepath={self.filepath}>"

    def filter_word_list(self, word_list):
        return [
            word for word in word_list
            if len(word) != 0 and word[0] != "#" and word[0] != " "
        ]

# skip line if it starts with #
# comprehension filter:
# if line.trim is empty first char is not pound sign or space, take the line

# /Users/alicechang/rithm/exercises/python-oo-practice/words.txt
