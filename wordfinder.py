import random
import math


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, filepath):
        """Take a filepath and read a file that contains 1 word per line,
        create a list of the words, and prints the number of words read"""
        self.file = open(filepath)
        self.word_list = self.get_lines_in_file(self.file)
        print(f"{len(self.word_list)} words read")

    def get_lines_in_file(self, file):
        """Return a list of the lines in a file"""
        return [line.rstrip() for line in file]

    def random(self):
        """Generate a random index for a list and return the element at that
         index"""
        rand_index = math.floor(random.random() * len(self.word_list))
        return self.word_list[rand_index]
