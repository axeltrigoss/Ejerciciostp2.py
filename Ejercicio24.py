from typing import Any, Optional, List, Tuple
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
        """Muestra el contenido de la pila de cima a base, restaurando su estado."""
        aux_stack = Stack()
        print("(Cima)")
        while self.size() > 0:
            value = self.pop()
            print(value)
            aux_stack.push(value)
        print("(Base)")
        
        # Restaurar la pila original
        while aux_stack.size() > 0:
            self.push(aux_stack.pop())


Personaje = Tuple[str, int]

def load_mcu_stack() -> Stack:
    """Crea y carga la pila inicial con datos de ejemplo del MCU."""
    mcu_stack = Stack()
    data: List[Personaje] = [
        ("Iron Man", 11),
        ("Captain America", 10),
        ("Thor", 9),
        ("Black Widow", 8),
        ("Hulk", 6),
        ("Rocket Raccoon", 5),
        ("Groot", 5),
        ("Hawkeye", 5),
        ("Doctor Strange", 4),
        ("Scarlet Witch", 3),
        ("Captain Marvel", 3) 
    ]
    for name, films in reversed(data):
        mcu_stack.push((name, films))
        
    return mcu_stack



def find_character_info(stack: Stack, name: str, return_type: str) -> Optional[Any]:
    """
    Busca un personaje y retorna su posición o cantidad de películas.
    Asegura que la pila original se restaure.
    """
    aux_stack = Stack()
    position = 0
    found_info = None
    
    while stack.size() > 0:
        character, films = stack.pop()
        position += 1
        aux_stack.push((character, films))

        if character == name:
            if return_type == "position":
                found_info = position
            elif return_type == "films":
                found_info = films

  

      while aux_stack.size() > 0:
        stack.push(aux_stack.pop())

    return found_info



def solve_a(mcu_stack: Stack):
    print("--- Inciso a: Posición de Rocket Raccoon y Groot ---")
    
    pos_rocket = find_character_info(mcu_stack, "Rocket Raccoon", "position")
    pos_groot = find_character_info(mcu_stack, "Groot", "position")

    print(f"Rocket Raccoon se encuentra en la posición: {pos_rocket}")
    print(f"Groot se encuentra en la posición: {pos_groot}")

def solve_b(stack: Stack):
    print("\n--- Inciso b: Personajes con más de 5 películas ---")
    aux_stack = Stack()
    result = []
    
    while stack.size() > 0:
        character, films = stack.pop()
        
        aux_stack.push((character, films))
        
        if films > 5:
            result.append((character, films))

    while aux_stack.size() > 0:
        stack.push(aux_stack.pop())
    
    if result:
        print("Personajes que participaron en más de 5 películas:")
        for name, films in result:
            print(f"- {name}: {films} películas")
    else:
        print("No se encontraron personajes que cumplan con el criterio.")

def solve_c(mcu_stack: Stack):
    print("\n--- Inciso c: Películas de Viuda Negra (Black Widow) ---")
    
    films = find_character_info(mcu_stack, "Black Widow", "films")

    if films is not None:
        print(f"Viuda Negra (Black Widow) participó en {films} películas.")
    else:
        print("Viuda Negra (Black Widow) no fue encontrada en la pila.")

def solve_d(stack: Stack):
    print("\n--- Inciso d: Personajes que empiezan con C, D, o G ---")
    aux_stack = Stack()
    result = []
    initials_to_check = ('C', 'D', 'G')
    
    while stack.size() > 0:
        character, films = stack.pop()
        
        aux_stack.push((character, films))
        
        if character.startswith(initials_to_check):
            result.append(character)

    while aux_stack.size() > 0:
        stack.push(aux_stack.pop())
    
    if result:
        print("Personajes cuyo nombre empieza con C, D, o G:")
        for name in sorted(result):
            print(f"- {name}")
    else:
        print("No se encontraron personajes cuyos nombres empiecen con C, D, o G.")

if __name__ == "__main__":
    mcu_stack = load_mcu_stack()
    
    print(" Estado inicial de la pila MCU:")
    mcu_stack.show()
    print("-" * 40)
    
    solve_a(mcu_stack)
    solve_b(mcu_stack)
    solve_c(mcu_stack)
    solve_d(mcu_stack)
    
    print("-" * 40)
    print(" Pila final restaurada (debería ser igual a la inicial):")
    mcu_stack.show()
