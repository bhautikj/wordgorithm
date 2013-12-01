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