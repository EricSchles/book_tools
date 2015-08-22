# cbir

more or less stolen from http://www.pyimagesearch.com/2014/12/01/complete-guide-building-image-search-engine-python-opencv/

##How to use:

`python index_search.py -d [directory of pictures] -i [name of file] #create an index`

`python index_search.py -i [name of index file] -q [path to query picture] -r [path to picture directory] #search for a picture`

A specific example:

`python index_search.py -d pic_db/ -i index.csv`

`python index_search.py -i index.csv -q person.jpg -r pic_db/`

