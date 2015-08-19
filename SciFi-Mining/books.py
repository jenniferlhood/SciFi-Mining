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
            title = "".join(title.rstrip("\r\n"))
            
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
    
    
#find the set of most common words by taking the intersection of the 200 most common words in all books in library
all_common = set(i[0] for i in book_list[0].words.most_common(1000))
  
 
for b in book_list:
    #she:he ratio
    if b.words['she']>0:
        gender = b.words['he']/b.words['she']
    else:
        gender = 0   
        
    b_common = set(i[0] for i in b.words.most_common(1000)) #top
    
    all_common = all_common & b_common
        
    line = str(str(len(b.words))+"\t"+b.filename+"\t"+b.author+"\t"+b.title+"\t"+str(gender)+"\n")
    meta_data.write(line)


meta_data.close()
print all_common    


a = set(['', 'and', 'by', 'that', 'this', 'of', 'it', 'long', 'the', 'to', 'as', 'other', 'A', 'a', 'in', 'be', 'on', 'or', 'if'])

b = set(['', 'replied', 'all', 'just', 'less', 'being', 'indeed', 'over', 'What', 'years', 'four', 'course', 'through', 'still', 'yet', 'seemed', 'No', 'had', 'should', 'better', 'to', 'only', 'those', 'under', 'he', 'might', 'On', 'them', 'his', 'return', 'means', 'very', 'possible', 'soon', 'cannot', 'every', 'know', 'they', 'half', 'not', 'world', 'now', 'him', 'nor', 'like', 'did', 'these', 'she', 'each', 'small', 'become', 'where', 'right', 'For', 'there', 'some', 'back', 'see', 'been', 'are', 'our', 'out', 'even', 'what', 'said', 'for', 'away', 'find', 'case', 'enough', 'then', 'between', 'new', 'before', 'ever', 'He', 'be', 'we', 'who', 'And', 'This', 'never', 'here', 'quite', 'let', 'found', 'come', 'by', 'on', 'great', 'last', 'her', 'of', 'could', 'days', 'against', 'times', 'place', 'or', 'first', 'own', 'point', 'into', 'There', 'one', 'down', 'done', 'But', 'another', 'open', 'your', 'once', 'little', 'long', 'from', 'would', 'few', 'give', 'question', 'three', 'least', 'their', 'much', 'too', 'way', 'time', 'themselves', 'hundred', 'was', 'more', 'life', 'himself', 'form', 'that', 'about', 'but', 'part', 'with', 'than', 'present', 'must', 'me', 'has', 'word', 'this', 'when', 'up', 'us', 'will', 'matter', 'while', 'can', 'were', 'my', 'and', 'do', 'almost', 'is', 'am', 'it', 'an', 'say', 'at', 'have', 'in', 'seen', 'You', 'made', 'any', 'as', 'if', 'again', 'no', 'make', 'able', 'same', 'how', 'other', 'take', 'which', 'you', 'many', 'day', 'either', 'A', 'may', 'shall', 'I', 'after', 'upon', 'most', 'moment', 'two', 'men', 'nothing', 'such', 'The', 'a', 'All', 'off', 'light', 'well', 'It', 'think', 'thought', 'As', 'without', 'so', 'At', 'In', 'far', 'the', 'left', 'its', 'order', 'came', 'If'])
    
    
     
    
        
        
            
           





