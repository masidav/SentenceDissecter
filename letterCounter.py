class LetterCounter():
    def __init__(self):
        #The three properties to save values asked for
        #A dictionary data structure was used  to easily track the differing letters between 3 structures
        self.totals = {"A":0, "C":0, "G":0, "T":0}
        self.percentages = {"A":0, "C":0, "G":0, "T":0}
        self.consectutives = {"A":0, "C":0, "G": 0, "T": 0}
    def countLetters(self, sentence):
        #This function takes a sentence and finds the total count of the selected 4 letters (A, C, G, T)
        # and finds their count, percentage(total includes spaces) and the highest consecutive letter count

        #Since upper and lower case don't matter it will be easier to have all capitilized
        sentence = sentence.upper()
        # need to reset consecutives since the highest count of "in a row" letters are saved
        self.consectutives = {"A": 0, "C": 0, "G": 0, "T": 0}
        self.sentenceLength = len(sentence)
        for letter in "ACGT":
            #count returns the amount of letters in a string
            letterCount = sentence.count(letter)
            self.totals[letter] = letterCount
            self.percentages[letter] = letterCount/self.sentenceLength
            self.countConsecutives(letter, sentence)
    def countConsecutives(self, letter, sentence):
        #This function will take a letter and sentence and find the consectutive occurences of said letter
        # and find the highest consectutive count

        #Find all indexes of a letter
        letterIndexes = [index for index in range(len(sentence)) if sentence[index] == letter]
        #if no letters are found the consecutive will stay zero
        if len(letterIndexes) == 0:
            return
        #Since we know there is at least letter we can assume the consectutives will be as low as 1
        count = 1
        #lastIndex is used as reference to see if the numbers are consectutive
        lastIndex = letterIndexes[0]
        for index in letterIndexes[1::]:
            if index - lastIndex == 1:
                count = count+1
            elif count > self.consectutives[letter]:
                self.consectutives[letter] = count
                count = 1
            else:
                count = 1
            lastIndex = index
         #This for loop will not update the count if the last item was in a row so we check here
        if count > self.consectutives[letter]:
                self.consectutives[letter] = count
    def displayCounts(self):
        #This function displays saved results from this class
        print("Total Letter Count: "+str(self.sentenceLength))
        for key, value in self.totals.items():
            printString = key+": "+str(value)
            print(printString)
        print("Percentages")
        for key, value in self.percentages.items():
            printString = key+": "+str(round(value*100, 2))+"%"
            print(printString)
        print("Consecutives")
        for key, value in self.consectutives.items():
            printString = key+": "+str(value)+" in a row"
            print(printString)