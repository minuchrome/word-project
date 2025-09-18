import random 
from word_manager import WordManager

word_manager = WordManager()

def test():
    words = word_manager.get_words()
    words.sort(key=lambda x: x["att"])
    word = words[0]
    print("다음 단어의 뜻은?")
    answer = input(f"{word["word"]}: ").strip().lower()
    word["att"] += 1
    if answer == word["def"].lower():
        print("정답!")
        word["rig"] += 1
    else:
        print(f"오답! 정답은 {word["def"]}입니다.")
    word_manager.save_data()

def add():
    word_input = input("추가할 영단어를 입력하세요: ")
    def_input = input("한국어 뜻을 입력하세요: ")
    word_manager.add_word({
        "word": word_input,
        "def": def_input
    })
    print("추가되었습니다.")

def list():
    words = word_manager.get_words()
    for i, word in enumerate(words):
        acc = "시도하지 않음"
        if word["att"] > 0:
            acc = str(round(word["rig"]/word["att"])*100)+"%"
        print(f"단어 #{i}:")
        print("  "+word["word"])
        print("  "+word["def"])
        print("  "+acc)
        print("----")

def remove():
    index_input = int(input("삭제할 단어의 인덱스를 입력하세요: "))
    removed = word_manager.remove_word(index_input)
    if removed:
        print("삭제되었습니다.")

modes = {
    "test": test,
    "add": add,
    "list": list,
    "remove": remove,
}

modes_str = " | ".join(modes.keys())

while True:
    mode_input = input(f"사용할 모드를 입력하세요: ({modes_str}) ").strip()
    if mode_input in modes:
        modes[mode_input]()
    else:
        print(f"없는 모드: {mode_input}")