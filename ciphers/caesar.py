# Шифр Цезаря

import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__), 
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from alphabet.alphabets import Alphabet

class Caesars_cipher:
    # класс для шифра Цезаря

    code_text = []

    def __init__(self, text, sim):
        self.text = text
        self.sim = sim

    def en_caesar(self, sn, ns):
        if self.sim == "yes":
            for i in self.text:
                if i in Alphabet.signs:
                    self.code_text += i
                else:
                    self.code_text += ns[int(int((sn[i]+3)) % len(sn))]
        else:
            for i in self.text:
                self.code_text += ns[int(int((sn[i]+3)) % len(sn))]

        print(''.join(self.code_text))

    def dec_caesar(self, ns, sn):
        if self.sim == "yes":
            for i in self.text:
                if i in Alphabet.signs:
                    self.code_text += i
                else:
                    self.code_text += ns[int(int((sn[i]-3)) % len(sn))]
        else:
            for i in self.text:
                self.code_text += ns[int(int((sn[i]-3)) % len(sn))]

        print(''.join(self.code_text))
