from googletrans import Translator

def translate_word(word, target_lang="ar"):
    translator = Translator()
    translation = translator.translate(word, dest=target_lang)
    print(f"Original: {word} ({translation.src}) → Translated: {translation.text} ({target_lang})")

if __name__ == "__main__":
    word = input("Enter a word to translate: ")
    translate_word(word)
