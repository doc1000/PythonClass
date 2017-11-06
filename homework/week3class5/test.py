from collections import Counter
import string

word_ctr = Counter()
translator = str.maketrans('','',string.punctuation)

with open('Hard2.py') as txt_file:
    for line_num, raw_line in enumerate(txt_file):
        # line = raw_line.strip()
        # line.strip()
        # line.lower()
        # line.translate(translator)
        words = raw_line.strip().lower().translate(translator).split()
        #print(str(line_num) + ': ' + str((len(line.split(' ')))))
        for word in words:
            word_ctr[word] += 1
#word_ctr_d = dict(word_ctr)
#print([x,y for x,y in dict(word_ctr)])
print(word_ctr)
#print(word_ctr_d)
