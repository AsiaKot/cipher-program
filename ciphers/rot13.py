from typing import List, Union, NoReturn


class Rot13:

    def __init__(self, text: str) -> NoReturn:
        self.text = text

    def use_cipher(self) -> Union[str,]:  # jak nazwać 2gi typ pliku w Union: "False"? bo funkcja może zwrócić też False
        """
        Encrypt/decrypt text with ROT13 cipher that replaces a letter
        with the 13th letter after it in the alphabet.
        :return: cipher_text or False (if text contains forbidden chars)
        :rtype: str or False
        """
        text_to_cipher: List[str] = list(self.text)
        cipher_chars: List[str] = []
        for char in text_to_cipher:
            ascii_dec = ord(char)
            if ascii_dec in [*range(32, 65), *range(91, 97), *range(123, 127)]:
                cipher_letter = str(char)
            elif ascii_dec in [*range(65, 78), *range(97, 110)]:
                cipher_letter = chr(ascii_dec + 13)
            elif ascii_dec in [*range(78, 91), *range(110, 123)]:
                cipher_letter = chr(ascii_dec - 13)
            else:
                print("Zastosowano niedozwolony znak")
                return False
            cipher_chars.append(cipher_letter)

        cipher_text: str = "".join(cipher_chars)
        return cipher_text
