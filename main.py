from alphabet.alphabets import Alphabet
from ciphers.caesar import Caesars_cipher

em = Alphabet("yes", "", "yes")
en = Caesars_cipher("", "yes")

ns = em.ns()
ssn = em.sn()

print(len(ssn))

en.dec_caesar(ns, ssn)

print(Alphabet.signs)
