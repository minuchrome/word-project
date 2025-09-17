import os
import json

words_path = "data/words.json"
class WordManager:
    def __init__(self):
        self.load_data()

    def init_data(self):
        return {
            "words": []
        }

    def load_data(self):
        if not os.path.exists(words_path):
            with open(words_path, "w", encoding="utf-8") as f:
                data = self.init_data()
                json.dump(data, f)
                self.data = data
        else:
            with open(words_path, encoding="utf-8") as f:
                data = json.load(f)
                self.data = data
    
    def save_data(self):
        with open(words_path, "w", encoding="utf-8") as f:
            json.dump(self.data, f)

    def get_words(self):
        return self.data["words"]
    
    def add_word(self, word):
        if "words" not in self.data:
            self.data = self.init_data()
        self.data["words"].append(word)
        self.save_data()

    def remove_word(self, index):
        if "words" not in self.data:
            return
        if not (0 <= index < len(self.words["words"])):
            return
        self.words["words"].pop(index)