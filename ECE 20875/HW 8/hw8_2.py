import numpy as np
from helper import remove_punc
from hw8_1 import *
import nltk

nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
from nltk.corpus import stopwords


# Clean and prepare the contents of a document
def read_and_clean_doc(doc):
    
    '''
    Arguments:
        doc: string, the name of the file to be read.
    Returns:
        all_no_stop: string, a string of all the words in the file, with stopwords removed.
    Notes: Do not append any directory names to doc -- assume we will give you a string representing a file name that will open correctly
    '''     
    
    # 1. Open document, read text into *single* string
    with open(doc, "r") as f:
        allStr = f.read()

    # 2. Filter out punctuation from list of words (use remove_punc)
    all_rm_punc = remove_punc(allStr)

    # 3. Make the words lower case
    all_lower = all_rm_punc.lower()

    # 4. Filter out stopwords
    tok_low = all_lower.split(" ")
    filt_tok = [tok for tok in tok_low if tok not in stopwords.words("english")]
    all_no_stop = "".join(filt_tok)

    return all_no_stop


# Builds a doc-word matrix
def build_doc_word_matrix(doclist, n):
    
    '''
    Arguments:
        doclist: list of strings, each string is the name of a file to be read.
        n: int, the length of each n-gram
    Returns:
        docword: 2-dimensional numpy array, the doc-word matrix for the cleaned documents,
            with one row per document and one column per ngram (there should be as many columns as unique words that appear across *all* documents. 
            Also, Before constructing the doc-word matrix, you should sort the list of ngrams output and construct the doc-word matrix based on the sorted list
        ngramlist: list of strings, the list of ngrams that correspond to the columns in docword
    '''
    # 1. Create the cleaned string for each doc (use read_and_clean_doc)
    doc_clean = []
    for count in doclist:
        doc_clean.append(read_and_clean_doc(count))
    # 2. Create and use ngram lists to build the doc word matrix
    ngramlist = []
    for count in doc_clean:
        ngram = get_ngrams(count, n)
        for i in ngram:
            if i not in ngramlist:
                ngramlist.append(i)

    ngramlist = sorted(ngramlist)   #Sort
    docword = np.zeros((len(doclist), len(ngramlist)))  #Create the 2-dimensional numpy array
    for element in range(len(doclist)):
        doc = doc_clean[element]
        ngrams = get_ngrams(doc, n)
        for counter in ngrams:
            index = ngramlist.index(counter)
            docword[element][index] += 1

    return docword, ngramlist


# Builds a term-frequency matrix
def build_tf_matrix(docword):
    
    '''
    Arguments:
        docword: 2-dimensional numpy array, the doc-word matrix for the cleaned documents, as returned by build_doc_word_matrix
    Returns:
        tf: 2-dimensional numpy array with the same shape as docword, the term-frequency matrix for the cleaned documents  
    HINTs: You may find np.newaxis helpful
    '''

    # fill in
    sum_docword = np.sum(docword, axis = 1) #Find sum of each row
    tf = docword / sum_docword[:, np.newaxis]   #Find tf

    return tf


# Builds an inverse document frequency matrix
def build_idf_matrix(docword):
    
    '''
    Arguments:
        docword: 2-dimensional numpy array, the doc-word matrix for the cleaned documents, as returned by build_doc_word_matrix
    Returns:
        idf: 1-dimensional numpy array, the inverse document frequency matrix for the cleaned documents.
             (should be a 1xW numpy array where W is the number of ngrams in the doc word matrix).
             Don't forget the log factor!
             
    '''
    # fill in
    number = docword.shape[0]   #Make zero arrays
    idf = np.zeros((1, docword.shape[1]))   
    for count in range(docword.shape[1]):   #For each ngram, update array and doc tf
        n_t = np.sum(docword[:, count] > 0)
        idf[0][count] = np.log10(number / n_t)  #Take the base 10 log of N / nt

    return idf


#   Builds a tf-idf matrix given a doc word matrix
def build_tfidf_matrix(docword):
    
    '''
    Arguments:
        docword: 2-dimensional numpy array, the doc-word matrix for the cleaned documents, as returned by build_doc_word_matrix
    Returns:
        tfidf: 2-dimensional numpy array with the same shape as docword, the tf-idf matrix for the cleaned documents
    '''

    # fill in
    tfidf = build_tf_matrix(docword) * build_idf_matrix(docword)    #Create tf-idf 2-dimensional numpy array
    return tfidf


#   Find the three most distinctive ngrams, according to TFIDF, in each document
def find_distinctive_ngrams(docword, ngramlist, doclist):
    
    '''
    Arguments:
        docword: 2-dimensional numpy array, the doc-word matrix for the cleaned documents, as returned by build_doc_word_matrix
        ngramlist: list of strings, the list of ngrams that correspond to the columns in docword
        doclist: list of strings, each string is the name of a file to be read.
    Returns:
        distinctive_words: dictionary, mapping each document name from doclist to an ordered list of the three most unique ngrams in each document
    '''
    distinctive_words = {}
    # fill in
    # you might find numpy.argsort helpful for solving this problem:
    # https://docs.scipy.org/doc/numpy/reference/generated/numpy.argsort.html
    # HINT: the smallest three of -docword correspond to largest 3 of docword
    tfidf = build_tfidf_matrix(docword) #Build tfidf matrix
    for count in range (len(doclist)):  #Run through documents and find distinctive ngrams
        doc_count = doclist[count]
        tfidf_count = tfidf[count]
        indices = np.argsort(-tfidf_count)[:3]  #Find three largest tfidf values
        ngrams = [ngramlist[element] for element in indices]    #Find correspongind ngrams
        distinctive_words[doc_count] = ngrams   #Add those ngrams to dictionary

    return distinctive_words


if __name__ == "__main__":
    from os import listdir
    from os.path import isfile, join, splitext

    ### Test Cases ###
    directory = "lecs"
    path1 = join(directory, "1_vidText.txt")
    path2 = join(directory, "2_vidText.txt")

    print("*** Testing build_doc_word_matrix ***")
    doclist = [path1, path2]
    docword, wordlist = build_doc_word_matrix(doclist, 4)
    print(docword.shape)
    print(len(wordlist))
    print(docword[0][0:10])
    print(wordlist[0:10])
    print(docword[1][0:10])
    print("\n*** Testing build_tf_matrix ***")
    tf = build_tf_matrix(docword)
    print(tf[0][0:10])
    print(tf[1][0:10])
    print(tf.sum(axis=1))
    print("\n*** Testing build_idf_matrix ***")
    idf = build_idf_matrix(docword)
    print(idf[0][0:10])
    print("\n*** Testing build_tfidf_matrix ***")
    tfidf = build_tfidf_matrix(docword)
    print(tfidf.shape)
    print(tfidf[0][0:10])
    print(tfidf[1][0:10])
    print("\n*** Testing find_distinctive_words ***")
    print(find_distinctive_ngrams(docword, wordlist, doclist))
