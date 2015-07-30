

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
#------------------------------------

WORDLIST_FILENAME = "E:\Desktop\My Documents\python games\Hand game\words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# -----------------------------------

#
# Scoring a word
#
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    count=0
    if len(word)==0 : 
        return 0
    elif len(word)<n : 
        for e in word : 
            count=count+SCRABBLE_LETTER_VALUES[e]
        score=count*len(word)
    else : 
        for e in word : 
            count =count+SCRABBLE_LETTER_VALUES[e]
        score=count*len(word)+50
    return score




def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print                               # print an empty line

def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n / 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand


 # Update a hand by removing letters

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    hand1=hand.copy()
    for e in word : 
        if e in hand1.keys() :
            hand1[e]=hand1[e]-1
    return hand1



#
#Test word validity
#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    hand1=hand.copy()
    cond2=True
    if word in wordList : 
        cond1=True
    else :
        cond1=False
    for e in word : 
        if e in hand1.keys() and hand1[e]!=0 : 
            cond2=cond2 and True
            hand1[e]=hand1[e]-1
        else : 
            cond2=False
            break
    return cond1 and cond2


#
#Playing a hand
#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    count=0
    for e in hand : 
        count=count+hand[e]
    return count



def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    score=0
    hand1=hand.copy()
    while calculateHandlen(hand1)!=0 :
        get=0 
        print 'Current Hand: ',
        displayHand(hand1)
        x=str(raw_input('Enter word, or a "." to indicate that you are finished: '))
        if x=='.' : 
            break
        
            
        else : 
        
            if isValidWord(x,hand1,wordList)==False :
            
                print 'Invalid word, please try again'
                print 

            else :
                get=getWordScore(x,n)
                score=score+getWordScore(x,n)
                
                hand1=updateHand(hand1,x)
                 
                print ('"'+str(x)+'" earned '+str(get)+' points. Total: '+str(score)+' points')
               

    if x=='.' :
        print ('Goodbye! Total score: '+str(score)+' points.') 
        
    if calculateHandlen(hand1)==0 : 
        print ('Run out of letters. Total score: '+str(score)+' points.')
        
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    total=0
    word=''
    hand1=hand.copy()
    for i in wordList :
        hand1=hand.copy()
        cond2=True
        for e in i : 
            if e in hand1.keys() and hand1[e]!=0 : 
                cond2=cond2 and True
                hand1[e]=hand1[e]-1
            else : 
                cond2=False
                break
        if cond2==True :   
            score=getWordScore(i,n)

            if score>total : 

                total=score
                word=i
                
    
    if len(word)==0 : 
        return None
    return word
        
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    score=0
    hand1=hand.copy()
    while calculateHandlen(hand1)!=0 :
        get=0 
        print 'Current Hand: ',
        displayHand(hand1)
        x=compChooseWord(hand1,wordList,n)
        if x==None : 
            break
        
            
    

        else :
            get=getWordScore(x,n)
            score=score+getWordScore(x,n)
            
            hand1=updateHand(hand1,x)
                 
            print ('"'+str(x)+'" earned '+str(get)+' points. Total: '+str(score)+' points')
               

    if x==None or calculateHandlen(hand1)==0  :
        print ('Total score: '+str(score)+' points.') 

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    hand1={}
    a=str(raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: "))
    if a!='e' : 
        x=True
    else : 
        x=False
    while x==True : 
        if a=='n' : 
            hand1=dealHand(HAND_SIZE)
            z=str(raw_input('Enter u to have yourself play, c to have the computer play: '))
            while z!='u' and z!='c' : 
                print 'Invalid Command'
                z=str(raw_input('Enter u to have yourself play, c to have the computer play: '))
            if z=='u' :
                playHand(hand1,wordList, HAND_SIZE)
            elif z=='c' : 
                compPlayHand(hand1,wordList,HAND_SIZE)
        elif a=='r' : 
            if len(hand1)==0 : 
                print 'You have not played a hand yet. Please play a new hand first!'

            else :
                z=str(raw_input('Enter u to have yourself play, c to have the computer play: '))
                while z!='u' and z!='c' : 
                    print 'Invalid Command'
                    z=str(raw_input('Enter u to have yourself play, c to have the computer play: '))
                if z=='u' :
                    playHand(hand1,wordList, HAND_SIZE)
                elif z=='c' : 
                    compPlayHand(hand1,wordList,HAND_SIZE)
        elif a=='e' : 
            break
        else : 
            print 'Invalid command.'
        a=str(raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: "))
        if a!='e' : 
            x=True
        else : 
            x=False
    

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    HAND_SIZE=int(raw_input("Enter the number of characters : "))
    playGame(wordList)





