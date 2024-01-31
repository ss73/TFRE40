# Excercise 1

> Test that the program works.

The program works, after renaming the supplied file `nilshogl-eng.txt` to `nilsholg-eng.txt`
which is the assumed file name used in [words.py](words.py)

# Excercise 2

> Implement the function `read_words`, accepting a file name as arument and returning a list:
> - Each word is added as en element in the list
> - Each word is converted to lower case
> - Each word is stripped from special characters
> - Each word is stripped from white space characters
>
&nbsp;

The function in [words.py](words.py) is implemented as:
```python
def read_words(filename):
    res = []
    with open(filename, 'r', encoding='utf-8-sig') as file:
        for line in file:
            canonize = lambda w: (w.lower()).strip(string.punctuation + string.whitespace)
            words = list(map(canonize, line.split()))
            res.extend(words)
    return res
```

Note that encoding `utf-8-sig` is used for reading rather than just `utf-8`. The `nilsholg` file
was likely created in a Windows based editor. For some reason MS decided to include a BOM (byte
order mark) when saving UTF-8 encoded files in Windows, which is not needed. If reading using standard
UTF-8 encoding, the first word of the text will have the Unicode character `\ufeff` prepended.

It is also convenient to use the `with open...` statement as this takes care of correctly closing
the opened file when it goes out of scope.

> Test that the program works: print the first and last words 100 words with slicing, and
> check that the result seems correct.

A simple smoke test can be performed by the following code:

```python
import os

local_file = lambda file: os.path.join(os.path.dirname(__file__), file)
words = read_words(local_file('nilsholg-eng.txt'))
print(words[0:20], '\n...\n', words[-20:])
```

...producing the following output:

```
['the', 'project', 'gutenberg', 'ebook', 'of', 'the', 'wonderful', 'adventures', 'of', 'nils', 'this', 'ebook', 'is', 'for', 'the', 'use', 'of', 'anyone', 'anywhere', 'in'] 
...
 ['how', 'to', 'help', 'produce', 'our', 'new', 'ebooks', 'and', 'how', 'to', 'subscribe', 'to', 'our', 'email', 'newsletter', 'to', 'hear', 'about', 'new', 'ebooks']
```

# Excercise 3
> Implement the function `count_only`, which taskes two parameters;
First, a list of words (for example, the book) and, second, a list of words we want to count in the text
(for example, the list of provinces).

The following code snippet implements the `count_only` function found in [words.py](words.py):
```python
def count_only(words, count_words):
    count_words = set(count_words)
    histogram = dict.fromkeys(count_words, 0)
    for word in words:
        if word in count_words:
            histogram[word] += 1
    return histogram

```
>Implement the function count_only and check that it works. The following statement
>should print the number **`51`** (if hist has been assigned its value as mentioned above):
`print(hist['skåne'])`

When running the above statement, the resulting number is **`48`**. It seems that three occurrences are missing!

As it turns out, had the reference text been the Swedish version, the output would probably have been 51, as there are two more occurrences of the word `Skane` in the English translation, and there is a final occurrence of the word `Skåne--not`, which counts as a single word since there is no white space between what a human would interpret as two words.

>Print the whole table. How many times does each province appear in the book?

The library `pprint` can be used to do a bit of formatting:

```python
import pprint
pprint.pprint(hist)
```

producing the output:

```python
{'blekinge': 21,
 'bohuslän': 3,
 'dalarna': 0,
 'dalsland': 3,
 'gotland': 0,
 'gästrikland': 3,
 'halland': 4,
 'hälsingland': 10,
 'härjedalen': 8,
 'jämtland': 3,
 'lappland': 0,
 'medelpad': 5,
 'närke': 9,
 'skåne': 48,
 'småland': 45,
 'södermanland': 0,
 'uppland': 4,
 'värmland': 0,
 'västerbotten': 0,
 'västergötland': 0,
 'västmanland': 0,
 'ångermanland': 5,
 'öland': 22,
 'östergötland': 12}
```

As it turns out there are many zeroes in the histogram. This can again be explined by the use of the translated text where you find that, for example, `Västerbotten` is (poorly) translated into `Westbottom`.

# Excercise 4

> Implement the function `count_all_except` which takes two parameters: a list of
> words to analyze, and a list of words to ignore. The function returns a dictionary
> where each counted word is matched with the number of time it occurs.
>
> The words to ignore are in the text-file [exceptions.txt](exceptions.txt)

The implementation below in [words.py](words.py) uses the existing `count_only` after creating a (rather large) set of words to count:

```python
def count_all_except(words, stopwords):
    count_words = set(words) - set(stopwords)
    return count_only(words, count_words)
```

> Test the function by printing the result (the whole dictionary). As we can see, the
> dictionary becomes quite large. A simpler way to test is to check that the word
> "goosey-gander" appears **170** times in the text.
>
> `print(hist['goosey-gander'])`


```python
215
```

Again, the result **215** differs. Likely due to the translation. A free-text search using the built-in capabilities of Visual Studio Code results in **231** hits, some of which match variants like `goosey-gander's` for example which can explain the discrepancy.

# Excercise 5

> Implement the function `sorted_hist`. It takes a dictionary as an parameter, and
> returns a list of tuples, where each tuple is a pair of an integer and a string. The
> integer is the number of occurences, and the string is the word.

The following code from [words.py](words.py) implements the specified functionality:

```python
def sorted_hist(hist):
    return sorted(list(zip(hist.values(), hist.keys())), reverse=True)
```

> Use `sorted_hist` to print the 20 words that occur most in the book, with their number
> of occurences. Each tuple should be printed on one line:
> ```
> 913 boy
> 740 ...
> ...
> ```

A simple loop is used to print the top 20 most frequent words:

```python
top_20 = sorted_hist(book_hist)[:20]
for pair in top_20:
    print(*pair)
```
producing the output:

```python
911 boy
740 said
440 geese
434 down
399 thought
397 little
391 wild
323 before
292 more
283 long
262 akka
246 must
234 big
232 such
230 himself
227 heard
226 forest
223 very
223 away
215 goosey-gander
```


# Excercise 6

> Implement the function `filter_hist` which takes a dictionary (from words to number
> of occurences) and create a new, which includes only words which appear at least
> n times in the book. The function has two parameters: the dictionary, and the number
> n. It returns a new dictionary.

The relevant part of [words.py](words.py) providing the function is:

```python
def filter_hist(hist, min_count):
    res = {}
    tops = sorted_hist(hist)
    current_count, current_word = tops.pop(0)
    while(current_count >= min_count):
        res[current_word] = current_count
        current_count, current_word = tops.pop(0)
    return res

```

>Use the result of `filter_hist` to answer the following question:
>
> * *How many words appear at least 100 times in the book?*
>
> &nbsp;

The numer of words appearing at leat 100 times can be produced by:

```python
print(len(filter_hist(book_hist, 100)))
```

This statement results in the number **102** being printed to the console:

```
102
```

# Excercise 7

>Load the file `alice-eng.txt` containing the full book of *Alice’s Adventures in Wonderland* using the function `read_words`
> and store it in another list.

```python
alice_words = read_words(local_file('alice-eng.txt'))
```

# Excercise 8

> Convert the list you have created to a set.

```python
alice_set = set(alice_words)
```

# Excercise 9

> Compare the length of the list of words to the length of the set. 
> * What is the difference?
> * Why is there such a difference?
>
> &nbsp;

Printing the lengths:
```python
print(len(alice_words), len(alice_set))
```

produces the output:

```python
30389 3433
```

The first number is the *total* number of words in the book, which is roughly one order of magnitude larger than the number of *unique* words. 

When converting a list into a set, all duplicates are removed. This is useful in any situation when a list needs to be de-duped and is achieved with the idiomatic statement `l = list(set(l))`.

# Excercise 10

> Do the same with the list of words from *Nils Holgersson’s Wonderful Journey Across Sweden*.
>
> You should now have two sets: 
> * The set of words from *Alice in Wonderland*. 
> * The set of words from *Nils Holgersson’s Wonderful Journey*. 
>
> You can call those two sets
> `nils_words_set` and `alice_words_set`

Printing the lengths:

```python
nils_words_set = set(nils_words)
print(len(nils_words), len(nils_words_set))
```

producing the output:

```python
156412 9756
```

# Excercise 11

> Compare the size of the sets of words of the two books: Which book uses more words?

*Nils Holgersson’s Wonderful Journey Across Sweden* contains roughly three times as many words as *Alice in Wonderland*.

# Excercise 12

> Use a **set difference** to get the set of words that are in *Alice’s Adventures in Wonderland*, 
> but not in *Nils Holgersson’s Wonderful Journey Across Sweden*. Use the difference
> method to compute the difference between the two sets of words.

Operator overloading allow set operations by using standard `-` (minus) to compute the difference:

```python
alice_words_only = alice_words_set - nils_words_set
```

# Excercise 13

> Use the function `count_only` to recover the word frequency information in the set of words unique to *Alice in Wonderland*. 
> 
> You can call the result `alice_only_counts`.

```python
alice_only_counts = count_only(alice_words, alice_words_only)
```

# Excercise 14

> Use the function `sorted_hist` to print the **20** words that are most common in, *and* uniqe to, *Alice’s Adventures in Wonderland*. 
>
> Do you see something that seems to capture’s the specifics of the book? How many times is the word *“queen”* mentioned?

The top 20 most frequent words in Alice but not in Nils can be found by:

```python
alice_only_top20 = sorted_hist(alice_only_counts)[:20]
for pair in alice_only_top20:
    print(*pair)
```

producing the following output:

```
391 alice
72 queen
59 mock
58 turtle
55 hatter
55 gryphon
44 rabbit
41 duchess
39 dormouse
38 mouse
30 caterpillar
28 illustration
18 soup
18 alice's
17 jury
13 dodo
12 sidenote
12 pigeon
12 dinah
12 chapter
```

Many of the most frequent and uniqe words are related to fictional characters or creatures, like Hatter, Gryphon (Griffin), Dodo, Mock Turtle etc. One can also deduce that the book probably has 12 chapters. The word *queen* appears no less than **72** times