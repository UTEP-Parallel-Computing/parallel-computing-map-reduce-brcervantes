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
        print(word_list)
    return word_list


def main():
    '''
    parallelize the word search among 8 different documents.
    '''
    #parallelize this part
    with mp.Parallel(3) as p:
        #word_list = mp.shared.dict()
        file_list = mp.shared.dict()

        word_list = {"hate"   :0,
                 "love"   :0,
                 "death"  :0,
                 "night"  :0,
                 "sleep"  :0,
                 "time"   :0,
                 "henry"  :0,
                 "hamlet" :0,
                 "you"    :0,
                 "my"     :0,
                 "blood"  :0,
                 "poison" :0,
                 "macbeth":0,
                 "king"   :0,
                 "heart"  :0,
                 "honest" :0}

        file_list = {"shakespeare1.txt":"",
                 "shakespeare2.txt":"",
                 "shakespeare3.txt":"",
                 "shakespeare4.txt":"",
                 "shakespeare5.txt":"",
                 "shakespeare6.txt":"",
                 "shakespeare7.txt":"",
                 "shakespeare8.txt":""}

        #creates a dict of the files already read and converted into a string
        #so the file does not get read more then once.
        for document in file_list:
            file_list[document] = read_file(document)

        start = timer()

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
