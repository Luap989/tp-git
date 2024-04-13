"""
Module calculator
Contains simple arithmetic functions.
"""


def addition(a, b):
    """
    Retourne la somme de deux nombres.

    Args:
        a (float): Le premier nombre.
        b (float): Le deuxième nombre.

    Returns:
        float: La somme des deux nombres.
    """
    return a + b

def subtraction(a, b):
    """
    Retourne la différence entre deux nombres.

    Args:
        a (float): Le premier nombre.
        b (float): Le deuxième nombre.

    Returns:
        float: La différence entre les deux nombres.
    """
    return a - b

def division(a, b):
    """
    Retourne le résultat de la division de a par b.

    Args:
        a (float): Le numérateur.
        b (float): Le dénominateur (ne peut pas être zéro).

    Returns:
        float: Le résultat de la division.
    """
    if b == 0:
        raise ValueError("Le dénominateur ne peut pas être zéro.")
    return a / b
