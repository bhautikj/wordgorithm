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

# derived directly from: https://github.com/classam/rhymenocerous/blob/master/rhyme.py
import copy
import nltk
from collections import defaultdict
import random
import cPickle
import gzip
import os

import syllables
import sources


def rhyme_quality( p1, p2 ):
    """ Determine a numerical quality of the rhyme between two pronunciation lists. 
    
        >>> rhyme_quality( ["A", "B", "C"], ["A", "B"] )
        0
        >>> rhyme_quality( ["A", "B", "C"], ["B", "C"] )
        2
        >>> rhyme_quality( ["A", "B"], ["A", "B"] )
        0
        >>> rhyme_quality( ["B", "B", "C", "D"], ["A", "B", "C", "D"] )
        #3
    """
    p1 = copy.deepcopy(p1)
    p2 = copy.deepcopy(p2)
    p1.reverse()
    p2.reverse()
    if p1 == p2:
        # G-Spot rocks the G-Spot
        return 0
    quality = 0
    for i, p_chunk in enumerate(p1):
        try:
            if p_chunk == p2[i]:
                quality += 1
            if p_chunk != p2[i]:
                break
        except IndexError:
            break
    return quality
    

def word_rhyme_candidates( word ):
    """
        Produce a list of potential rhyme candidates for a word
        >>> print word_rhyme_candidates("battalion")[:5]
        ['stallion', 'italian', 'scallion', 'medallion', 'mccallion']
    """
    candidates = []
    try:
        pronunciations = sources.pronunciation_dictionary[word]
    except KeyError:
        return []
    if pronunciations == []:
        return []
    for pronunciation in pronunciations:
        for rhyme_word, rhyme_pronunciation in sources.rhyme_entries:
            quality = rhyme_quality( pronunciation, rhyme_pronunciation )
            if quality > 0:
                candidates.append( (quality, rhyme_word) )
    candidates.sort()
    candidates.reverse()
    best_quality = candidates[0][0]
    worst_allowable_quality = best_quality - 1
    candidates = [ candidate for q, candidate in candidates if q >= worst_allowable_quality ]

    return candidates
