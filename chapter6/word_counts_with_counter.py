from collections import Counter

text = ('this is sample text with several words '
        'this is more sample text with some different words')
counter = Counter(text.split())
for word, count in sorted(counter.items()):
    print(f'{word:<7}{count}')
    