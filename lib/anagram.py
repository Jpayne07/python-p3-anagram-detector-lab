class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, list):
        anagrams = []
        for item in list:
            if ''.join(sorted(item)) == ''.join(sorted(self.word)):
                anagrams.append(item)
                print(anagrams)
        return anagrams
            
            

listen = Anagram('listen')

listen.match(['enlists', 'google', 'inlets', 'banana','listen'])