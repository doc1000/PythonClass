from collections import Counter
import string

class ReportGenerator:
    def __init__(self): #constructor - so you can call it as a pointer and assign to variable, sets up distinct place in memory adn lets you re-use the self
        #pass
        self._ctr = Counter() #instancde attribute or varilable.  available to each instance of class
        self._translator = str.maketrans('','',string.punctuation)
        #self._my_name = __name__

    def get_counts(self):
            return self._ctr

    def count_file(self,filename):
        with open(filename) as txt_file:
            for line_num, raw_line in enumerate(txt_file):
                words = raw_line.strip().lower().translate(self._translator).split()
                for word in words:
                    self._ctr[word] += 1
        return self #this lets you chain together methods

    def my_name(self):
        return __name__

print(__name__)

if __name__ == '__main__': #if you actually type in the name of this file in command module, then this runs, otherwise it DOES NOT run... for testing purposes
    rg = ReportGenerator()
    rg.count_file('Hard2.py')
    print(rg.get_counts())
    #print(rg)
    print(rg.my_name())
