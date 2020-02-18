from collections import Counter

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def lowercase_remove_punctuation():
    test_sentence = input("Input test")
    lowercase_string = test_sentence
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    for word in lowercase_string:
        if word in punctuations:
            lowercase_string = lowercase_string.replace(word, "").lower()
# working
    print('lowercase string: ')
    print(lowercase_string)

    split_string = lowercase_string.split(" ")
# working
    print('Split String: ')
    print(split_string)

    new_words = []

    for word in split_string:
        if word not in STOP_WORDS:
            without_stop_words = new_words.append(word)

    # for stop_word in split_string:
    #     if stop_word in STOP_WORDS:
    #         without_stop_words = split_string.remove(stop_word)

# not quite working! (was working previously)
    print('without stop words :')
    print(without_stop_words)

    # word_dict = {}

    # for instance in without_stop_words:
    #     if instance not in word_dict:
    #         word_dict[instance] += 1
    #     else:
    #         word_dict[instance] = 1

    # counted_list = {}

    # counted_list = Counter(without_stop_words)

    # print('countedlist: ')
    # print(counted_list)


#         word_dict[word] = len(instance)
#         # print(f'{word} : '{count}')
#     print(word_dict)
lowercase_remove_punctuation()
