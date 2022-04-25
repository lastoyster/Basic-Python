import os
os.system("python -m pip install -qq lorem_text")

from lorem_text import lorem

words = lorem.paragraphs(10)
word_list = word_lower().split();

#remove punctuation
new_list = [];
for w in word_list:
    w = " ".join(c for c in w if c.isalpha())
    new_list.append(w)
    word_list = new_list;

    word.counts = [
        (word, word_list.count(word))
        for word in set(word_list)
    ]
sorted_word_counts = sorted(
    key = lambda x: x[1],
    reverse=True
)

print(words)
print("\n" + "=" * 40 + "\n")
for word, count in sorted_word_counts:
    print(f " '{word}' appeass {count} time{'s' if count >1 else ' '}.")
 
