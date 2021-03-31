import urllib.request
import os
from urllib import request, parse

def read_file():
    path = str('/Users/vivian.dsouza/Downloads/py.txt')
    var = os.path.dirname(path) 
    #var = os.path.isdir(path) 
    quotes = open(path)
    file = quotes.read()
    print(var)
    quotes.close()
    check_profanity(file)

def check_profanity(self):
    url = "http://www.wdylike.appspot.com/?q="
    url = url + parse.quote(self)
    req = request.urlopen(url)
    answer = req.read()
    #params = urlencode({'q': text_to_read})
    #connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?" + params)
    #connection = urllib.request.urlopen('http://www.wdylike.appspot.com/?q=QUERY' + text_to_check)
    #output = connection.read()
    print(answer)
    req.close

read_file()    



