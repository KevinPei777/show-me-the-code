def get_input(input_string):
    with open('filtered_words.txt') as text:
        sensitive_words = text.readlines()

        for word in sensitive_words:
            word = word.replace('\n', '')

            if word in input_string:
                return print('Freedom!')
        return print('Human Rights')


string = input('Please input your idea!\n')
get_input(string)
