pyg = 'ay'
#here is where we take the users input
original = raw_input('Enter a word:')
word = original.lower ()
first = word [0]
#this is where we begin construction the Pig Latin translation 
new_word = word + first + pyg 
#we do this to ensure that the first letter is not appearing twice
new_word = new_word[1:len(new_word)]
if len(original) > 0 and original.isalpha():
  print "the Pig Latin translation of that word is: " + new_word
else:
  print 'empty'
