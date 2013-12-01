#
# The MIT License (MIT)
#
# Copyright (c) 2013 Bhautik J Joshi bjoshi@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

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