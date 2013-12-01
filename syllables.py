# derived directly from: https://github.com/classam/rhymenocerous/blob/master/syllables.py

import nltk
from collections import defaultdict
import random

import sources

syllable_guide = defaultdict( lambda: 1 )
for word, pronunciations in sources.rhyme_entries:
    syllable_guide[word] = len([x for x in pronunciations if x[-1].isdigit() ]) 

def syllables( word ):
    """
        >>> print syllables( "I" )
        1
        >>> print syllables( "battalion" )
        3
    """
    return syllable_guide[word.lower()]

def sentence_syllables( sentence ):
    """
        >>> print sentence_syllables( "I am a battalion" )
        7
    """
    tokens = nltk.word_tokenize(sentence) 
    return sum( [ syllables(word) for word in tokens ] )


def matchWord(word, minSyllables, maxSyllables):
  nsyb = syllables(word)

  if nsyb >= minSyllables and nsyb <= maxSyllables:
    return True
  else:
    return False
    
def getWord(source, minSyllables = 0, maxSyllables = 100):
  maxTries = 1000
  nTries = 1
  testWord = random.choice(source)
  while matchWord(testWord, minSyllables, maxSyllables) == False and nTries < maxTries:
    testWord = random.choice(source)
    nTries += 1
  
  if nTries >= maxTries:
    raise Exception('Cannot find word of requested length')
  return testWord