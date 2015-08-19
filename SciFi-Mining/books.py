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
    def __init__(self, title, author, filename,words):
        self.title = title
        self.author = author
        self.filename = filename
        self.words = words


book_list = list() #list containing book objects
meta_data = "" #file to output author list

files = glob.glob("books/*.txt")

for filename in files:
    
    book_file = open(filename, 'r')
    book_contents = False
    book_text = ""
    title = ""
    author = ""

    for l in book_file:     

        if author == "" and title == "" and "The Project Gutenberg EBook" in l and " by " in l:
            temp_line = l.lstrip("The Project Gutenberg EBook ")
            temp_line = temp_line.split(" by ")
           
            title = temp_line[0]
            author = temp_line[1].rstrip("\r\n")
    
            
        elif "Title:" in l:
            title = l.lstrip("Title:")
            title = " ".join(title.rstrip("\r\n"))
            
        elif "Author:" in l:
            author = l.lstrip("Author:")
            author = author.rstrip("\r\n")
            
        elif "START" in l and "GUTENBERG" in l or "THE SMALL PRINT!" in l:
            book_contents = True
        elif "END" in l and "GUTENBERG" in l:
            book_contents = False
            
        if book_contents:
            if "*** START OF THIS PROJECT GUTENBERG EBOOK" not in l and "*** END OF THIS PROJECT GUTENBERG EBOOK" not in l and "THE SMALL PRINT!" not in l:
                book_text = book_text + " " + l
     



    book_text = book_text.translate(string.maketrans("",""), '\n\r')
    book_text = book_text.translate(string.maketrans("",""), string.punctuation)     
    
    book_text = book_text.split(' ')
    words = Counter(book_text)
    # words.most_common(3) gives the three most common words
    book_list.append(book(title,author,filename,words))
    book_file.close()
    
book_list = sorted(book_list, key=lambda x: x.author)
    
    
meta_data = open("meta.txt","w")
meta_data.write("Wordcount \t filename \t author \t title \n")
    
    
    
    
for b in book_list:
    #she:he ratio
    gender = b.words['she']/b.words['he']
        
        
    b.words.most_common()
        
    line = str(str(len(b.words))+"\t"+b.filename+"\t"+b.author+"\t"+b.title+"\t"+str(gender)+"\n")
    meta_data.write(line)

meta_data.close()
    
    
    
    
     
         
        
        
            
           





