from sklearn.feature_extraction.text import TfidfVectorizer

def TfIdf(document_list):
    vectorizer = TfidfVectorizer(stop_words="english")
    X = vectorizer.fit_transform(document_list)
    return vectorizer,X

corpus = [
    "Hello there, my name is Eric, will you by my friend?",
    "Hi there, I'm olaf, and I like warm hugs",
    "Oh hey there, my name is billop, and my mother didnt want to name me bill or phillip, so she named me billop",
    "Hello, my name is the rock, and can you smell what I'm cooking?  It's a pie, for your face"]

vectorizer,result = TfIdf(corpus)
print dict(zip(vectorizer.get_feature_names(),vectorizer.idf_))
