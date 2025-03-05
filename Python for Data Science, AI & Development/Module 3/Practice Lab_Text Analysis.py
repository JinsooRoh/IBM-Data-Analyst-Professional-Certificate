# Scenario: Text Analysis
"""
# Part A
# Step 1: Define a string
givenstring="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

# Step 2: Define the class and its attributes
class TextAnalyzer(object):
    # The __init__ method initializes the class with a 'text' parameter.
    # This will store the provided 'text' as an instance variable.
    def __init__(self, text):


# Step 3: Implement a code to format the text in lowercase
class TextAnalzer(object):
    
    def __init__ (self, text):
        # remove punctuation
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')

        # make text lowercase
        formattedText = formattedText.lower()

        self.fmtText = formattedText

# Step 4: Implement a code to count the frequency of all unique words
class TextAnalzer(object):
    
    def __init__ (self, text):
        # remove punctuation
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')

        # make text lowercase
        formattedText = formattedText.lower()

        self.fmtText = formattedText

    def freqAll(self):
        # split text into words
        wordlist = self.fmtText.split(' ')
        

        # Create dictionary
        freqMap = {}
        for word in set(wordlist): # use set to remove duplicates in the list
            freqMap[word] = wordlist.count(word)

        return freqMap
"""

# Step 5: Implement a code to count the frequency of a specific word
class TextAnalzer(object):

    def __init__ (self, text):
        # remove punctuation
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')

        # make text lowercase
        formattedText = formattedText.lower()

        self.fmtText = formattedText

    def freqAll(self):
        # split text into words
        wordlist = self.fmtText.split(' ')
        

        # Create dictionary
        freqMap = {}
        for word in set(wordlist): # use set to remove duplicates in the list
            freqMap[word] = wordlist.count(word)

        return freqMap

    def freqOf(self, word):
        # get frequency map
        freqDict = self.freqAll()

        if word in freqDict:
            return freqDict[word]
        else:
            return 0



# Part B
# Step 1: Create an instance of TextAnalyzer class
givenstring="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."
analyzed = TextAnalzer(givenstring)

# Step 2: Call the function that converts the data into lowercase
print("Formated Text: ", analyzed.fmtText)

# Step 3: Call the function that counts the frequency of all unique words from the data
freqMap = analyzed.freqAll()
print(freqMap)

# Step 4: Call the function that counts the frequency of a specific word¶
word = "lorem"
frequency = analyzed.freqOf(word)
print("The word",word, "appears", frequency, "times.")
