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
        return f"""
        <WordFinder filepath={self.filepath}
        word_list={self.word_list}>
        """

    def get_lines_in_file(self, file):
        """Return a list of the lines in a file"""
        return [line.rstrip() for line in file]

    def random(self):
        """Generate a random index for a list and return the element at that
         index"""
        rand_index = math.floor(random.random() * len(self.word_list))
        return self.word_list[rand_index]


class SpecialWordFinder(WordFinder):
    def __init__(self, filepath):
        """Take a filepath and read a file that contains 1 word per line,
        create a list of the words, prints the number of words read,
        and filters the word_list to have only words that do not begin
        with a # or blank space"""
        super().__init__(filepath)
        self.word_list = self.filter_word_list(self.word_list)

    def __repr__(self):
        return f"""
        <SpecialWordFinder filepath={self.filepath}
        word_list ={self.word_list}>
        """

    def filter_word_list(self, word_list):
        """Take a list of words and return a new list of the words that do
        not start with # or a blank space"""
        return [
            word for word in word_list
            if len(word) != 0 and word[0] != "#" and word[0] != " "
        ]
