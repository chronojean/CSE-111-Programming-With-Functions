from random_word import RandomWords

r = RandomWords()

words = []

for _ in range(100):
    word = r.get_random_word()
    words.append(word)

print(words)