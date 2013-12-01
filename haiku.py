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


