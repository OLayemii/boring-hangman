class Words:
    def __init__(self):
        self.wordfile = open("words.txt", "r")
    
    def getwords(self):
        wordlist = []
        for line in self.wordfile:
            wordlist.append(line.strip())
        return wordlist
