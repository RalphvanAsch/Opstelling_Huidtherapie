
from Hardware import *

# Tets als functies schrijven pls en de functies uitvoeren in __main__

def dit_is_een_test(invoer: str) -> bool:
    """
    Dit is een test functie
    """
    return True if type(invoer) == str else False # ik heb aangegeven dat dit een string is en een bool wordt

if __name__ == "__main__":
    out = dit_is_een_test("Hier testen") # Ik verwacht true te krijgen als de test goed gaat
    print(out) # print de uitkomst van de test