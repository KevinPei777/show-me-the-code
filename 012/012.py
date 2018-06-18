def get_input(input_string):
    with open('filtered_words.txt') as text:
        sensitive_words = text.readlines()
        replace_sign = 0

        for word in sensitive_words:
            word = word.replace('\n', '')
            if word in input_string:
                input_string = input_string.replace(word, '*' * len(word))
                replace_sign += 1
        if replace_sign:
            return print(input_string)
        return print('Human Rights')


string = input('Please input your idea!\n')
get_input(string)
