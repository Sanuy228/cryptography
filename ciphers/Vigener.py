# Шифр Виженера

import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__), 
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from alphabet.alphabets import Alphabet

class vigener:
    # класс для шифра Виженера

    code_text = []

    def __init__(self, text, text_ciphers, sim):
        self.text = text
        self.text_ciphers = text_ciphers
        self.sim = sim

    def en_caesar(self, sn, ns):
        x = 0
        if self.sim == "yes":
            for i in self.text:
                if i in Alphabet.signs:
                    self.code_text += i
                else:
                    self.code_text += ns[ (int(int(sn[i]) + int(sn[self.text_ciphers[x % len(self.text_ciphers)]]))) % len(ns)] 
                    x += 1
                    
        else:
            for i in self.text:
                self.code_text += ns[ (int(int(sn[i]) + int(sn[self.text_ciphers[x % len(self.text_ciphers)]]) + 1)) % len(ns)]
                x += 1

        return self.code_text

    def dec_caesar(self, sn, ns):
        x = 0
        if self.sim == "yes":
            for i in self.text:
                if i in Alphabet.signs:
                    self.code_text += i
                else:
                    self.code_text += ns[ (int(int(sn[i]) - int(sn[self.text_ciphers[x % len(self.text_ciphers)]]))) % len(ns)] 
                    x += 1
                    
        else:
            for i in self.text:
                self.code_text += ns[ (int(int(sn[i]) - int(sn[self.text_ciphers[x % len(self.text_ciphers)]]) + 1)) % len(ns)]
                x += 1

        return self.code_text

