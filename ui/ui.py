from typing import NoReturn
from os import sys

from ciphers import rot13, rot47, untils
from extras import utilities


class EncryptionProgram:

    def __init__(self) -> NoReturn:
        self.mode_on = True

    def show_menu(self) -> NoReturn:
        while self.mode_on:
            encrypt_or_decrypt = input("""
MENU
Wybierz jedną z opcji: 
1 - Zaszyfruj tekst
2 - Odszyfruj tekst
""")
            utilities.clear_screen()
            print()
            if encrypt_or_decrypt == "1":
                encrypt = True
                plain_text = input("Podaj tekst do zaszyfrowania:\n")
            elif encrypt_or_decrypt == "2":
                encrypt = False
                plain_text = input("Podaj tekst do odszyfrowania:\n")
            else:
                print("Niepoprawny wybór")
                continue

            utilities.clear_screen()
            cipher = input("""
Wybierz szyfr:
1 - ROT13
2 - ROT47
""")
            if cipher == "1":
                cipher = "ROT13"
                cipher_text = rot13.Rot13(plain_text).use_cipher()
            elif cipher == "2":
                cipher = "ROT47"
                cipher_text = rot47.Rot47(plain_text).use_cipher()
            else:
                print("Niepoprawny wybór")
                continue

            utilities.clear_screen()
            print()
            untils.show_result(encrypt, cipher_text)
            untils.save_to_file(plain_text, cipher, cipher_text)

            user_choice = input("""
Co dalej?
1 - Powrót do MENU
2 - Zamknij program            
""")
            if user_choice == "1":
                utilities.clear_screen()
                continue
            elif user_choice == "2":
                sys.exit()
