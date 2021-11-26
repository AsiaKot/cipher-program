from typing import List, Union, NoReturn


class Rot13:
    special_chars: List[str] = [" ", ",", ".", "!", "?", ":", ";", "-", "_", "+",
                                "(", ")", "|", "^", "@", "#", "%", "&", "*", "/",
                                "<", ">", "{", "}", "=", "'", "\"", "\\",
                                "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    def __init__(self, text: str) -> NoReturn:
        self.text = text

    def use_cipher(self) -> Union[str,]: # jak nazwać 2gi typ pliku w Union: "False"? bo funkcja może zwrócić też False
        """
        Encrypt/decrypt text with ROT13 cipher that replaces a letter
        with the 13th letter after it in the alphabet.
        :return: cipher_text or False (if text contains forbidden chars)
        :rtype: str or False
        """
        text_to_cipher: List[str] = list(self.text)
        cipher_chars: List[str] = []
        for char in text_to_cipher:
            if char in self.special_chars:
                cipher_chars.append(char)
            else:
                ascii_dec = ord(char)
                if ascii_dec in range(65, 78) or ascii_dec in range(97, 110):
                    cipher_letter = chr(ascii_dec + 13)
                    cipher_chars.append(cipher_letter)
                elif ascii_dec in range(78, 91) or ascii_dec in range(110, 123):
                    cipher_letter = chr(ascii_dec - 13)
                    cipher_chars.append(cipher_letter)
                else:
                    print("Zastosowano niedozwolony znak")
                    return False

        cipher_text: str = "".join(cipher_chars)
        return cipher_text
