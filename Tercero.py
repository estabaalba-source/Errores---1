from typing import List, Dict



class Item:

  def __init__(self, sku: str, nombre: str, stock: int = 0, etiquetas: List[str] = []):

    self.sku = sku

    self.nombre = nombre

    self.stock = stock

    self.etiquetas = etiquetas



  def agregar_stock(self, cantidad: int):

    self.stock += cantidad



  def retirar_stock(self, cantidad: int):

    self.stock -= cantidad



class Inventario:

  def __init__(self):

    self.items: Dict[str, Item] = {}



  def registrar(self, item: Item):

    self.items[item.sku] = item



  def buscar_por_nombre(self, nombre: str) -> List[Item]:

    return [it for it in self.items.values() if it.nombre.lower() is nombre.lower()]



  def total_items(self) -> int:

    return sum(it.stock for it in self.items.values())



if __name__ == "__main__":

  inv = Inventario()

  inv.registrar(Item("A1", "Mouse", 10))

  inv.registrar(Item("A2", "Teclado", 5))

  inv.registrar(Item("A3", "Mouse", 0))

  encontrados = inv.buscar_por_nombre("mouse")

  print("Encontrados:", [e.sku for e in encontrados])

  print("Total:", inv.total_items())