#!/usr/bin/env python

# cross-validate.py - given a file name and a list of directories, create a model for classifying similar items

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# September 5, 2017 - calling it "done"; see http://zacstewart.com/2015/04/28/document-classification-with-scikit-learn.html
# March    26, 2018 - simplified; see https://www.kaggle.com/rishabhgoel/spam-detection-using-multinomialnb
# May       6, 2019 - added stopwords


# configure
STOPWORDS = './etc/stop-words.txt'
SPLITS    = 10

# require
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model            import SGDClassifier
from sklearn.model_selection         import cross_val_score
from sklearn.model_selection         import KFold
from sklearn.naive_bayes             import MultinomialNB
from sklearn.pipeline                import Pipeline
from sklearn.svm                     import SVC
import glob
import os
import sys

# sanity check
if len( sys.argv ) < 3 :
	sys.stderr.write( 'Usage: ' + sys.argv[ 0 ] + " <naive|sgd|svm> <directory> <another directory> [<another directory> ...]\n" )
	exit()

# initialize
data        = []
labels      = []
directories = []
kfold       = KFold( n_splits=SPLITS, shuffle=True, random_state=1 )

# initialize the desired model
if sys.argv[ 1 ]   == 'naive' : model = MultinomialNB()
elif sys.argv[ 1 ] == 'sgd'   : model = SGDClassifier( max_iter=10, tol=None, random_state=1, fit_intercept=True )
elif sys.argv[ 1 ] == 'svm'   : model = SVC()
else : 
	sys.stderr.write( 'Usage: ' + sys.argv[ 0 ] + " <naive|sgd|svm> <directory> <another directory> [<another directory> ...]\n" )
	exit()

# get the directories to process
for i in range( 2, len( sys.argv ) ) : directories.append( sys.argv[ i ] )

# process each given directory
for directory in directories :

	# find all the text files and get the directory's name
	files = glob.glob( directory + "/*.txt" )
	label = os.path.basename( directory )
	
	# process each file
	for file in files :
		
		# open the file, read it, and update the lists of texts and labels
		with open( file, 'r' ) as handle :
			data.append( handle.read() )
			labels.append( label )

# read stop words
with open( STOPWORDS ) as f: stopwords = f.readlines()
stopwords = [ stopword.strip() for stopword in stopwords ] 

# get frequency of features (counts)
countVectorizer = CountVectorizer( ngram_range=(1, 2), stop_words=stopwords )
data            = countVectorizer.fit_transform( data )

# use TFIDF to accomodate for varying lengths of documents
tfidfTransformer = TfidfTransformer( use_idf=False )
data             = tfidfTransformer.fit_transform( data )

# cross-validate 
scores = cross_val_score( model, data, labels, cv=kfold )

# output; done
print( scores )
print( scores.mean() )

