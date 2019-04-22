#The StatisticalAnalysis object is the process by which new words can be added to the historic analysis
#TODO create writing all the data to a text file to save historical data
from Brick import Brick

class StatisticalAnalysis:
    historic = [Brick("test")]
    historic[0].newAppearance("","","")

    def __init__(self):
        a = 42

    def performNewAnalysis(self):
        #This is the function that is accessed by the main program, all of the rest are internal to the class
        words_list,extension = self.getInput()
        self.updateStats(words_list,extension)
        
        
    def getInput(self):
        #This function returns a standardized text (non-lemmatized)
        phrase = input("Please insert your phrase: ")
        standard_phrase, extension = self.standardizeInput(phrase)
        return standard_phrase,extension
        
    def standardizeInput(self,phrase):
        #This function sets the phrase to lower case, removes punctuation and splits the words into a list
        #Requirements: The original input sentence
        phrase = phrase.lower()
        clean_phrase = self.removePunctuation(phrase)
        words, extension = self.splitWords(clean_phrase)
        return words, extension
    
    def removePunctuation(self, phrase):
        #This function removes the punctuation from the list
        #Requirements: lower case phrase
        punctuation = "-_?:!.,;()\""
        for character in phrase:
            if character in punctuation:
                phrase = phrase.replace(character, '')
        return phrase

    def splitWords(self,phrase):
        #This function splits the sentece into words. It add a blank space at the beginning and at the end to help know which words usually begin or end sentences
        #Requirements: clean phrase (lower case and without punctuation)
        phrase_words = phrase.split(" ")
        phrase_words.insert(0,"")
        extension = len(phrase_words)
        phrase_words.insert(extension,"")
        return phrase_words, extension


    def updateStats(self,words_list,extension):
        #This function updates the stats of the words
        for i in range(1,extension,1):
            current_brick = Brick(words_list[i])
            found = False
            for item in self.historic:
                if current_brick.word == item.word:
                    found = True
                    found_brick = item
                    break

            if found == True:
                current_brick = found_brick
                current_brick.newAppearance(words_list[i-1],words_list[i+1],"what")
    
            else:
                self.historic.append(current_brick)
                current_brick = self.historic[len(self.historic)-1]
                current_brick.newAppearance(words_list[i-1],words_list[i+1],"what")
    

                                   
        for record in self.historic:
            print(record.getAllStats())




