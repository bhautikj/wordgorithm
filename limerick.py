import sources
import syllables
import rhyme

import random


# There once was a writer named Mark,
# Who encountered a punt in the dark.
# He said, "Now, by thunder,
# It's a natural wonder
# I declare this a National Park!"
#
#
# There once was a [noun1] named [nounAA]
# Who found a [noun2] in the [nounAB]
# They said, "Now, by [nounBA],
# It's a [adjective0] [nounBB]
# I declare this a [adjective1] [nounAC]!"

def genLimerickA():
  limerick = ""
  nounsA = findRhyming(sources.nouns, 3)
  nounsB = findRhyming(sources.nouns, 2)
  noun1 = syllables.getWord(sources.nouns, 2, 3)
  noun2 = syllables.getWord(sources.nouns, 2, 3)
  adjective0 = syllables.getWord(sources.adjectives, 2, 3)
  adjective1 = syllables.getWord(sources.adjectives, 2, 3)
  
  limerick  = "There was once a " + noun1 + " named " + nounsA[0] + "\n"
  limerick += "Who found a " + noun2 + " in the " + nounsA[1] + "\n"
  limerick += "They said, 'Now, by " + nounsB[0] + "\n"
  limerick += "It's a " + adjective0 + " " + nounsB[1] + "!\n"
  limerick += "I declare this a " + adjective1 + " " + nounsA[2] + "!'\n"
  return limerick


#There was a young man so benighted
#He never knew when he was slighted;
#He would go to a party
#And eat just as hearty,
#As if he'd been really invited.
def genLimerickB():
  limerick = ""
  adjectivesA = findRhyming(sources.adjectives, 3)
  nounsB = findRhyming(sources.nouns, 2)
  nounsC = findRhyming(sources.nouns, 2)
  verb1 = syllables.getWord(sources.verbs, 2, 3)
  
  limerick  = "There was a " + nounsC[0] + " so " + adjectivesA[0] + "\n"
  limerick += "Unaware he was " + adjectivesA[1] + ";\n"
  limerick += "He would go to a " + nounsB[0] + "\n"
  limerick += "And " + verb1 + " just as " + nounsB[1] + ",\n"
  limerick += "Just like a " + nounsC[1] + " " + adjectivesA[2] + ".\n"
  
  return limerick

def findRhymingCore(source, num, numSyb = 2):
  sourceNoun = syllables.getWord(source, numSyb, numSyb)
  rhymeNouns = rhyme.word_rhyme_candidates(sourceNoun)
  
  nounList = []
  nounList.append(sourceNoun)
  
  suggest = []
  for word in rhymeNouns:
    if syllables.syllables(word) == numSyb:
      if word in source:
        suggest.append(word)
  
  if len(suggest) < num:
    return []
  
  maxCount = 100
  count = 1
  for i in range(num-1):
    testWord = random.choice(suggest)
    while testWord in nounList and count < maxCount:
      testWord = random.choice(suggest)
      count += 1
    if count >= maxCount:
      return []
    nounList.append(testWord)
    
  return nounList

def findRhyming(source, num, numSyb = 2):
  nouns = findRhymingCore(source, num, numSyb)
  while nouns == []:
    nouns = findRhymingCore(source, num, numSyb)
  return nouns
        