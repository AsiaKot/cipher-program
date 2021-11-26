from typing import NoReturn


def show_result(encrypt, text: str) -> NoReturn:
    """
    Prints encrypted/decrypted text.
    :param encrypt: True if text is encrypted, False if decrypted
    :type: bool
    :param text: text encrypted/decrypted with cipher or False (if text contains forbidden chars)
    :type text: str of False
    :return: NoReturn
    """
    if text:
        if encrypt is True:
            print(f"Twój zaszyfrowany tekst to:\n"
                  f"{text}\n")
        else:
            print(f"Twój odszyfrowany tekst to:\n"
                  f"{text}\n")


def save_to_file(plain_text: str, cipher: str, cipher_text: str) -> NoReturn:
    """
    Saves text before and after encryption/decryption to file. File is appended each time.
    :param plain_text: text encrypted with ROT13/ROT47 cipher
    :type plain_text: str
    :param cipher: used cipher (ROT13/ROT47)
    :type plain_text: str
    :param cipher_text: text decrypted with ROT13/ROT47 cipher or False (if text contains forbidden chars)
    :type cipher_text: str or False
    :return: NoReturn
    """
    if cipher_text:
        print("Zapisuję Twój tekst do pliku")
        with open("encrypted_texts.txt", "a+", encoding="UTF-8") as file:
            file.writelines(plain_text + " > " + cipher + " > " + cipher_text + "\n")