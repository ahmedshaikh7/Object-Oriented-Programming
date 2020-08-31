from typing import List


class Definition:
    def __init__(self, definition: str, part_of_speech: str):
        self.definition = definition
        self.part_of_speech = part_of_speech


    def __repr__(self):
        s = self.part_of_speech.upper()
        s += ". "
        s += self.definition

        return s


class Entry:
    def __init__(self, word: str, definitions: List[Definition]):
        #implement
        self.word = word
        self.definitions = definitions

    def __repr__(self):
        i = 1
        s = self.word
        s += ":\n"

        for item in self.definitions:
            s += "{}. {}\n".format(i, str(item))
            i += 1

        return s
