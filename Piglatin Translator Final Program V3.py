#Piglatin translator
#Created by Jack Carmichael
#carmichaeljr@s.dcsdk12.org
#Dont like how the y_words dictionary is passed around so much!!!

from time import sleep
from random import randint

#Print load screen function
#Version 1
#9/15/15
#prints the load screen
def print_load_screen():
    print("\t\t<--PigLatin Translator-->")
    print("\t\t\tLoading...")
    print("\t      ...",end="")
    #prints the loading bar
    for x in range(9):
        print("...",end="")
        sleep(0.3)


#Main state machine function
#Version 2
#9/27/15
#the main state machine for it all, y_words lives here
def user_entry(secondary_language):
    #predetermined variables
    y_words={}
    original_text=""
    translated_text=""
    conversation=""
    #The loop that waits for a user entry
    user_entry_loop=True
    while user_entry_loop:
        #prints the main GUI
        print("\n*",end="")
        print("*"*59)
        print("___________________Translator________________")
        print("\t0-Quit Program\n\t1-Help Menu\n\t2-See Conversation\n\t3-Settings\n\t...or just type in text you want to translate")
        #prints the original and translated text if there is any, undeneath the GUI
        if len(original_text)!=0:
            print("\nO-->",original_text,"\nT-->",translated_text,"\n")
        original=input("Type the # from the menu or the text to be translated and press enter.\n-->")
        #quits the main loop if user anters 0
        if original=="0":
            return False
            user_entry_loop=False
        #prints the help menu if user enters 1
        elif original=="1":
            print_help()
        #prints the conversation if there has been any
        elif original=="2":
            print_conversation(conversation)
        elif original=="3":
            y_words, secondary_language=settings(y_words, secondary_language)
        #translates the text if none of the above is true
        elif len(original)!=0 and not_alpha(original)!=True:
            original_text, translated_text,y_words=translate_text(original,y_words, secondary_language)
            #adds the text to the conversation string
            conversation+="\nO-->"
            conversation+=original_text
            conversation+="\nT-->"
            conversation+=translated_text
            conversation+="\n"
            conversation+="*"*30
        #if nothing is true, it alerts the user to its confusion
        else:
            print(".?!."*20)
            print("Sorry the computer did not understand the last entry.")


#Help Menu Function
#Version 1
#9/15/15
#brings up the help menu
def print_help():
    help_loop=True
    while help_loop:
        #prints the main GUI for the help menu
        print("*"*60)
        print("____________________Help____________________")
        print("\t0-Go back to translator\n\t1-How to use this translator\n\t2-How to speak piglatin")
        user_selection=input("Select a catagory by typing it's # and pressing enter-->")
        #exits the help menu if 0 is entered
        if user_selection=="0":
            help_loop=False
        #prints how to use this translator if 1 entered
        elif user_selection=="1":
            print("\n"	)
            print("*"*60)
            print("__________How to use this Translator__________")
            print('~When the computer tells you to enter in your text,'+
                  'type\t\n     your text, it can be either in english or piglatin.'+
                  '\n~Press enter when you are done.\n~The computer will figure'+
                  'out if the text is in english \n    or piglat in and it will translate it accordingly')
            input("Press enter to continue-->")
        #prints how to speak piglatin if user enters 2
        elif user_selection=="2":
            print("\n")
            print("*"*60)
            print("____________How to speak PigLatin______________")
            print('~PigLatin is like a jumbled up version of english.'+
                  '\n~If the word starts with a consinant:'+
                  '\n\t~Take the first letter of the word and put it at the end.'+
                  '\n\t~Then add \"ay\" to the end of that.\n\t~Ex.:  Pig---> igpay'+
                  '\n~If the word starts with a vowel:\n\t~Just add \"yay\" to the end.'+
                  '\n\t~Ex.: are---> areyay\n~Do that to every word in the sentence and you got it!'+
                  '\n\tEX.: What is grass?---> hatway isyay rassgay?')
            input("Press enter to continue-->")
        #otherwise the computer alerts the user to its confusion
        else:
            print("\n")
            print("*"*60)
            print("Sorry, what was that?")


#Print Conversation Function
#Version 1
#9/15/15
#prints the conversation that has been going on
def print_conversation(conversation):
    #prints the main GUI for conversation menu
    print("___________________Conversation_________________")
    #if no one has spoken, prints that there has been no conversation
    if len(conversation)==0:
        print("There have been no conversations yet.")
    #otherwise prints the conversation
    else:
        print(conversation)
    input("Press enter to continue-->")


#Setings function
#Version  1
#makes it so that the user can change the translators settings
def settings(y_words, secondary_language):
    setting_loop=True
    while setting_loop:
        print("*"*60)
        print("__________________Settings__________________")
        print("\t0-Go back to translator\n\t1-Y_words\n\t2-Language\n\n")
        if secondary_language=="giberish":
            print("!!!!!Warning: You cannot translate from gibberish to english!!!!!")
        user_selection=input("Select a catagory by typing it's # and pressing enter-->")
        if user_selection=="0":
            return y_words, secondary_language
            setting_loop=False
        elif user_selection=="1":
            y_words=y_word(y_words)
        elif user_selection=="2":
            secondary_language=change_language(secondary_language)
        else:
            print(".!?."*10)
            print("Sorry, the computer did not understand that last entry")
            print(".!?."*10)


#Y word function
#9/28/15
#Version 1
#Lets the user manualy enter a y word
def y_word(y_words):
    y_word_loop=True
    print_update=False
    while y_word_loop:
        print("*"*60)
        print("__________________Y-words__________________")
        print('\t0-Go back to settings\n\t1-Importance of Y_words'
              '\n\t. . .or just type in an english word that starts in y and press enter\n\n')
        if print_update==True:
            print(update)
            print_update=False
        user_selection=input("Select a catagory by typing it's # and pressing enter-->")
        if user_selection=="0":
            y_word_loop=False
            return y_words
        elif user_selection=="1":
            print("\n"	)
            print("*"*60)
            print("__________Importance of Y-words__________")
            print('~When translating from piglatin to english, the translator\n can sometimes'
                  ' get a little mixed up.\n\t For example:'
                  'is --> isyay \n\t\tyellow --> ellowyay.'
                  '\nYou can see that if the computer just deleted the \"yay\" at\n the end,'
                  'then yellow would become ellow. If you only deleted\n the \"ay\" then is '
                  'becomes isy. By adding to the y-words list\n you give the computer a more '
                  'complete list of words that\n start in y, therefor increasing its ability '
                  'to translate words correctley.')
            input("Press enter to continue-->")
        elif len(user_selection)>1 and user_selection[len(user_selection)-3:].lower()!="ay" and user_selection[0].lower()=="y":
            if user_selection.lower() not in y_words:
                #perform the general translation
                first_letter=user_selection[0]
                new_word=user_selection+first_letter+"ay"
                new_word=new_word[1:]
                y_words[new_word]=user_selection
                print_update=True
                update="-->",user_selection, "has been added to the Y-words dictionary!"
        else:
            print(".!?."*10)
            print("Sorry, the computer did not understand that last entry")
            print(".!?.")


#Change language function
#9/28/15
#Version 1
#Allows the user to change the secondary language
def change_language(secondary_language):
    change_language_loop=True
    update_screen=False
    while change_language_loop:
        print("*"*60)
        print("__________________Language__________________")
        print("\t0-Go back to settings\n\t1- English->Piglatin\n\t2- English->Gibberish\n\n")
        if update_screen==True:
            print(update)
            update_screen=False
        user_selection=input('Select your secondary language by typing it\'s # \n'+
                             'from the menu and pressing enter-->')
        if user_selection=="0":
            change_language_loop=False
            return secondary_language
        elif user_selection=="1":
            if secondary_language!="piglatin":
                update_screen=True
                update="--> Your secondary language is now piglatin."
            secondary_language="piglatin"
        elif user_selection=="2":
            if secondary_language!="giberish":
                update_screen=True
                update="--> Your secondary language is now giberish."
            secondary_language="giberish"
        else:
            print(".!?."*10)
            print("Sorry, the computer did not understand that last entry")
            print(".!?."*10)


#Not Alpha Function
#Version 1
#9/15/15
#sees if all the user entered was junk
def not_alpha(original):
    #preset variables
    symbol_count=0
    #goes through each letter in the string to be translated and determines if it is all symbols or letters
    for letter in original:
        if not letter.isalpha():
            symbol_count+=1
    #calculates the % of symbols
    symbol_percent=float(symbol_count/len(original))
    #determines if that percent is acceptable or not
    if symbol_percent>0.5:
        return True
    else:
        return False


#Translate Text Function
#Version 2
#9/27/15
#the function that translates the text
def translate_text(original_text, y_words, secondary_language):
    #presets variables
    original_text+="  "                           #side effect!!!
    if secondary_language=="piglatin":
        #determines the language of the teat to be translated
        language=determine_language(original_text)
    else:
        language="null"
    #goes through the list of words and translates each one
    translated_text, y_words=pick_words(original_text, language, y_words, secondary_language)
    return original_text, translated_text, y_words


#determine language function
#Version 2
#9/15/15
#determines the language of the original text
def determine_language(original_text):
    #preset variables
    word_tally=0
    y_word_tally=0
    counter=0
    word=""
    original_text+=" "
    y_word_list=[]
    #loop that goes through the text and picks out words
    word_loop=True
    while word_loop:
        character=original_text[counter]
        #if is a word ending character, the word has ended
        if (character==" " or character=="." or character=="," or character==";" or character==":" or character=="?" or character=="!" or character=="\"" or character=="'" or character=="-") and (character!="0" and character!="1" and character!="2" and character!="3" and character!="4" and character!="5" and character!="6" and character!="7" and character!="8" and character!="9" and character!="%"):
            word_tally+=1
            if word[len(word)-2:]=="ay":
                y_word_tally+=1
            counter+=1
            #if the character is a number, skip it
        elif character=="0" or character=="1" or character=="2" or character=="3" or character=="4" or character=="5" or character=="6" or character=="7" or character=="8" or character=="9" or character=="%":
            counter+=1
        #if it is none of the above, the word has not ended
        else:
            word+=character
            counter+=1
        #if the string has ended quit the loop
        if counter==len(original_text):
            #print word_tally ,y_word_tally
            word_loop=False
        character=""
    if word_tally< 3:
        discrenpency_value=word_tally-1
    else:
        discrenpency_value=word_tally-2
    #determines the overall language
    if y_word_tally >= word_tally-discrenpency_value:
        return "piglatin"
    else:
       return "english"


#Pick Words Function
#Version 1
#9/15/15
#picks out the words in the text and calls the function to translate them
def pick_words(original_text, original_language, y_words, secondary_language):
    #preset variables
    counter=0
    translated_text=""
    word=""
    #the main loop that picks out words and translates them
    pick_out_words_loop=True
    while pick_out_words_loop:
        #sets a variable letter to the next character in the string
        letter =original_text[counter]
        #if the character is a symbol and is not a "word ending", translate
        if letter.isalpha()==False and letter!="." and letter!="'" and letter!="," and letter!="!" and letter!="?" and letter!=" ":
            #translate word, then attach the symbol at the end of that
            if len(word)!=0:
                if secondary_language!="giberish":
                    translated_word, y_words=translate_word(word, original_language, y_words)
                else:
                    translated_word=translate_gibberish_word(word)
                translated_text+=translated_word
                translated_word=""
                word=""
            translated_text+=letter
        #if the character is a "word ending" character, translate the word, then add the punctuation and skip the space at the end of that
        elif letter=="." or letter=="," or letter=="!" or letter=="?":
            if len(word)!=0:
                if secondary_language!="giberish":
                    translated_word, y_words=translate_word(word, original_language, y_words)
                else:
                    translated_word=translate_gibberish_word(word)
                translated_text+=translated_word
                translated_word=""
                word=""
            translated_text+=letter
            #counter+=1
        # if the character is a space, translate the word
        elif letter==" ":
            if len(word)!=0:
                if secondary_language!="giberish":
                    translated_word, y_words=translate_word(word, original_language, y_words)
                else:
                    translated_word=translate_gibberish_word(word)
                translated_text+=translated_word
                translated_word=""
                word=""
            translated_text+=letter
        #if letter has a apostrophy, translate accordingly
        elif letter=="'" and original_language!="piglatin":
            if len(word)!=0:
                if secondary_language!="giberish":
                    translated_word, y_words=translate_word(word, original_language, y_words)
                else:
                    translated_word=translate_gibberish_word(word)
                translated_text+=translated_word
                translated_word=""
                word=""
            counter+=1
            letter=original_text[counter]
            if letter=="m":
                translated_text+=" amyay "
            else:
                translated_text+="isyay "
            counter+=1
        #otherwise, add the character to the string to be translated
        else:
            word+=letter
        counter+=1
        #if the counter is at the end of the string,translate the last word and exit the loop
        if counter==len(original_text)-1:
            if len(word)!=0:
                translated_word,y_words=translate_word(word, original_language, y_words)
                translated_text+=translated_word
                translated_word=""
                word=""
            pick_out_words_loop=False
    return translated_text,y_words


#Translate words Function
#Version 2
#9/21/15
#the function that translates the words
def translate_word(word, original_language, y_words):
    #print "working" if word[0]==word[0].upper() else "Not working"
    #if the word is captilized, make note of it so it can be used latter on
    if word[0]==word[0].upper():
        capitilized=True
    else:
        capitilized=False

    if original_language=="english":
        # if the word starts in a vowel, translate accordingly
        if word[0]=="a" or word[0]=="e" or word[0]=="i" or word[0]=="o" or word[0]=="u":
            new_word=word+"yay"
        #otherwise perform the general translation
        else:
            first_letter=word[0]
            new_word=word+first_letter+"ay"
            new_word=new_word[1:]
        #a dictionary that stores english words that start in y, for piglatin translation latter
        if word[0].lower()=="y" and already_in_values(word,y_words)!=True:
            y_words[new_word]=word
    else:
        """original language==piglatin"""
        #if the word in english starts in y, it might be in y words with its translated equivalant
        if word.lower() in y_words:
            new_word=y_words[word]
        #deals with the case when the english word starts with a voweland yay is just tacked on to the end.
        elif (word[len(word)-3:].lower()=="yay") and (word not in y_words):
            new_word=word[:len(word)-3]
        #otherwise, just translate like the inverse of the english process
        else:
            #print word
            new_word=word[:len(word)-2]
            last_letter=new_word[len(new_word)-1:]
            #print last_letter
            new_word=last_letter+new_word
            new_word=new_word[:len(new_word)-1]
    new_word=new_word.lower()
    if capitilized==True:
        first_letter=new_word[0].upper()
        #print first_letter
        new_word=first_letter+new_word[len(new_word)-(len(new_word)-1):]
    return new_word, y_words


#Already in values function
#Version 1
#9/15/15
#determines if the word is already in the dictionaries values
def already_in_values(word,y_words):
    y_word_values=y_words.values()
    for item in y_word_values:
        if item==word:
            return True


#Translate to gibberish function
#9/28/15
#Version 1
#translates the given word to giberish
def translate_gibberish_word(word):
    random_characters=["\"", "?", ":", "{", "}", "+", "=", "*", ")", "$", "@", "!", "1", "3", "5", "d", "E", "W", "V", "/","%", "&", "^"]
    if len(word)>2:
        first_letter=word[0]
        last_letter=word[len(word)-1:]
        middle_word=""
        for x in range(len(word)-2):
            middle_word+=random_characters[randint(0,len(random_characters)-1)]
        translated_word=first_letter+middle_word+last_letter
    else:
        translated_word=word
    return translated_word


#Main Function
#Version 2
#9/27/15
def main():
    print_load_screen()
    main_loop=True
    secondary_language="piglatin"
    while main_loop:
        main_loop=user_entry(secondary_language)
    print("\n"*3)
    print("\t    Thank you for using this translator!")
    print("\t     ...",end="")
    for x in range(10):
        print("...",end="")
        sleep(0.1)

main()
