from alphabet.alphabets import Alphabet
from ciphers.caesar import Caesars_cipher
from ciphers.Vigener import vigener

em = Alphabet("yes", "", "")
en = Caesars_cipher("саша шёл по лесу", "yes")
ec = vigener("юари ёёш пж фтса", "машина", "yes")


ns = em.ns()
sn = em.sn()

ec.dec_caesar(sn, ns)

