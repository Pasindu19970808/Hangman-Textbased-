from random import randint
from string import ascii_lowercase

wordlist = open('hangman.txt')       

secret_words = list()
smallest = None
biggest = None
for word0 in wordlist:
    secret_words.append(word0.strip())
    if smallest == None:
        smallest = len(word0.strip())
    elif len(word0.strip()) < smallest:
        smallest = len(word0.strip())
    if biggest == None:
        biggest = len(word0.strip())
    elif len(word0.strip()) > biggest:
        biggest = len(word0.strip())
    
amountofwords = len(secret_words)


def get_num_attempts():
    while True:
        num_attempts = input("How many attempts do you want? [1-25] ")
        try:
            num_attempts = int(num_attempts)
            if 1<= num_attempts and num_attempts<=25:
                return num_attempts
            else:
                print('{0} is not between 1 and 25'.format(num_attempts))
        except ValueError:
            print('{0} is not an integer between 1 and 25'.format(num_attempts))
        except TypeError:
            print('{0} is not an integer and is not between 1 and 25'.format(num_attempts))
            
            
def get_min_word_length():
    while True:
        min_length = input("What is the minimum word length? ")
        try:
            min_length = int(min_length)
            if smallest<= min_length and min_length<=biggest:
                return min_length
            else:
                print('{0} is not between '.format(min_length),smallest,' and ',biggest)
        except ValueError:
            print('{0} is not an integer between '.format(min_length),smallest,' and ',biggest)
            
def get_word():
    while True:
          pos = randint(0,amountofwords)
          guessword = secret_words[pos]
          if len(guessword)>= min_length:
             return guessword
             break
#produces the guessword as a list of booleans initialized as False
#for each letter as no letter has been guessed
#idxs = [letter not in ascii_lowercase for letter in guessword]
             
def get_display_word(guessword,idxs):
    if len(guessword) != len(idxs):
        raise ValueError('Word length and indices length are not the same')
    #if the letter has been guessed and is idxs[i] is true, display the letter
    #else display a *
    temp = list()
    for pos,letter in enumerate(guessword):
          if idxs[pos] is True:
              temp.append(letter)
          else:
              temp.append('*')
    displayed_word = ''.join(temp)
    return displayed_word

           
def get_next_letter(guessed_letters,num_attempts,remain_attempts,guessword):
    while True:
        nextletter = input("Input next guess letter: ")
        nextletter = str(nextletter.lower())
        if (len(nextletter) == 1) and (nextletter not in guessed_letters) and (nextletter in ascii_lowercase) and (nextletter in guessword):
                guessed_letters.append(nextletter)
                if nextletter in guessword:
                    position = [i for i,f in enumerate(guessword) if f == nextletter]
                    for val in position:
                        idxs[val] = True
                remain_attempts = remain_attempts
                print('Remaining attempts: ', remain_attempts)
                return {'ra':remain_attempts,'gl':guessed_letters,'id':idxs}
        elif (len(nextletter) == 1) and (nextletter in guessed_letters) and (nextletter in ascii_lowercase):
                print("You've guessed {0} before".format(nextletter))
                remain_attempts = remain_attempts - 1
                print('Remaining attempts: ', remain_attempts)
                return {'ra':remain_attempts,'gl':guessed_letters,'id':idxs}
        elif (len(nextletter) == 1) and (nextletter not in guessword) and (nextletter in ascii_lowercase):
                print('{0} is not a correct guess'.format(nextletter))
                remain_attempts = remain_attempts - 1
                print('Remaining attempts: ', remain_attempts)
                return {'ra':remain_attempts,'gl':guessed_letters,'id':idxs}
        elif (len(nextletter) != 1):
                print('{0} is not a single letter'.format(nextletter))  
                remain_attempts = remain_attempts - 1
                print('Remaining attempts: ', remain_attempts)
                return {'ra':remain_attempts,'gl':guessed_letters,'id':idxs}
        else:
                print('{0} is not a valid input and is not a letter'.format(nextletter))
                remain_attempts = remain_attempts - 1
                print('Remaining attempts: ', remain_attempts)
                return {'ra':remain_attempts,'gl':guessed_letters,'id':idxs}
            
#gets number of attempts           
num_attempts = get_num_attempts()
#gets the minimum length of word
min_length = get_min_word_length()
#gets the guessword
guessword = get_word()

idxs = list()
for letter in guessword:
    if letter in ascii_lowercase:
        idxs.append(False)
        
guessed_letters = list()   
remain_attempts = num_attempts       


displayed_word = get_display_word(guessword,idxs)
print(displayed_word)


while remain_attempts >= 1:
    if False not in idxs:
        print ("Well done, you win")
        break
    else:
        result = get_next_letter(guessed_letters,num_attempts,remain_attempts,guessword)
        remain_attempts = result['ra']
        guessed_letters = result['gl']
        idxs = result['id']
        displayed_word = get_display_word(guessword,idxs)
        print(displayed_word)

if False in idxs:
   print('You lost the game, the word was ',guessword)
        
    
    
     



    
    


    

