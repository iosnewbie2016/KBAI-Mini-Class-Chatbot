"""
ADD YOUR CODE HERE

Please read project directions before importing anything
"""


import common


class StudentAgent:

    def __init__(self, verbose):
        self._verbose = verbose
        # TODO: Add your init code here
        return
        
    
    # takes in list of words, returns question_object and data_requested
    def input_output(self, word_list):
        print(word_list) # for debugging only

        # TODO: Add your code here
        #Variable definition
        _question_object = ""
        _data_requested = ""
        word_list_copy = word_list #Copy of the word list
        
        #Dictionaries/grammars for different types of words including the data requested and questions
        datasList = ("DUEDATE","RELEASEDATE","DURATION","WEIGHT","PROCESS")
        questionsList = ("what","where","when","how")
        prepositionList = ("of","in","on","at","to","for","this","that")
        verbList = ("is", "are","am","be","being","will","would","must","should","does","do","did","can","could","has","have","had","give","given")
        timeList = ("time","day","days","date")
        howTimeList = ("much","long","many")
        
        #Sensitive words that will lead to instant object returns    
        releaseWords = ("release","releases","released","publish","start","begin")
        dueWords = ("due","deadline")
        weightWords = ("weight","percentage","worth","contribute")
        processWords = ("procedure","process")
        additionalWords = ("we","work","class")
        whenDueWords = ("turn","turned","turning","submit","submitted","submitting","complete","completed","completing")
        whereWords = ("location","place","find","locate")
        
        bannedWords = prepositionList + verbList + timeList + howTimeList + releaseWords + dueWords + weightWords + processWords + whenDueWords    #Banned words for object name
        stripWords = prepositionList + verbList + timeList + howTimeList + additionalWords + whenDueWords   #Remaining words to strip off
        
        #Default returns for all the questions list
        #Default data return if question starts with 'What'
        if word_list[0] == questionsList[0]:
            if word_list[1] in timeList:    #If 'what' is followed by the words in timeList
                _data_requested = datasList[1]  #return RELEASEDATE
                word_list_copy = word_list[2:]  #delete the words from the list
            else:
                data_requested = datasList[3] #return WEIGHT
                word_list_copy = word_list[1:] #delete the word from the list
        #Default data return if question starts with 'where'
        elif word_list[0] == questionsList[1]:
            _data_requested = datasList[4] #return PROCESS
            word_list_copy = word_list[1:] #delete the word from the list
            for word in word_list_copy:
                if word in whereWords:  #If words such as location or place after 'where' exists, remove it
                    word_list_copy.remove(word)
        #Default data return if question starts with 'when'
        elif word_list[0] == questionsList[2]:
            _data_requested = datasList[1] #return RELEASEDATE
            word_list_copy = word_list[1:] #delete the word from the list
            for word in word_list:  
                if word in whenDueWords:    #if when is followed by words such as turn in or submit  
                    _data_requested = datasList[0]  #return DUEDATE
                    word_list_copy.remove(word)
                    break
        #Default data return if question starts with 'How'
        elif word_list[0] == questionsList[3]:
            if word_list[1] in howTimeList: #Handle "how long"
                if word_list[2] in timeList: #handle "how much time"
                    word_list_copy = word_list[3:] #delete the word from the list
                else:
                    word_list_copy = word_list[2:] #delete the word from the list
                _data_requested = datasList[2] #return DURATION
            else:
                _data_requested = datasList[4] #return PROCESS
                word_list_copy = word_list[1:] #delete the word from the list
        
        #Check for sensitive words that instantly returns data requested
        
        #RELEASEDATE
        for i in range(len(word_list_copy)):
            if i < len(word_list_copy):
                if word_list_copy[i] in releaseWords:
                    counter = i #Get index of the word after release
                    word_list_copy.pop(i)  #Remove the release word
                    if counter < len(word_list_copy):
                        if word_list_copy[counter] in timeList:
                                word_list_copy.remove(word_list_copy[counter])  #Remove the word after release word if it is in time list
                    _data_requested = datasList[1]  #return RELEASEDATE
        
        #DUEDATE
        for i in range(len(word_list_copy)):
            if i < len(word_list_copy):
                if word_list_copy[i] in dueWords:
                    counter = i #Get index of the word after due
                    word_list_copy.pop(i)  #Remove due
                    if counter < len(word_list_copy):
                        if word_list_copy[counter] in timeList:
                            word_list_copy.remove(word_list_copy[counter])  #Remove the word after due word if it is in time list
                    _data_requested = datasList[0]  #return DUEDATE
        
        #WEIGHT
        for i in range(len(word_list_copy)):
            if i < len(word_list_copy):
                if word_list_copy[i] in weightWords:
                    word_list_copy.pop(i)  #Remove weight
                    _data_requested = datasList[3]  #return WEIGHT
        
        #PROCESS
        for i in range(len(word_list_copy)):
            if i < len(word_list_copy):
                if word_list_copy[i] in processWords:
                    word_list_copy.pop(i)  #Remove process
                    _data_requested = datasList[4]  #return PROCESS
        
        #Check if the word list contains any articles to get object
        if len(word_list_copy) > 0:
            for i in range(len(word_list_copy)):
                if i < len(word_list_copy):
                    if word_list_copy[i] == 'a' or word_list_copy[i] == 'an' or word_list_copy[i] == 'the' or word_list_copy[i] == 'my' or word_list_copy[i] == 'our':   #Check if there is any article in the list
                        counter = i   #Get index of the article
                        word_list_copy.pop(i)  #Remove article
                        if counter < len(word_list_copy):
                            if word_list_copy[counter] not in bannedWords:    #Project name cannot be part of bannedWords
                                _question_object = word_list_copy[counter]    #Get the word after the article
                                word_list_copy.remove(word_list_copy[counter])  #Remove word from the list if it is a valid object name
                                if counter < len(word_list_copy):
                                    if word_list_copy[counter] not in bannedWords:  
                                        _question_object += " " + word_list_copy[counter] #If the word after first object word is not 'in the list' then add it as part of the object
                                        word_list_copy.remove(word_list_copy[counter])  #Remove word from the list if it is a valid object name
                                return _question_object, _data_requested
                                
        #Case for no articles in the sentence
        #Strip the sentence off unnecessary words 
        loop = 0
        while len(word_list_copy) > 0:
            if loop == len(word_list_copy):
                break
            elif loop < len(word_list_copy):
                if word_list_copy[loop] in stripWords:
                    word_list_copy.pop(loop)
                    loop -= 1
            loop += 1
        
        #Special case to check for 'i' in the sentence
        if len(word_list_copy) > 0:
            for word in word_list_copy:
                if word == 'i':
                    word_list_copy.remove(word)
        
        #Return object requested as one word or more words concatenated
        if len(word_list_copy) > 0:
            for word in word_list_copy:
                if word == word_list_copy[-1]:
                    _question_object += word
                else:
                    _question_object += word + " "

        return _question_object, _data_requested
    
    
