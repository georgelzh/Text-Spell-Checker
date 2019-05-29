#!Python 3
# Spelling Checker
# It receives the letters of a word and automatically corrects it.
# Zhihong Li
# 5/26/2019
#
import sys, re

inFile = sys.argv[1]    # dictionary path
textFile = sys.argv[2]  # textFile path
outputFile = sys.argv[3]  # output path


class Node(object):         # create a node class
    def __init__(self, value=None):    # initialization of the node, you could store a value
        self.value = value             # put the input value into value
        self.children = {}             # create a dictionary/sub-trie
        self.isEndOfWord = False       # a bool that tells whether a node the an end node of a word


class Trie(object):
    # trie data structure class
    def __init__(self):
        self.node = Node()      # create

    def insert(self, key):      # insert function
        node = self.node        # create a new node
        for letter in key:
            if letter in node.children:
                node = node.children[letter]   # if letter is in the trie, then move current node to the node of the letter
            else:                              # else create a new node with the letter in it, and move to the node.
                new_node = Node(letter)
                node.children[letter] = new_node
                node = new_node
        node.isEndOfWord = True                 # when finish inserting the word, mark the last node of the letter as end of word.

    def search(self, key, prev_node = None):
        if prev_node is not None:
            node = prev_node
        else:
            node = self.node
        for letter in key:
            if letter not in node.children:
                return False
            else:
                node = node.children[letter]
        return True, node


# loading your dictionary
t = Trie()              # create a new tri

def loadDict(infile_Path):
    with open(inFile, "r", encoding= 'UTF-8') as w:
        words = w.read().splitlines()
    for word in words:
        t.insert(word)


# read the text
def load_text_get_pure_word(text_file_path):
    with open(text_file_path, "r") as t:    # load the text file
        lines = t.read()
    wordRege = re.compile(r'\w+', re.IGNORECASE)   # create a regular expression that looks for only word
    pure_word = wordRege.findall(lines)             # get(find) all the word in the text file
    return pure_word


def get_wrong_spell_word(word_list):
    final_text = []
    for word in word_list:
        if not t.search(word):  # return the word as it is.
            final_text.append(word)
    return ' '.join(final_text)       # return the string(text) with underlined wrong spelled word


def write_file(output_text, output_path):
    with open(output_path, "w", encoding='UTF-8') as o:
        o.write(output_text)


loadDict(inFile)
pure_word = load_text_get_pure_word(textFile) # get a list with only words in it
final_output_text = get_wrong_spell_word(pure_word)     # store the wrong spelled word as a string
write_file(final_output_text, outputFile)               # write out the wrong spelled word




# reference: https://routley.io/tech/2017/07/16/tries.html
# English dictionary source: https://github.com/dwyl/english-words
# https://www.geeksforgeeks.org/trie-insert-and-search/
