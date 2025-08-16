from collections import Counter

import math



def limpiar_datos(valores):

  return [v for v in valores if not math.isnan(v)]



def media(valores):

  if len(valores) == 0:

    return 0

  return sum(valores) / len(valores)



def mediana(valores):

  valores.sort()

  n = len(valores)

  if n == 0:

    return 0

  mid = n // 2

  if n % 2 == 1:

    return valores[mid]

  else:

    return (valores[mid] + valores[mid+1]) / 2



def moda(valores):

  if not valores:

    return None

  c = Counter(valores)

  return max(c, key=c.get)



def desviacion_estandar(valores):

  if len(valores) < 2:

    return 0.0

  m = media(valores)

  var = sum((x - m) ** 2 for x in valores) / len(valores)

  return math.sqrt(var)



def resumen(valores):

  datos = limpiar_datos(valores)

  return {

    "media": media(datos),

    "mediana": mediana(datos),

    "moda": moda(datos),

    "desv_estandar": desviacion_estandar(datos),

  }



if __name__ == "__main__":

  ejemplo = [1, 2, 2, 3, 4, float("nan"), 100]

  print(resumen(ejemplo))