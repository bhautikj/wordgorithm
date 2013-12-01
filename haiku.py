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

import sources
import syllables
import rhyme


# form: 5,7,5
# verb0  noun0 - 
# noun1 verb1 adverb1 
# adj0 noun3 
def genHaikuA():
  haiku = ""
   
  noun0   = syllables.getWord(sources.nouns, 2, 2)
  verb0   = syllables.getWord(sources.verbs, 3, 3)
  noun1   = syllables.getWord(sources.nouns, 2, 2)
  verb1   = syllables.getWord(sources.verbs, 2, 2)
  adverb1 = syllables.getWord(sources.adverbs, 3, 3)
  noun3   = syllables.getWord(sources.nouns, 3, 3)
  adj0    = syllables.getWord(sources.adjectives, 2, 2)
  
  
  haiku = verb0 + " " + noun0 + " -\n" + noun1 + " " + verb1 + " " + adverb1 + "\n" + adj0 + " " + noun3
  
  return haiku


