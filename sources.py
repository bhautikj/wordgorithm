import nltk
from nltk.corpus import wordnet as wn

import sys, os, urllib, string, cPickle as pickle


if os.path.exists("homophones.pickle"):
  f = open("homophones.pickle", "rb")
  homophones = pickle.load(f)
  f.close()
else:  
  #homophone list url
  urlH = "http://cdl.best.vwh.net/NeXT/homophones.html"
  rawHomoPh = urllib.urlopen(urlH).read()
  homophonesList = map(lambda x: x.split()[1:],rawHomoPh.split("<p>")[1].split("<br>"))
  homophones = dict([(x[0],x[1:]) for x in homophonesList if len(x) > 1])
  f = open("homophones.pickle", "wb")
  pickle.dump(homophones, f)
  f.close()

        
rhyme_entries = nltk.corpus.cmudict.entries()
pronunciation_dictionary = nltk.corpus.cmudict.dict()

#adjective list wordnet
adjectives = []
for synset in list(wn.all_synsets('a')):
  adjSyn = synset.lemma_names
  for asy in adjSyn:
    adjectives.append(asy.lower())
    
#noun list wordnet
nouns = []
for synset in list(wn.all_synsets('n')):
  nounSyn = synset.lemma_names
  for ns in nounSyn:
    nouns.append(ns.lower())
    

#adverb list wordnet    
adverbs = []
for synset in list(wn.all_synsets('r')):
  adverbSyn = synset.lemma_names
  for vs in adverbSyn:
    adverbs.append(vs.lower())

#verb list wordnet    
verbs = []
for synset in list(wn.all_synsets('v')):
  verbSyn = synset.lemma_names
  for vs in verbSyn:
    verbs.append(vs.lower())