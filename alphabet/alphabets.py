import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__), 
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

class Alphabet:
    # класс создающий словари для шифров
    # символы расскладок
    symb_ru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    symb_eu = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    signs = ",./?\|!@#$%^&*()- _=+`~"


    def __init__(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3


    # создание полного списка символов
    def symbols(self):
        symb = []
        if self.b1 == "yes":
            symb += self.symb_ru
        if self.b2 == "yes":
            symb += self.symb_eu
        if self.b3 == "yes":
            symb += self.signs
            
        return symb
    

    # словари для символов 
    symb_num = {}
    num_symb = {}


    # словарь символ_цифра
    def sn(self):
        x = 0
        for i in self.symbols():
            self.symb_num[i] = x
            x += 1

        return self.symb_num


    # словарь цифра_символ 
    def ns(self):
        x = 0
        for i in self.symbols():
            self.num_symb[x] = i
            x += 1

        return self.num_symb
    