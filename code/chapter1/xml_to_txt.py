from xml.sax.handler import ContentHandler
import xml.sax
import sys
from glob import glob

def transform(xml_file):
    class textHandler(ContentHandler):
        def characters(self, ch):
            sys.stdout.write(ch.encode("ascii","ignore"))
            
    parser = xml.sax.make_parser()
    handler = textHandler()
    parser.setContentHandler(handler)
    parser.parse(xml_file)

if __name__ == '__main__':
    chapters = [chapter for chapter in glob(sys.argv[1]+"*.xml") if "main" in chapter]
    chapters = sorted(chapters)
    tmp10,tmp11,tmp12 = chapters[2],chapters[3],chapters[4]
    chapters = chapters[:2] + chapters[5:]
    chapters.append(tmp10)
    chapters.append(tmp11)
    chapters.append(tmp12)
    
    for chapter in chapters:
        transform(chapter)
