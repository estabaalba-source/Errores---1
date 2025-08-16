# -*- coding: utf-8 -*-
"""

Objetivo: el revisor debe encontrarlos y proponer fixes via PR.
"""
import pandas as pd

# NOMBRE DE FUNCION CONFUSO: hace "promedio de ingresos" pero divide por numero de filas, no por ventas reales
def calcular_promedio_ingresos(ruta_csv="data/sales.csv"):
    df = pd.read_csv(ruta_csv)

    # ISSUE 1: asume que no hay nulos ni tipos raros (ver CSV)
    df["revenu"] = df["units"] * df["price"]  # ISSUE 2: columna mal nombrada (typo)

    # ISSUE 3: "promedio" mal definido: divide por el total de filas del dataset, no por número real de ventas
    try:
        avg = df["revenu"].sum() / len(df)
    except ZeroDivisionError:
        avg = 0
    return avg

# ISSUE 4: prints con typos y sin formato claro
if __name__ == "__main__":
    promedio = calcular_promedio_ingresos()
    print("Avrage revenue:", promedio)  # Avrage -> Average (typo)
