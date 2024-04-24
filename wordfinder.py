import random as random_library


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, filepath):
        """Take a filepath and read a file that contains 1 word per line,
        create a list of the words, and prints the number of words read"""
        file = open(filepath)
        self.word_list = self.get_words_in_file(file)
        print(f"{len(self.word_list)} words read")

    def __repr__(self):
        return f"""<WordFinder length of word_list={len(self.word_list)}>"""

    def get_words_in_file(self, file):
        """Return a list of the lines in a file"""
        return [line.rstrip() for line in file]

    def random(self):
        """Generate a random index for a list and return the element at that
         index"""
        return random_library.choice(self.word_list)


class SpecialWordFinder(WordFinder):
    def __repr__(self):
        return f"""
        <SpecialWordFinder length of word_list ={len(self.word_list)}>"""

    def get_words_in_file(self, file):
        """Take a list of words and return a new list of the words that do
        not start with # or a blank space"""

        word_list = super().get_words_in_file(file)

    # TODO: let the parent class deal with its responsibilities and make the
    # subclass deal only with what's going to be different
        return [
            word for word in word_list
            if len(word) != 0 and word[0] != "#" and word != " "
        ]
