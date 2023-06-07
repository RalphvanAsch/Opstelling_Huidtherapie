
from src.Base_interface import *

def startup_basic_test():
    """
    Test de startup functie
    """
    gui = Base_interface()
    gui.mainloop()

    return True


if __name__ == "__main__":
    startup_basic_test()