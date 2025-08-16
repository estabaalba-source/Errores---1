import csv
from pathlib import Path
from datetime import datetime

DATA_PATH = Path("datos/ventas.csv")  # se espera: fecha,categoria,producto,precio,cantidad

def leer_csv(ruta: Path) -> list[dict]:
    # Usar with para abrir/leer el archivo de forma segura
    with open(ruta, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]

def normalizar_fecha(fila: dict) -> dict:
    fila["fecha"] = datetime.strptime(fila["fecha"], "%Y-%m-%d")
    return fila

def limpiar_filas(filas: list[dict]) -> list[dict]:
    limpias = []
    vistos = set()

    for fila in filas:
        # Validar que exista categoría y no esté vacía
        if not fila.get("categoria"):
            continue

        # Usar también la fecha como parte de clave para evitar eliminar ventas distintas del mismo producto
        clave = (fila["producto"].strip().lower(), fila["fecha"])

        if clave in vistos:
            continue

        vistos.add(clave)

        # Convertir tipos solo si están presentes
        try:
            fila["precio"] = float(fila["precio"])
            fila["cantidad"] = int(fila["cantidad"])
        except (ValueError, TypeError):
            continue

        limpias.append(normalizar_fecha(fila))

    return limpias

def ingresos_por_categoria(filas: list[dict]) -> dict[str, float]:
    totales = {}
    for fila in filas:
        cat = fila.get("categoria")
        if cat not in totales:
            totales[cat] = 0.0
        totales[cat] += fila["precio"] * fila["cantidad"]
    return totales

def main():
    if not DATA_PATH.exists():
        print("No se encontró el archivo de datos.")
        return

    filas = leer_csv(DATA_PATH)
    filas_limpias = limpiar_filas(filas)
    totales = ingresos_por_categoria(filas_limpias)

    # Mostrar totales ordenados (mayor a menor)
    for cat, total in sorted(totales.items(), key=lambda x: x[1], reverse=True):
        print(f"{cat}: {round(total, 2)}")

if __name__ == "__main__":
    main()
