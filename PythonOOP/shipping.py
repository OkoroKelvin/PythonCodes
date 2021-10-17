from urllib.request import urlopen


def fetch_words():
    story = urlopen('https://sixty-north.com/c/t.txt')
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_words(story_words):
    for word in story_words:
        print(word)


# def main():


if __name__ == '__main__':
    my_love = fetch_words()
    print_words(my_love)
