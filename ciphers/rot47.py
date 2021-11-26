from typing import List, Union, NoReturn


class Rot47:

    def __init__(self, text: str) -> NoReturn:
        self.text = text

    def use_cipher(self) -> Union[str,]:  # jak nazwać 2gi typ pliku w Union: "False"? bo funkcja może zwrócić też False
        """
        Encrypt/decrypt text with ROT47 cipher that replaces any ASCII character in the range 33-126
        with a character 47 positions further up to but not more than 126 positions.
        :return: cipher_text or False (if text contains forbidden chars)
        :rtype: str or False
        """
        text_to_cipher: List[str] = list(self.text)
        cipher_chars: List[str] = []
        for char in text_to_cipher:
            if char == " ":
                cipher_chars.append(char)
            else:
                ascii_dec = ord(char)
                if ascii_dec in range(33, 80):
                    cipher_letter = chr(ascii_dec + 47)
                    cipher_chars.append(cipher_letter)
                elif ascii_dec in range(80, 127):
                    cipher_letter = chr(ascii_dec - 47)
                    cipher_chars.append(cipher_letter)
                else:
                    print("Zastosowano niedozwolony znak")
                    return False

        cipher_text: str = "".join(cipher_chars)
        return cipher_text
