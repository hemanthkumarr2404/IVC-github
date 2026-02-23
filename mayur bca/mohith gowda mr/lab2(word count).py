def count_words(sentence: str) -> int:
    words = sentence.split()
    return len(words)
sentence = str(input("Enter the sentence: "))
print("Number of words:", count_words(sentence))
