#The purpose of this classes is to help organizing the analysis of the word structure and frequency in the project AcademAI
#The Brick object refers to a word. This name was giving to avoid redundancy and improve code readibility. The name stems from the word being the basic block of speech

class Brick:
    #Previous list, after list: lists containing which words are more frequently before and after a word in the text
    #Counter is a variable to store how many times the word has been found
    def __init__(self,word):
        self.word = word
        self.counter = 0
        self.previous = {}
        self.after = {}
        self.headers = {}
        
    def newAppearance(self, previous, after, header):
        #The code that runs every time the word has been detected
        self.counter += 1
        self.updateBefore(previous)
        self.updateAfter(after)
        self.updateHeaders(header)

    def updateBefore(self, before):
        #Updating the statistics for the previous words
        if before in self.previous:
            self.previous[before]+=1
        else:
            self.previous[before] = 1

    def updateAfter(self,after):
        #Updating the statistics for the after words
        if after in self.after:
            self.after[after]+=1
        else:
            self.after[after] = 1

    def updateHeaders(self,header):
        #Updating the statistics for the question-header relationships
        if header in self.headers:
            self.headers[header]+=1
        else:
            self.headers[header] = 1

    def getAllStats(self):
        #Displaying the whole stats of the word
        print("This is the analysis for the word: ", self.word,"\n")
        self.getPreviousStats()
        self.getAfterStats()
        self.getHeaderStats()
        

    def getPreviousStats(self):
        #Displaying previous stats
        print("This is the analysis of the words that usually come before the word\n")
        for word in self.previous:
            print("{0:5}{1:15}{2:10}{3:10}".format("Word: ", word," Frequency: ", self.previous[word]/self.counter))

    def getAfterStats(self):
        #Displaying after stats
        print("\nThis is the analysis of the words that usually come after the word\n")
        for word in self.after:
            print("{0:5}{1:15}{2:10}{3:10}".format("Word: ", word," Frequency: ", self.after[word]/self.counter))

    def getHeaderStats(self):
        #Displaying question-headers stats
        print("\nThis is the analysis of the headers that usually relate to this word\n")
        for word in self.headers:
            print("{0:5}{1:15}{2:10}{3:10}".format("Word: ", word," Frequency: ", self.headers[word]/self.counter))
        

