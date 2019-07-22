# Modeling C. neoformas
Given a set of PDF files, create a classification model for determining whether or not they allude to C. neoformas.

More specifically, given two directories (./pdf/All_pos and ./pdf/All_neg) filed with an arbitrary number of PDF files separated into positively and negatively identified articles for C. neoformas, this system will:

   * convert the PDF files into plain text (./bin/pdf2txt.sh)
   * move the plain text files to the ./models directory, accordingly (./bin/divide.sh)
   * normalize the plain text (./bin/clean.sh)
   * create a model (./bin/train.sh)
   
The process outlined above can be run with "one script to rule them all" -- ./bin/build.sh.

While a person may want rush to ./bin/build.sh right away, it might be better to first test which classification algorithm it use (./bin/cross-validate.py), and then test which parameters to use for a selected algorithm (./bin/parameterize.py). To the best of my ability, this has already been done, but testing scripts are still here because software is never done.

Once the a model has been created, one can classify other plain text files with the classifier (./bin/classify.py), but at first glance it does not work.

---
Eric Lease Morgan &lt;emorgan@nd.edu&gt;  
July 23, 2019

