from alphabet.alphabets import Alphabet
from ciphers.caesar import Caesars_cipher
from ciphers.Vigener import vigener
from ciphers.Athena import Athena

em = Alphabet("yes", "", "")
en = Caesars_cipher("саша шёл по лесу", "yes")
ec = vigener("юари ёёш пж фтса", "машина", "yes")


ns = em.ns()
sn = em.sn()
symb = em.symbols()
at = Athena("НЧЯЁ ЙьцПЭ егНьцЁкю иЙПУЧЯ ЙгХНмргЯ", 2, 6, ns, symb)

print(at.dec_alphabet())

