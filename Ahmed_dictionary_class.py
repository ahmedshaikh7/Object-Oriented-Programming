from word import Definition, Entry
from typing import List

class MyDictionary:
    def __init__(self) -> None:
        #implement
        self.entries = {}
        self.__num_entries__ = 0  
        
        
    def get_num_entries(self) -> int:
        # implement
        return self.__num_entries__

    def suggest_closest_word(self, word: str) -> str:
        
        #score_werd = self.__levenshtein_dist__(werd, word)
        #for self.werd in mydictionary:
        
        distance_list = []
        word_list = []
        
        for letter in self.entries.keys():
            for i in range(len(self.entries[letter])):
                the_word = self.entries[letter][i].word
                word_list.append(the_word)
                
        #appends each levenshtein distance into an empty list
        for each in word_list:
            val = self.__levenshtein_dist__(each, word)
            distance_list.append(val)
            
        
        #uses parallel lists to use the number to call the cooresponding word
        for x in range(len(distance_list)):
            if distance_list[x] == min(distance_list):
                return word_list[x]
            

    
    def add_entries(self, entries: List[Entry]) -> None:
        for entry in entries:
            first_letter = entry.word[0]
            if first_letter in self.entries:
                self.entries[first_letter].append(entry)
                self.entries[first_letter].sort(key = lambda x: x.word)
            else:
                self.entries[first_letter] = [entry]
        self.__num_entries__ += len(entries)
                
    def get_entries_by_window(self, word: str, window: int) -> List[Entry]:
        i = self.get_word_index(word)
        if i == -1:
            return []
        else:
            max_i = len(self.entries[word[0]])
            start_i = i - window//2
            if start_i < 0:
                start_i = 0
            end_i = max((i + window//2) % max_i, (start_i + window) % max_i)
            return self.entries[word[0]][start_i:end_i]
    
    def get_word_index(self, word: str) -> int:
        ''' Return the index of word in the List given by accessing the
        value of self.entries, associated with key word[0]. If the word is
        not found, return -1.
        
        >>> word = "illuminate"
        >>> def1 = Definition("make lighter or brighter", "verb")
        >>> def2 = Definition("make free from confusion or ambiguity", "verb")
        >>> def3 = Definition("add embellishments and paintings to (medieval manuscripts)", "verb")
        >>> entry = Entry(word, [def1, def2, def3])
        ...
        >>> my_dictionary = MyDictionary()
        >>> my_dictionary.add_entries([entry])
        >>> my_dictionary.get_word_index(word)
        0
        '''

        starting_letter = word[0]

        if starting_letter in self.entries:
            curr_entries = self.entries[starting_letter]
            l = 0
            r = len(curr_entries) - 1

            while l < r:
                m = (l + r) // 2
                curr_word = curr_entries[m].word

                if word == curr_word:
                    return m
                elif word > curr_word:
                    l = m + 1
                elif word < curr_word:
                    r = m - 1

            if l == r and word == curr_entries[l].word:
                return l
            
        return -1
    def __levenshtein_dist__(self, word1: str, word2: str, display = False) -> int:
        ''' Return the minimum edit distance between two words, word1 and word2.
        The optional display parameter displays the full calculation matrix when
        set to True, and hides it otherwise.

        The minimum edit distance is the minimum number of {swaps, inserts, deletes}
        needed to change word1 to word2 and vice versa.

        >>> d = MyDictionary()
        >>> d.__levenshtein_dist__('capybara', 'llama')
        6
        >>> d.__levenshtein_dist__('apple', 'bapple')
        1
        '''
        
        dist_array = [None]*(len(word1) + 1)
        for i in range(len(word1) + 1):
            dist_array[i] = [0] * (len(word2) + 1)
        
        for i in range(0, len(word1)+1):
            for j in range(0, len(word2)+1):
                if min(i, j) == 0:
                    dist_array[i][j] = max(i, j) 
                else:
                    (val1, val2, val3) = (dist_array[i][j-1] + 1, \
                                          dist_array[i-1][j] + 1, \
                                          dist_array[i-1][j-1] + (word1[i-1] != word2[j-1]))
                    
                    dist_array[i][j] = min(val1, val2, val3)
                    
        if display:               
            for item in dist_array:
                print(item)

        return dist_array[-1][-1]

    def __repr__(self):
        s = ''
        keys = list(self.entries.keys())
        keys.sort()
        for key in keys:
            for entry in self.entries[key]:
                s += str(entry)
                s += '\n'
        return s

if __name__ == "__main__":
    # testing

    #word = "illuminate"
    #def1 = Definition("make lighter or brighter", "verb")
    #def2 = Definition("make free from confusion or ambiguity", "verb")
    #def3 = Definition("", "verb")
    #entry = Entry(word, [def1, def2, def3])

    #my_dictionary = MyDictionary()
    #my_dictionary.add_entries([entry])
    

    #print(my_dictionary)     
    word = "hi"
    def1 = ("uttering of a greeting", "noun")
    entry = Entry(word, [def1])
    my_dictionary = MyDictionary()
    my_dictionary.add_entries([entry])
    word = 'run'
    def2 = ("move at a faster speed", "verb")
    entry = Entry(word, [def2])
    my_dictionary.add_entries([entry])    
    my_dictionary.suggest_closest_word("ran")      
