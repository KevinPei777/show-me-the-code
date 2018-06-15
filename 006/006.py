import os
import sys
import string


def lower(text):
    return text.lower()


# replace all punctuation to ' '
def replace_punctuation(text):
    for word in text:
        if word in string.punctuation:
            text = text.replace(word, " ")
    return text


def word_count(word_dict):
    items = [[x, y] for (y, x) in word_dict.items()]
    items.sort(reverse=True)
    return items


# the current path and list of dirs
root_dir = sys.path[0]

all_files = os.listdir(root_dir)

index = all_files.index('articles')
text_dir = root_dir + '/' + all_files[index]

all_text = os.listdir(text_dir)

word_dict = {}
for text in all_text:
    with open(text_dir + '/' + text, 'r') as article:
        article = article.read()
        work = lower(article)

        result = replace_punctuation(work)
        word_list = result.split()

        # user word_dict count words
        for word in word_list:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1

final_result = word_count(word_dict)
count_list = []

# choose important word
for count in final_result:
    if count[0] >= 20:
        count_list.append('{0}:{1}'.format(count[1], count[0]))
print(count_list)
