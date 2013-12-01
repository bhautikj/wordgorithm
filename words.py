import nltk
from nltk.corpus import wordnet as wn

import string, random

def findNounSynonym(word):
  return findSynonymCore(word, ".n.01")

def findAdjectiveSynonym(word):
  return findSynonymCore(word, ".a.01")

def findSynonymCore(word, wordnetPattern):
  found = False
  cand = ""
  
  maxTries = 1000
  nTries = 1
  
  while found == False and nTries < maxTries:
    try: 
      words = wn.synset(word + wordnetPattern).lemma_names
      cand = string.lower(random.choice(words))
      found = True
    except nltk.corpus.reader.wordnet.WordNetError:
      break
      
    nTries += 1
    if nTries >= maxTries:
      raise Exception('Cannot find syllable')

  return cand