
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
    # Return tijd, data
    return np.linspace(0, 1, 100), data

class Base_physics(tk.Tk):
    def __init__(self):
        super().__init__()
        # Titel boven de GUI
        self.title("Technisch interface")

        # Grootte van de GUI in px
        self.geom = (900, 600)
        self.geometry("%sx%s" % self.geom)

        # Niet resizable
        self.resizable(False, False)

        # Global row counter
        self.row = 0
        self.rowfig = 0

        # Vars
        self.measurement = None
        self.load_data = None
        self.save_data = None
        self.results = None

        # Figsize
        self.dpi = 100
        self.figsize = (self.geom[0]/(2*self.dpi), self.geom[1]/(self.dpi))
        self.graph_topleft(generate_data())

        # Build the right side of the GUI
        self.data_box()
        self.data_box()
        self.data_box()

    def graph_topleft(self, data):
        """
        Graph in de top left corner
        """

        # Maak een figuur aan
        fig = plt.Figure(figsize=self.figsize, dpi=100)
        fig.suptitle("Test")

        # Maak een subplot aan
        ax = fig.add_subplot(111)
        # Maak een plot aan
        ax.plot(*data)
        # Maak een canvas aan
        canvas = FigureCanvasTkAgg(fig, master=self)
        # Laat de canvas zien
        canvas.draw()
        # Plaats de canvas in de GUI
        self.rowfig = 0
        canvas.get_tk_widget().grid(row=self.rowfig, column=0, sticky="NSEW", padx=10, pady=10,
                                    columnspan=3, rowspan=6)

        self.after(1000, self.update_graph, generate_data())
        return None

    def data_box(self):
        """
        Data in the top right corner
        """
        # Maak een label aan
        text_src = "Dit is een stuk text waar uitleg staat over het onderstaande"
        label = tk.Label(master=self, text=text_src)
        label.grid(row=self.row, column=4, sticky="NSEW", columnspan=3, rowspan=1)
        self.row += 1

        # Hier komt de frame met alle data
        frame_data = tk.Frame(master=self)
        # Loop door alle lables en entries heen (row, column)
        for i in range(4):
            for j in range(3):
                if i % 2 ==0:
                    # Maak een label aan
                    label = tk.Label(master=frame_data, text="Test")
                    # Plaats de label in het frame
                    label.grid(row=i, column=j, sticky="NSEW")
                else:
                    # Maak een entry aan
                    entry = tk.Entry(master=frame_data)
                    # Plaats de entry in het frame
                    entry.grid(row=i, column=j, sticky="NSEW")

        frame_data.grid(row=self.row, column=4, sticky="NSEW", columnspan=1, rowspan=1)
        self.row += 1
        return None

    def update_graph(self, data):
        self.graph_topleft(data)
