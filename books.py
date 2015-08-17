from __future__ import division
import glob
import string
from collections import Counter

#------------------
"""
Title:
Author:
*** START OF THIS PROJECT GUTENBERG EBOOK 

*** END OF THIS PROJECT GUTENBERG EBOOK
f = open('workfile', 'w')


for line in f:
        print line,


"""
class book(object):
    def __init__(self, title, author, words):
        self.title = title
        self.author = author
        self.words = words


book_list = list()


files = glob.glob("*.txt")

for filename in files:

    book_file = open(filename, 'r')
    book_contents = False
    book_text = ""
    title = ""
    author = ""

    for l in book_file:     

        if "Title:" in l:
            title = l.lstrip("Title: ")
            title = title.rstrip("\r\n")
            
        elif "Author:" in l:
            author = l.lstrip("Author: ")
            author = author.rstrip("\r\n")
            
        elif "*** START OF THIS PROJECT GUTENBERG EBOOK" in l:
            book_contents = True
        elif "*** END OF THIS PROJECT GUTENBERG EBOOK" in l:
            book_contents = False
            
        if book_contents:
            if "*** START OF THIS PROJECT GUTENBERG EBOOK" not in l and "*** END OF THIS PROJECT GUTENBERG EBOOK" not in l:
                book_text = book_text + " " + l
     



    book_text = book_text.translate(string.maketrans("",""), '\n\r')
    book_text = book_text.translate(string.maketrans("",""), string.punctuation)     
    
    book_text = book_text.split(' ')
    words = Counter(book_text)
    # words.most_common(3) gives the three most common words
    book_list.append(book(title,author,words))
     
     
         
        
        
            
           





