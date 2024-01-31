import os
import string

def read_words(filename):
    res = []
    with open(filename, 'r', encoding='utf-8-sig') as file:
        for line in file:
            canonize = lambda w: (w.lower()).strip(string.punctuation + string.whitespace)
            words = list(map(canonize, line.split()))
            res.extend(words)
    return res

def count_only(words, count_words):
    count_words = set(count_words)
    histogram = dict.fromkeys(count_words, 0)
    for word in words:
        if word in count_words:
            histogram[word] += 1
    return histogram

def count_all_except(words, stopwords):
    count_words = set(words) - set(stopwords)
    return count_only(words, count_words)

def filter_hist(hist, min_count):
    res = {}
    tops = sorted_hist(hist)
    current_count, current_word = tops.pop(0)
    while(current_count >= min_count):
        res[current_word] = current_count
        current_count, current_word = tops.pop(0)
    return res

def sorted_hist(hist):
    return sorted(list(zip(hist.values(), hist.keys())), reverse=True)

# -----------------------------------------------------------

if __name__ == '__main__':

    print('\n\n--- Excercise 2 ---\n')

    local_file = lambda file: os.path.join(os.path.dirname(__file__), file)
    words = read_words(local_file('nilsholg-eng.txt'))
    print(words[0:20], '\n...\n', words[-20:])

    print('\n\n--- Excercise 3 ---\n')

    provinces = read_words(local_file('provinces.txt'))
    print(provinces)

    hist = count_only(words, provinces)
    print(hist['skåne'])

    import pprint
    pprint.pprint(hist)


    print('\n\n--- Excercise 4 ---\n')

    stop_words = read_words(local_file('exceptions.txt'))
    book_hist = count_all_except(words, stop_words)
    print(book_hist['goosey-gander'])

    print(sorted_hist(hist),'\n')


    print('\n\n--- Excercise 5 ---\n')

    top_20 = sorted_hist(book_hist)[:20]
    for pair in top_20:
        print(*pair)


    print('\n\n--- Excercise 6 ---\n')

    print(filter_hist(book_hist, 400))
    print(len(filter_hist(book_hist, 100)))


    print('\n\n--- Excercise 7, 8, 9 ---\n')

    alice_words = read_words(local_file('alice-eng.txt'))
    alice_set = set(alice_words)

    print(len(alice_words), len(alice_set))

    alice_words_set = alice_set


    print('\n\n--- Excercise 10 ---\n')

    nils_words = words
    nils_words_set = set(nils_words)
    print(len(nils_words), len(nils_words_set))

    print('\n\n--- Excercise 12, 13, 14 ---\n')

    alice_words_only = alice_words_set - nils_words_set
    print(len(alice_words_only), '\n')

    alice_only_counts = count_only(alice_words, alice_words_only)
    alice_only_top20 = sorted_hist(alice_only_counts)[:20]
    for pair in alice_only_top20:
        print(*pair)
