import string


def lower(text):
    return text.lower()


# replace all punctuation to ' '
def replace_punctuation(text):
    for word in text:
        if word in string.punctuation:
            text = text.replace(word, " ")
    return text


# def word_count(word_dict):
#     items = [[x, y] for (y, x) in word_dict.items()]
#     items.sort(reverse=True)


with open('article.txt', 'r') as article:
    article = article.read()
    work = lower(article)

    result = replace_punctuation(work)
    words_list = result.split()

    # text_dict:save words and rates
    text_dict = {}
    for i in words_list:
        if i in text_dict:
            text_dict[i] += 1
        else:
            text_dict[i] = 1

    print(text_dict)
