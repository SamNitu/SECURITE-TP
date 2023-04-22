# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 22:06:26 2023

@author: EJEUNA1
"""

def permutation(cle, perm):
    if len(cle) != len(perm) :
        return -1
    
    clePermute = ""
    for car in perm:
        index = int(car)
        clePermute = clePermute + cle[index]
        
    
    return clePermute


def ouExclusive(cle1, cle2):
    if len(cle1) != len(cle2):
        return -1
    
    result = ""
    
    for i in range(0, len(cle1)):
        if (cle1[i] == "0" and cle2[i] == "0") or (cle1[i] == "1" and cle2[i] == "1"):
            result = result + "0"
        else:
            result = result + "1"
            
    
    return result

def ouInclusive(cle1, cle2):
    if len(cle1) != len(cle2):
        return -1
    
    result = ""
    
    for i in range(0, len(cle1)):
        if (cle1[i] == "0" and cle2[i] == "0"):
            result = result + "0"
        else:
            result = result + "1"
            
    
    return result


def etLogique(cle1, cle2):
    if len(cle1) != len(cle2):
        return -1;
    
    result = ""
    
    for i in range(0, len(cle1)):
        if (cle1[i] == "1" and cle2[i] == "1"):
            result = result + "1"
        else:
            result = result + "0"
            
    
    return result


def decalageGauche(cle, ordre):
    decal = cle[0:ordre]
    reste = cle[ordre:len(cle)]
    
    return reste + decal


def decalageDroit(cle, ordre):
    taille = len(cle)
    diff = taille - ordre
    
    decal = cle[diff:taille]
    reste = cle[0:diff]
    
    return decal + reste

def inversePermutation(fonctionPermutation):
    result = ""
    i = 0
    
    for i in range(0, len(fonctionPermutation)):
        result = result + str(fonctionPermutation.index(str(i), 0, len(fonctionPermutation)))
        
    return result


def GenerationDesCles(cle, fonctionPermutation):
    clePermute = permutation(cle, fonctionPermutation)
    k1_ = clePermute[0:len(clePermute)//2]
    k2_ = clePermute[len(clePermute)//2:len(clePermute)]
    
    global k1
    k1 = ouExclusive(k1_, k2_)
    global k2
    k2 = etLogique(k2_, k1_)
    
    k1 = decalageGauche(k1, 2)
    k2 = decalageDroit(k2, 1)
    
    return "Clés Générés : (" + k1 + ", " + k2 + ")"

print(GenerationDesCles("01101101", "65274130"))

def chiffrement(n, pi, p, k1, k2):
    clePermute = permutation(n, pi)
    G0 = clePermute[0:len(clePermute)//2]
    D0 = clePermute[len(clePermute)//2:len(clePermute)]
    
  
    
    D1 = ouExclusive(permutation(G0, p), k1)
    G1 = ouExclusive(D0, ouInclusive(G0, k1))
    
    D2 = ouExclusive(permutation(G1, p), k2)
    G2 = ouExclusive(D1, ouInclusive(G1, k2))
    
    C = G2 + D2
    
    pi_1 = inversePermutation(pi)
    
    result = permutation(C, pi_1)
    global valeurCrypte
    valeurCrypte = result
    
    return "Valuer à crypter " + n +" --> " + valeurCrypte + " Valeur Cryptée"

print(chiffrement('01101110', '46027315', '2013', k1, k2))

def dechiffrement(n, pi, p, k1, k2):
    clePermute = permutation(n, pi)
    G2 = clePermute[0:len(clePermute)//2]
    D2 = clePermute[len(clePermute)//2:len(clePermute)]
    
    inv_p = inversePermutation(p)
    
    G1 =  permutation(ouExclusive(D2, k2), inv_p)
    D1 = ouExclusive(G2, ouInclusive(G1, k2))
    
    G0 = permutation(ouExclusive(D1, k1), inv_p)
    D0 = ouExclusive(G1, ouInclusive(G0, k1))
    
    N = G0 + D0
    
    inv_pi = inversePermutation(pi)
    
    result = permutation(N, inv_pi)
    
    return "Valeur Decryptée : " + result

print(dechiffrement(valeurCrypte, '46027315', '2013', k1, k2))