# Algorithm based directly on: http://computationalhumor.tumblr.com/

# What do you call a [adjective1] [noun1]?
# A [adjective2] [noun2]!
#
# Where:
#
#    [adjective2] and [noun2] are homonyms.
#    [adjective1] and [adjective2] are synonyms.
#    [noun1] and [noun2] are synonyms.
    
import sys, random, nltk, urllib, string
from nltk.corpus import wordnet as wn

import sources
import words


def jokegenA():
  done = False
  
  while done == False:
    #homophone list url
    homophones = sources.homophones
    
    #adjective list wordnet
    adjs = sources.adjectives
        
    #noun list wordnet
    nouns = sources.nouns
    
    #generate nouns that have homophones that are adjectives,
    #or vice versa
    x = string.lower(random.choice(homophones.keys()))
    maxTries = 1000
    nTries = 1
    while x not in adjs and x not in nouns and nTries < maxTries:
      x = string.lower(random.choice(homophones.keys()))
      nTries += 1
      if nTries >= maxTries:
        raise Exception('Cannot find word from homophones that is a noun or an adjective')
    
    found = False
    
    if x in adjs:
      adj2 = x
      for h in homophones[adj2]:
        if h in nouns:
          noun2 = h
          noun1 = words.findNounSynonym(noun2)
          adj1 = words.findAdjectiveSynonym(adj2)
          found = True
    elif x in nouns:
      noun2 = x
      for h in homophones[noun2]:
        if h in adjs:
          adj2 = h
          noun1 = words.findNounSynonym(noun2)
          adj1 = words.findAdjectiveSynonym(adj2)
          found = True
    
    if found:
      if noun2 != noun1 and adj2 != adj1:
        x = "What do you call a " + adj1 + " " + noun1 + "?\nA " + adj2 + " " + noun2 + "!\n"  
        return x
            
if __name__ == "__main__":
    jokeGenA()