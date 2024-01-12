from alphabet.alphabets import Alphabet
from ciphers.caesar import Caesars_cipher
from ciphers.Vigener import vigener

em = Alphabet("yes", "", "")
en = Caesars_cipher("саша шёл по лесу", "yes")
ec = vigener("саша шёл по лесу ываыва ываываы", "саша шёл по лесу", "yes")


ns = em.ns()
sn = em.sn()
print(ns)

ec.en_caesar(sn, ns)

