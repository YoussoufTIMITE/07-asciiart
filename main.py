
"""
Module principal pour l'encodage ASCII Art.
Contient les fonctions artcode_i (itératif), artcode_r (récursif) et main().
"""


#### Fonctions secondaires


def artcode_i(s):
    """
    Retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme itératif.
    Args:
        s (str): la chaîne de caractères à encoder
    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if not s:
        return []
    chars = [s[0]]
    occs = [1]
    for k in range(1, len(s)):
        if s[k] == s[k-1]:
            occs[-1] += 1
        else:
            chars.append(s[k])
            occs.append(1)
    return list(zip(chars, occs))


def artcode_r(s):
    """
    Retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme récursif.
    Args:
        s (str): la chaîne de caractères à encoder
    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if not s:
        return []
    first = s[0]
    count = 1
    while count < len(s) and s[count] == first:
        count += 1
    return [(first, count)] + artcode_r(s[count:])
    

#### Fonction principale


def main():
    """
    Fonction principale pour tester l'encodage ASCII Art.
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
