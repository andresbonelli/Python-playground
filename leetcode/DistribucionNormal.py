import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from decorators.Decorators import leetcode_test
from typing import List

@leetcode_test
def calcular_distribucion_normal(numbers: List[int], xlabel: str, ylabel: str):
    """

    :param numbers: (list of int) lista de valores numéricos
    :param xlabel: (str) etiqueta de los valores
    :param ylabel: (str) etiqueta de la densidad por cada valor
    :return: None
    """
    # Creating a DataFrame from array
    df = pd.DataFrame(numbers)

    # Calculating mean and standard deviation using pandas
    mean = df.mean().values[0]
    std_dev = df.std().values[0]

    # Plotting histogram
    plt.hist(numbers, bins=10, density=True, alpha=0.5, color='grey')

    # Plotting the PDF
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mean, std_dev)
    plt.plot(x, p, 'k', linewidth=2)
    plt.title(f'Distribucion Normal\n'
              f'Promedio: {round(mean)}, Desviacion: {round(std_dev)}')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

if __name__ == "__main__":

    # Age data
    edades = [36, 26, 40, 24, 20, 35, 58, 26, 28, 38, 36, 18, 26, 22, 22, 33,
              39, 29, 54, 26, 43, 20, 39, 40, 20, 25, 40, 26, 22, 32, 62, 34,
              24, 23, 35, 24, 26, 35, 43, 55, 63, 24, 38, 56, 54, 36, 43]

    calcular_distribucion_normal(edades, xlabel="Edad", ylabel="Densidad")

