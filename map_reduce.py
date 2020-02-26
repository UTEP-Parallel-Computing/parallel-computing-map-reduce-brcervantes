#!/usr/bin/env python

'''
Assignment 2 Map Reduce

@author Briana Cervantes
'''

import sys
import re
import pymp as mp
from timeit import default_timer as timer


def read_file(file_name):
    '''
    Reads provided file and returns the file in string format.
    '''

    with open(file_name) as file:
        file_str = file.read().lower()
    return file_str


def find_words(word_list, file_str):
    '''
    Finds the total number of occurances for word list in a string.
    '''

    for word in word_list:
        find = re.findall(word, file_str)
        word_list[word] += len(find)
    return word_list


def main():
    '''
    parallelize the word search among 8 different documents.
    '''

    words = ["hate",
            "love",
            "death",
            "night",
            "sleep",
            "time",
            "henry",
            "hamlet",
            "you",
            "my",
            "blood",
            "poison",
            "macbeth",
            "king",
            "heart",
            "honest"]

    word_list = mp.shared.dict()

    start = timer()

    #parallelize this part
    with mp.Parallel(8) as p:
        for word in words:
            word_list[word] = 0

        file_list = mp.shared.dict()

        file_list["shakespeare1.txt"] = ""
        file_list["shakespeare2.txt"] = ""
        file_list["shakespeare3.txt"] = ""
        file_list["shakespeare4.txt"] = ""
        file_list["shakespeare5.txt"] = ""
        file_list["shakespeare6.txt"] = ""
        file_list["shakespeare1.txt"] = ""
        file_list["shakespeare1.txt"] = ""

        #creates a dict of the files already read and converted into a string
        #so the file does not get read more then once.
        for document in file_list:
            file_list[document] = read_file(document)

        # create lock for word list
        word_lock = p.lock

        for document in p.iterate(file_list):
            word_lock.acquire()
            word_list = find_words(word_list, file_list[document])
            word_lock.release()

    end = timer()
    print("Total time: ", (end - start))
    print(word_list)


if __name__ == "__main__":
    main()
