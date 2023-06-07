
from time import sleep
from typing import Tuple

import numpy as np
import matplotlib.pyplot as plt
import os
import tkinter as tk

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

# Hier iets wat voor nu data genereert om aan te leveren aan Base_interface
# Dit is een test functie
def generate_data() -> Tuple[np.ndarray, np.ndarray]:
    """
    Genereer data voor de GUI

    :return: tijd, data
    """
    # Maak een array aan van data over de tijd, sleep is om te simuleren dat het even duurt
    data = np.random.rand(100)
    sleep(1)
    # Return tijd, data
    return np.linspace(0, 1, 100), data

class Base_physics(tk.Tk):
    def __init__(self):
        super().__init__()
        # Titel boven de GUI
        self.title("Technisch interface")

        # Grootte van de GUI in px
        self.geometry("500x500")

        # Niet resizable
        self.resizable(False, False)

        # Global row counter
        self.row = 0

        # Vars
        self.measurement = None
        self.load_data = None
        self.save_data = None
        self.results = None

