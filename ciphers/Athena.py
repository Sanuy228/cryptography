# шифр Афины

import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__), 
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

class Athena:
    # класс для шифра Афины

    code_text = []
    let_num = {}
    let_let = {}

    def __init__(self, text, key1, key2, ns, symb):
        self.text = text
        self.key1 = key1
        self.key2 = key2
        self.symb = symb
        self.ns = ns

    def en_alphabet(self):
        x = 0
        for i in self.symb:
            self.let_num[i] = (x*self.key1+self.key2) % len(self.symb)
            x += 1
        for i in self.symb:
            self.let_let[i] = self.ns[self.let_num[i]]

        for i in self.text:
            if i == " ":
                self.code_text += " "
            else:
                self.code_text += self.let_let[i]
        
        return "".join(self.code_text)
    
    def dec_alphabet(self):
        x = 0
        for i in self.symb:
            self.let_num[i] = (x*self.key1+self.key2) % len(self.symb)
            x += 1
        for i in self.symb:
            self.let_let[self.ns[self.let_num[i]]] = i

        for i in self.text:
            if i == " ":
                self.code_text += " "
            else:
                self.code_text += self.let_let[i]
        
        return "".join(self.code_text)
    