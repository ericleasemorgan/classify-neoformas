#!/usr/bin/env python

# train.py - given a file name and a list of directories, create a model for classifying similar items

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# September 5, 2017 - calling it "done"; see http://zacstewart.com/2015/04/28/document-classification-with-scikit-learn.html
# March    26, 2018 - simplified; see https://www.kaggle.com/rishabhgoel/spam-detection-using-multinomialnb
# May       6, 2019 - added stopwords
# July     23, 2019 - added Kfold, TFIDF, and started using SGD; consider editing based on ./bin/parameterize.py


# configure
MAXIMUM   = 350
STOPWORDS ='./etc/stop-words.txt'

# require
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection         import train_test_split
from sklearn.model_selection         import KFold
from sklearn.linear_model            import SGDClassifier
import glob
import os
import pickle
import sys

# sanity check
if len( sys.argv ) < 4 :
	sys.stderr.write( 'Usage: ' + sys.argv[ 0 ] + " <model> <directory> <another directory> [<another directory> ...]\n" )
	quit()

# get the desired name of the output file
model = sys.argv[ 1 ]

# initialize the data and its associated labels
data        = []
labels      = []
directories = []

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

# divide the data/labels into training and testing sets
data_train, data_test, labels_train, labels_test = train_test_split( data, labels )

# read stop words
with open( STOPWORDS ) as f: stopwords = f.readlines()
stopwords = [ stopword.strip() for stopword in stopwords ] 

# vectorize the training data
vectorizer = CountVectorizer( ngram_range=(1, 2), stop_words=stopwords )
data_train = vectorizer.fit_transform( data_train )

# use TFIDF to accomodate for varying lengths of documents
tfidfTransformer = TfidfTransformer( use_idf=False )
data_train       = tfidfTransformer.fit_transform( data_train )

# model the training data and associated labels
classifier = SGDClassifier( max_iter=10, tol=None, random_state=1, fit_intercept=True )
classifier.fit( data_train, labels_train )

# vectorize the test set and generate classifications
data_test       = vectorizer.transform( data_test )
data_test       = tfidfTransformer.fit_transform( data_test )
classifications = classifier.predict( data_test )

# calculate and output accuracy
count = 0
for i in range( len( classifications ) ) :
    if classifications[ i ] == labels_test[ i ] : count += 1
print ( "  Accuracy: %s%% \n" % ( int( ( count * 1.0 ) / len( classifications ) * 100 ) ) )

# extract features and associate them with their coefficients
features    = vectorizer.get_feature_names()
coeficients = sorted( zip( classifier.coef_[ 0 ], features ) )

# get the most significant features
features = coeficients[ : -( MAXIMUM + 1 ) : -1 ]
print( "  Most significant features:" )
words = []
for ( score, feature ) in features : words.append( feature )
print ('; '.join( words ) )
print ()

# save and quit
with open( model, 'wb' ) as handle : pickle.dump( ( vectorizer, classifier ), handle )
quit()


