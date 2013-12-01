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