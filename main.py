def encrypt(text, shift, alphabet):
    result = ""
    for char in text:
        if char in alphabet:
            index = alphabet.find(char)
            result += alphabet[(index + shift) % len(alphabet)]
        else:
            result += char
    return result


def decrypt(text, shift, alphabet):
    result = ""
    for char in text:
        if char in alphabet:
            index = alphabet.find(char)
            result += alphabet[(index - shift) % len(alphabet)]
        else:
            result += char
    return result


def read_input_file(file_name):
    result = ""
    with open(file_name, "r", encoding="utf-8") as f:
        while True:
            line = f.readline()
            if not line:
                break
            result += line
    return result


def main():
    shift = 16
    uk_alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    en_alphabet = "abcdefghijklmnopqrstuvwxyz ,.!?;:"
    ua_text = read_input_file("input_ua.txt")
    en_text = read_input_file("input_en.txt")
    print("Оригінальний текст з файлу українською:")
    print(ua_text)
    ua_text = encrypt(ua_text, shift, uk_alphabet)
    print("\nЗашифрований текст українською:")
    print(ua_text)
    ua_text = decrypt(ua_text, shift, uk_alphabet)
    print("\nДешифрований текст українською:")
    print(ua_text)

    print("\nОригінальний текст з файлу англійською:")
    print(en_text)
    en_text = encrypt(en_text, shift, en_alphabet)
    print("\nЗашифрований текст англійською:")
    print(en_text)
    en_text = decrypt(en_text, shift, en_alphabet)
    print("\nДешифрований текст англійською:")
    print(en_text)


if __name__ == '__main__':
    main()