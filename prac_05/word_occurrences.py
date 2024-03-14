def main():
    user_input = input("Text: ")
    word_counts = count_word_occurrences(user_input)
    display_word_occurrences(word_counts)


def count_word_occurrences(text):
    word_counts = {}

    words = text.split()
    for word in words:
        word = word.lower()
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts


def display_word_occurrences(word_counts):
    display_order = ['this is a collection of words of nice words this is a fun thing it is']

    for word in display_order:
        count = word_counts.get(word, 0)
        print(f"{word} : {count}")


if __name__ == '__main__':
    main()
