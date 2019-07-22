#!/usr/bin/env python

# parameterize.py - given many preconfigurations, determine what hyperparameters might be best; edit iteratively

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# July 23, 2019 - first investigations; edit based on output of cross-validate.py


# configure
STOPWORDS ='./etc/stop-words.txt'
SPLITS    = 10
JOBS      = 8

# require
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model            import SGDClassifier
from sklearn.model_selection         import GridSearchCV
from sklearn.model_selection         import KFold
from sklearn.naive_bayes             import MultinomialNB
from sklearn.pipeline                import Pipeline
import glob
import os
import sys

# sanity check
if len( sys.argv ) < 3 :
	sys.stderr.write( 'Usage: ' + sys.argv[ 0 ] + " <directory> <another directory> [<another directory> ...]\n" )
	quit()

# initialize
data        = []
labels      = []
directories = []
kfolds      = KFold( n_splits=SPLITS, shuffle=True, random_state=1 )

# get the directories to process
for i in range( 1, len( sys.argv ) ) : directories.append( sys.argv[ i ] )

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

# create a pipeline and enumerate hyperparameters
pipeline   = Pipeline( [ ( 'vectorizer', CountVectorizer( stop_words=stopwords ) ), ( 'transformer', TfidfTransformer( use_idf=False ) ), ( 'classifier', SGDClassifier( max_iter=10, tol=None, random_state=1 ) ) ] )
parameters = { 
               'classifier__fit_intercept' : [ True, False ], 
             }

# initialize the grid and do the work
grid = GridSearchCV( pipeline, parameters, cv=kfolds, n_jobs=JOBS )
grid = grid.fit( data, labels )

# output results and done
print( "%s: %r" % ( "Best score", grid.best_score_ ) )
print( "Best parameters:" )
for parameter in sorted( parameters.keys() ) : print( "  %s -> %r" % ( parameter, grid.best_params_[ parameter ] ) )
exit()
