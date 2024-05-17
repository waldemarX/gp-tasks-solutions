def read_words_from_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        words = file.read().split()
    return words


def combine_words(word1, word2):
    max_overlap = 0
    for i in range(1, min(len(word1), len(word2)) + 1):
        if word1[-i:] == word2[:i]:
            max_overlap = i
    combined_word = word1 + word2[max_overlap:]
    return combined_word


def generate_combined_words(base_word, words_list):
    combined_words = [
        combine_words(base_word, other_word)
        for other_word in words_list
        if other_word != base_word
    ]
    return combined_words


def main():
    filename = "words.txt"
    words_list = read_words_from_file(filename)
    first_word = input("Word: ").strip()
    new_words = generate_combined_words(first_word, words_list)

    for word in new_words:
        print(word)


if __name__ == "__main__":
    main()
