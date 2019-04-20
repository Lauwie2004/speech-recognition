import random
import time


def arr():
    arr = []
    with open(r"file.txt") as f:
        for words in f:
            list = "%s" % words

        arr = words.split()

        longer_wrds = []

        for woorden in arr:
            if len(woorden) > 5:
                longer_wrds.append(woorden)
    return longer_wrds[random.randint(1, int(len(longer_wrds)))]

arr()
