from word_manager import WordManager

word_manager = WordManager()
while True:
    word_input = input("영단어를 입력하세요: ")
    def_input = input("뜻을 입력하세요: ")
    word_manager.add_word({
        "word": word_input,
        "def": def_input
    })
    print("----------")
    print(word_manager.get_words())