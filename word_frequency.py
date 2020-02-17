# STOP_WORDS = [
#     'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
#     'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
#     'will', 'with'
# ]


# def print_word_freq(file):
#     """Read in `file` and print out the frequency of words in that file."""
#     pass


# if __name__ == "__main__":
#     import argparse
#     from pathlib import Path

#     parser = argparse.ArgumentParser(
#         description='Get the word frequency in a text file.')
#     parser.add_argument('file', help='file to read')
#     args = parser.parse_args()

#     file = Path(args.file)
#     if file.is_file():
#         print_word_freq(file)
#     else:
#         print(f"{file} does not exist!")
#         exit(1)


# string = "This is the longest time I've ever been a racoon named 'Rocky'"

# print(string.lower())

# for word in words:
#     string[0].lower()


# def parse_files(*args)


# for word in words:
#     print((word))


# Python Program - Remove Punctuations from String

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def lowercase_remove_punctuation():
    test_sentence = input("Input test")
    lowercase_string = test_sentence
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    for word in test_sentence:
        if word in punctuations:
            lowercase_string = lowercase_string.replace(word, "").lower()

    print(lowercase_string)
    split_string = lowercase_string.split(" ")

    print(split_string)

    for stop_word in split_string:
        if stop_word in STOP_WORDS:
            split_string.remove(stop_word)

    print(split_string)

    for word in list:
        return word + " | " + len(word)


lowercase_remove_punctuation()

# then join
