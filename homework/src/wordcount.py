# obtain a list of files in the input directory

from ._internals.count_words import count_words
from ._internals.preprocess_lines import preprocess_lines
from ._internals.read_all_lines import read_all_lines
from ._internals.split_in_words import split_in_words

from ._internals.Write_count_words import Write_count_words


def main():

    input_folder = "data/input/"
    output_folder = "data/output/"

    all_lines = read_all_lines(input_folder)
    all_lines = preprocess_lines(all_lines)
    words = split_in_words(all_lines)
    counter = count_words(words)
    Write_count_words(counter, output_folder)


if __name__ == "__main__":
    main()
