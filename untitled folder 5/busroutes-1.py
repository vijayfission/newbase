from HTMLParser import HTMLParser
from re import sub
from sys import stderr
from traceback import print_exc

class DeHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.__text = []

    def handle_data(self, data):
        text = data.strip()
        if len(text) > 0:
            text = sub('[ \t\r\n]+', ' ', text)
            self.__text.append(text + ' ')

    def handle_starttag(self, tag, attrs):
        if tag == 'td':
            self.__text.append('\n\n')
        elif tag == '':
            self.__text.append('\n')

    def handle_startendtag(self, tag, attrs):
        if tag == 'td':
            self.__text.append('\n\n')

    def text(self):
        return ''.join(self.__text).strip()


def dehtml(text):
    try:
        parser = DeHTMLParser()
        parser.feed(text)
        parser.close()
        return parser.text()
    except:
        print_exc(file=stderr)
        return text

import urllib

def main():
	for i in range(1, 27):
		u = urllib.urlopen('http://www.hyderabadbusroutes.com/index.php?service=BUSROUTE&page='+str(i))	
		k = u.read()
		file = open("text"+str(i)+".txt", 'w')
		l = (dehtml(k))
		file.write(l)
		file.close()
		print "file is written for " +str(i)

if __name__ == '__main__':
    main()