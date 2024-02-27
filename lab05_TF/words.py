import string
import os

def read_words(filename):

    # Make sure the script and the file you are trying to load are
    # in the same directory
    filepath = os.path.join(os.path.dirname(__file__), filename)

    # Open the file (utf-8 is the encoding that is used).
    file = open(filepath, encoding='utf-8-sig')

    # Add words of each line to list
    wordlist = []
    for line in file:
        for word in line.split():
            wordlist.append(word.strip(string.punctuation + string.whitespace).lower())

    return wordlist

def count_only(words, count_words):
    d = {}
    for word in count_words:
        d[word] = words.count(word)
    return d

def count_all_except(words, stopwords):
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            if not word in stopwords:
                freq[word] = 1
    return freq


def filter_hist(hist, min_count):
    return [(count,word) for word,count in hist.items() if count >= min_count]

def sorted_hist(hist):
    hist_list = []
    for word in hist:
        hist_list.append((hist[word],word))
    hist_list.sort(reverse=True)
    return hist_list


# 3
provinces = read_words('provinces.txt')
# print(provinces)

words = read_words('nilsholg-eng.txt')
# print (words[1:20])

hist = count_only(words, provinces)
print(hist)
print(hist['skåne'])

for p,c in hist.items():
    print(p + ': ' + str(c))


# 4
exclude = read_words('exceptions.txt')
hist = count_all_except(words,exclude)
print(hist)
print(hist['goosey-gander'])

# 5
print(sorted_hist(hist)[0:40])

# 6
common_words = filter_hist(hist,100)
print (str(len(common_words)) + ' common words')

# 7
alice_words = read_words('alice-eng.txt')

# 8
alice_words_set = set(alice_words)

# 9
print ('Wordcount: ' + str(len(alice_words)))
print ('Unique wordcount: ' + str(len(alice_words_set)))
# each word is only included once i the set, but multiple times in the list

# 10
nils_words_set = set(words)

# 11
print ('Unique wordcount in Alice: ' + str(len(alice_words_set)))
print ('Unique wordcount in Nils: ' + str(len(nils_words_set)))
# Nils uses about 3 times more words

# 12
diff = alice_words_set.difference(nils_words_set)

# 13
alice_only_counts = count_only(alice_words, diff)

# 14
alice_only_counts_sorted = sorted_hist(alice_only_counts)
for (count,word) in alice_only_counts_sorted[0:20]:
    print(word + ': ' + str(count) + ' times')

# Lots of wierd creatures
# Queen is mentioned 72 times


# -----------------------------------------------------------
if False: #__name__ == '__main__':
    filename = 'nilsholg-eng.txt'

    # Make sure the script and the file you are trying to load are
    # in the same directory
    filepath = os.path.join(os.path.dirname(__file__), filename)

    # Open the file (utf-8 is the encoding that is used).
    file = open(filepath, encoding='utf-8-sig')

    # Print each line in the file
    for line in file:
        print(line)
