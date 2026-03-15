# Clase Base (Padre)
class Empleado:
    def __init__(self, nombre, id_empleado, salario_base):
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.salario_base = salario_base

    def mostrar_datos(self):
        print(f"ID: {self.id_empleado} | Nombre: {self.nombre} | Salario Base: ${self.salario_base}")

    def calcular_pago(self):
        return self.salario_base

# Clase Derivada (Hija) - Reutiliza atributos y métodos
class Gerente(Empleado):
    def __init__(self, nombre, id_empleado, salario_base, bono_gestion):
        # Llamada al constructor de la clase base (Herencia)
        super().__init__(nombre, id_empleado, salario_base)
        self.bono_gestion = bono_gestion

    # Sobrescritura de método (Polimorfismo básico)
    def calcular_pago(self):
        return self.salario_base + self.bono_gestion

    # Método exclusivo de la subclase
    def organizar_reunion(self):
        print(f"El gerente {self.nombre} está organizando una reunión de equipo.")

# --- Programa Principal (Instanciación y Pruebas) ---
if __name__ == "__main__":
    # Instancia de la clase base
    emp1 = Empleado("Juan Perez", "E001", 1000)
    
    # Instancia de la clase derivada
    gerente1 = Gerente("Ana Gomez", "G001", 2000, 500)

    print("--- Información de Empleados ---")
    emp1.mostrar_datos()
    print(f"Pago total: ${emp1.calcular_pago()}")
    
    print("\n--- Información de Gerente (Herencia) ---")
    gerente1.mostrar_datos() # Método heredado
    print(f"Pago total con bono: ${gerente1.calcular_pago()}") # Método sobrescrito
    gerente1.organizar_reunion() # Método exclusivo