from typing import Any, Optional


class Stack:
    def __init__(self):
        self.__elements = []

    def push(self, value: Any) -> None:
        self.__elements.append(value)

    def pop(self) -> Optional[Any]:
        return (
            self.__elements.pop()
            if self.__elements
            else None
        )

    def size(self) -> int:
        return len(self.__elements)

    def on_top(self) -> Optional[Any]:
        return (
            self.__elements[-1]
            if self.__elements
            else None
        )

    def show(self):
        aux_stack = Stack()
        print("\n--- Contenido de la Pila (Desde la cima) ---")
        while self.size() > 0:
            value = self.pop()
            print(f"- Modelo: {value['modelo']}, Película: {value['pelicula']}, Estado: {value['estado']}")
            aux_stack.push(value)
        print("-------------------------------------------\n")
        
        while aux_stack.size() > 0:
            self.push(aux_stack.pop())


trajes_stack = Stack()

datos_trajes = [
    {"modelo": "Mark III", "pelicula": "Iron Man", "estado": "Impecable"},
    {"modelo": "Mark VI", "pelicula": "Iron Man 2", "estado": "Destruido"},
    {"modelo": "Mark XLIV", "pelicula": "Avengers: Age of Ultron", "estado": "Dañado"}, 
    {"modelo": "Mark XLVI", "pelicula": "Capitan America: Civil War", "estado": "Dañado"},
    {"modelo": "Mark XLV", "pelicula": "Avengers: Age of Ultron", "estado": "Impecable"},
    {"modelo": "Mark XLVII", "pelicula": "Spider-Man: Homecoming", "estado": "Impecable"},
    {"modelo": "Mark L", "pelicula": "Avengers: Infinity War", "estado": "Destruido"},
    {"modelo": "Mark XLVI", "pelicula": "Spider-Man: Homecoming", "estado": "Dañado"}, 
]

for traje in datos_trajes:
    trajes_stack.push(traje)

print("Pila inicial cargada con trajes de Iron Man.")
trajes_stack.show()


print("## a. Búsqueda del Mark XLIV (Hulkbuster) 🔎")

aux_stack = Stack()
peliculas_encontradas = set()
modelo_buscado = "Mark XLIV"
encontrado = False

while trajes_stack.size() > 0:
    traje = trajes_stack.pop()
    
    if traje["modelo"] == modelo_buscado:
        encontrado = True
        peliculas_encontradas.add(traje["pelicula"])
    
    aux_stack.push(traje)

while aux_stack.size() > 0:
    trajes_stack.push(aux_stack.pop())

if encontrado:
    print(f" El modelo {modelo_buscado} (Hulkbuster) FUE utilizado.")
    print(f"Aparece en las películas: {', '.join(peliculas_encontradas)}")
else:
    print(f" El modelo {modelo_buscado} (Hulkbuster) NO fue utilizado.")


print("\n## b. Modelos Dañados ")

aux_stack = Stack()
modelos_danados = []

while trajes_stack.size() > 0:
    traje = trajes_stack.pop()
    
    if traje["estado"] == "Dañado":
        modelos_danados.append(traje["modelo"])
    
    aux_stack.push(traje)

while aux_stack.size() > 0:
    trajes_stack.push(aux_stack.pop())

print("Los modelos de trajes que quedaron **Dañados** son:")
print(f" {', '.join(modelos_danados)}")


print("\n## c. Eliminación de Trajes Destruidos 💥")

pila_conservada = Stack()
modelos_eliminados = []
estado_eliminacion = "Destruido"

while trajes_stack.size() > 0:
    traje = trajes_stack.pop()
    
    if traje["estado"] == estado_eliminacion:
        modelos_eliminados.append(traje["modelo"])
    else:
        pila_conservada.push(traje)

trajes_stack = pila_conservada

print(f"Los siguientes trajes con estado '{estado_eliminacion}' han sido **eliminados**:")
print(f"➡️ {', '.join(modelos_eliminados)}")
trajes_stack.show()


print("\n## e. Agregar Mark LXXXV (sin repetir) ➕")

nuevo_traje = {"modelo": "Mark LXXXV", "pelicula": "Avengers: Endgame", "estado": "Destruido"}
modelo_a_agregar = nuevo_traje["modelo"]
aux_stack = Stack()
modelo_ya_existe = False

while trajes_stack.size() > 0:
    traje = trajes_stack.pop()
    
    if traje["modelo"] == modelo_a_agregar:
        modelo_ya_existe = True
        
    aux_stack.push(traje)

while aux_stack.size() > 0:
    trajes_stack.push(aux_stack.pop())

if not modelo_ya_existe:
    trajes_stack.push(nuevo_traje)
    print(f" Modelo {modelo_a_agregar} agregado a la pila.")
else:
    print(f" El modelo {modelo_a_agregar} ya existe en la pila. No se agregó.")
    
trajes_stack.show()


print("\n## f. Búsqueda por Película 🎥")

peliculas_buscadas = ["Spider-Man: Homecoming", "Capitan America: Civil War"]
modelos_encontrados = set() 
aux_stack = Stack()

while trajes_stack.size() > 0:
    traje = trajes_stack.pop()
    
    if traje["pelicula"] in peliculas_buscadas:
        modelos_encontrados.add(traje["modelo"])
    
    aux_stack.push(traje)

while aux_stack.size() > 0:
    trajes_stack.push(aux_stack.pop())

print(f"Trajes utilizados en '{', '.join(peliculas_buscadas)}':")
print(f" {', '.join(modelos_encontrados)}")
