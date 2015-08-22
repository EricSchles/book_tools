from sklearn.feature_extraction.text import TfidfVectorizer
import jellyfish
import distance

def TfIdf(document_list):
    vectorizer = TfidfVectorizer(stop_words="english")
    X = vectorizer.fit_transform(document_list)
    return dict(zip(vectorizer.get_feature_names(),vectorizer.idf_))

def ngram(sentence,n):
    input_list = [elem for elem in sentence.split(" ") if elem != '']
    return zip(*[input_list[i:] for i in xrange(n)])

def similarity_analysis(doc_one,doc_two):
    ngrams_one = [ngram(doc_one,elem) for elem in xrange(1,4)]
    ngrams_two = [ngram(doc_two,elem) for elem in xrange(1,4)]

    #longer body of text should be looped through
    if len(ngrams_one) < len(ngrams_two):
        ngrams_one,ngrams_two = ngrams_two, ngrams_one
    word_choice_count = 0 
    phrase_choice_count = 0
    for elem in ngrams_one[0]:
        if elem in ngrams_two[0]:
            word_choice_count += 1
    word_choice_similarity = float(word_choice_count)/len(ngrams_one[0])

    phrases_one = ngrams_one[1] + ngrams_one[2]
    phrases_two = ngrams_two[1] + ngrams_two[2]
    for elem in phrases_one:
        if elem in phrases_two:
            phrase_choice_count += 1
    phrase_choice_similarity = float(phrase_choice_count)/len(phrases_one)
    return word_choice_similarity, phrase_choice_similarity

with open("book.txt","r") as f:
    book = f.read()
with open("unsorted_book.txt","r") as f:
    unsorted_book = f.read()

#print similarity_analysis(unsorted_book,book)
unsorted_result = TfIdf([unsorted_book])
regular_result = TfIdf([book])

for i in unsorted_result:
    if unsorted_result[i] < 1.0:
        print i
for j in regular_result:
    if regular_result[i] < 1.0:
        print i
