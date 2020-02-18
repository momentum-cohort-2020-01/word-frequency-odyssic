from collections import Counter

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def open_file(file):
    with open(file) as file:
        open_file = file.read()
        print(type(open_file))

    return open_file

    print(open_file)


def print_word_freq(file):

    lowercase_remove_punctuation(open_file(file))


def lowercase_remove_punctuation(open_file):

    lowercase_string = open_file
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
    #         without_stop_words = split_string.replace(stop_word, '')

    print('without stop words :')
    print(without_stop_words)


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
