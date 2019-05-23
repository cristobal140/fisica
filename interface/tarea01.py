import tkinter as tk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def curva_de_ejemplo():
    """
    Curva de Ejemplo que despliega una curva paramétrica en una ventana nueva

    Integrantes:
    - Omar Olivares Urrutia (@ofou)
    :return: plot curve
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Prepare arrays x, y, z
    theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
    z = np.linspace(-2, 2, 100)
    r = z ** 2 + 1
    x = r * np.sin(theta)
    y = r * np.cos(theta)

    ax.plot(x, y, z, label='Curva Paramétrica de Ejemplo')
    ax.legend()

    fig.show()

    # Añadir el plot de matplotlib
    # fig = Figure(figsize=(5, 4), dpi=100)
    # t = np.arange(0, 3, .01)
    # fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))
    #
    # canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    # canvas.draw()
    # canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    #
    # toolbar = NavigationToolbar2Tk(canvas, root)
    # toolbar.update()
    # canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    # canvas.mpl_connect("key_press_event", on_key_press)

    # If you put root.destroy() here, it will cause an error if the window is
    # closed with the window manager.


def helice_conica():
    # añadir sus códigos aca

    pass
def helice_circular_1():
    # añadir sus códigos aca
    pass
def Corona_Sinusoidal():
    # añadir sus códigos aca
    pass
def curva_de_viviani():
    # añadir sus códigos aca
    pass
def hipopoda_1():
    # añadir sus códigos aca
    '''
           Integrantes:
           - Boris Gutiérrez Cornejo (@BorisAndresLmb)
           - Juan González Jélvez (@JuanGonzalez33)
           - Pablo Barrera Whiteley (@Pablobw)
           - José Flores Cáceres (@JoseFlores9)
           - Cristobal Rojas Saavedra (@cristotix)

           Función hipopoda_1: Grafica la hipopoda
           Utiliza la forma paramétrica de la función
           x= a+(r-a)*cos(t)
           y=(r-a)*sen(t)
           z=2*((a*(r-a))**1/2))*sen(t)
           Parametros:
           a= distancia del centro de la esfera al eje del cilindro
           r=Radio de la esfera
           return: plot Curve (Hipopede)
           '''

    plt.rcParams['legend.fontsize'] = 10

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Prepare arrays x, y, z
    theta = np.linspace(-4 * np.pi, 4 * np.pi, 99)
    a = 1
    r = 5
    x = a + (r - a) * np.cos(theta)
    y = (r - a) * np.sin(theta)
    z = 2 * (a * (r - a)) ** (1 / 2) * np.sin(theta / 2)
    ax.plot(x, y, z, label='parametric curve')

    ax.legend()

    plt.show()
    pass
def conica_de_papus():
    # añadir sus códigos aca
    pass
def Curva_de_Arquitas():
    # añadir sus códigos aca
    pass
def horoptera():
    # añadir sus códigos aca
    pass
def Curva_Bicilindrica():
    # añadir sus códigos aca
    pass

if __name__ == '__main__':
    # Creación de Ventanas
    root = tk.Tk()
    root.wm_title("Proyecto de Fisica 2019/01")
    root.geometry("800x600")

    # Crear frame contenedor de los elementos
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)
    # Añadir titulo
    label = tk.Label(frame, text="Curvas Paramétricas Famosas", height="2")
    label.pack(fill=tk.X, expand=1)

    # Cada grupo debe utilizar sus propia función
    curva_de_ejemplo = tk.Button(master=frame, text="Curva de Ejemplo", command=curva_de_ejemplo)
    curva_de_ejemplo.pack(side=tk.BOTTOM, padx=10, pady=10)

    curva_de_ejemplo = tk.Button(master=frame, text="Hélice Cónica", command=helice_conica)
    curva_de_ejemplo.pack(side=tk.BOTTOM, padx=10, pady=10)

    curva_de_ejemplo = tk.Button(master=frame, text="Hélice Circular", command=helice_circular_1)
    curva_de_ejemplo.pack(side=tk.BOTTOM, padx=10, pady=10)

    curva_de_ejemplo = tk.Button(master=frame, text="Corona Sinusoidal", command=Corona_Sinusoidal)
    curva_de_ejemplo.pack(side=tk.BOTTOM, padx=10, pady=10)

    curva_de_ejemplo = tk.Button(master=frame, text="Curva de Viviani", command=curva_de_ejemplo)
    curva_de_ejemplo.pack(side=tk.BOTTOM, padx=10, pady=10)

    curva_de_ejemplo = tk.Button(master=frame, text="Hipopoda", command=hipopoda_1)
    curva_de_ejemplo.pack(side=tk.BOTTOM, padx=10, pady=10)

    curva_de_ejemplo = tk.Button(master=frame, text="Curva de Arquitas", command=Curva_de_Arquitas)
    curva_de_ejemplo.pack(side=tk.BOTTOM, padx=10, pady=10)

    curva_de_ejemplo = tk.Button(master=frame, text="Curva Bicilindrica", command=Curva_Bicilindrica)
    curva_de_ejemplo.pack(side=tk.BOTTOM, padx=10, pady=10)

    curva_de_ejemplo = tk.Button(master=frame, text="Conica de Papus", command=conica_de_papus)
    curva_de_ejemplo.pack(side=tk.BOTTOM, padx=10, pady=10)

    curva_de_ejemplo = tk.Button(master=frame, text="Horoptera", command=horoptera)
    curva_de_ejemplo.pack(side=tk.BOTTOM, padx=10, pady=10)

    tk.mainloop()
