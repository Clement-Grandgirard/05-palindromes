#### Fonction secondaire
"""Vérifie si une chaîne est un palindrome."""
import string


def ispalindrome(p):
    """Retourne True si p est un palindrome."""
    table_punctuation = str.maketrans('', '', string.punctuation)
    table_accent = str.maketrans("àâäçéèêëîïôöùûüÿ", "aaaceeeeiioouuuy")
    p = p.replace(" ","").lower().translate(table_punctuation).translate(table_accent)
    if len(p)%2 == 0:
        for i in range(len(p)//2):
            if p[i]!=p[len(p)-i-1]:
                return False
    else:
        for i in range(len(p)//2):
            if p[i]!=p[len(p)-i-1]:
                return False
    return True

#### Fonction principale


def main():
    """Teste la fonction ispalindrome sur plusieurs mots."""
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
