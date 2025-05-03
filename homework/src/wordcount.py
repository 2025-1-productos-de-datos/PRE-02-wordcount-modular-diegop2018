# obtain a list of files in the input directory
import os

from ._internals.Write_count_words import Write_count_words


def read_all_lines():
    all_lines = []
    input_directory_files = os.listdir("data/input/")
    for filename in input_directory_files:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
            all_lines.extend(lines)
    return all_lines


def main():
    input_directory_files = os.listdir("data/input/")
    # all_lines = read_all_lines()

    ## read files
    ## clean lines
    ## split lines into words
    ## count the frequency of the words in the files in the input directory
    ## write the results to a file in the output directory

    # count the frequency of the words in the files in the input directory
    counter = {}
    for filename in input_directory_files:
        with open("data/input/" + filename) as f:
            for l in f:
                for w in l.split():
                    w = w.lower().strip(",.!?")
                    counter[w] = counter.get(w, 0) + 1

    # create the directory output/ if it doesn't exist
    Write_count_words(counter)


if __name__ == "__main__":
    main()
