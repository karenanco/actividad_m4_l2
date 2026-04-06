class Autor:
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais

class Editorial:
    def __init__(self, nombre, ciudad):
        self.nombre = nombre
        self.ciudad = ciudad

class Libro:
    def __init__(self, titulo, autor_obj, anio, nombre_editorial, ciudad_editorial):
        # Atributos básicos
        self._titulo = titulo
        self._anio_publicacion = anio
        
        # Colaboración (Recibe un objeto Autor ya creado)
        self.autor = autor_obj
        
        # Composición (El objeto Editorial se crea DENTRO de Libro)
        self.editorial = Editorial(nombre_editorial, ciudad_editorial)

    # --- Métodos Accesadores (Getters) y Mutadores (Setters) ---
    def get_titulo(self):
        return self._titulo

    def set_titulo(self, nuevo_titulo):
        self._titulo = nuevo_titulo

    def get_anio_publicacion(self):
        return self._anio_publicacion

    def set_anio_publicacion(self, nuevo_anio):
        self._anio_publicacion = nuevo_anio

    # --- Sobrecarga de Métodos (Simulada con valores por defecto) ---
    def resumen(self, texto=None):
        if texto is None:
            print("Libro sin resumen disponible.")
        else:
            print(f"Resumen: {texto}")

    # --- Mostrar Información ---
    def mostrar_info(self):
        print(f"--- Información del Libro ---")
        print(f"Título: {self._titulo}")
        print(f"Año: {self._anio_publicacion}")
        print(f"Autor: {self.autor.nombre} (País: {self.autor.pais})")
        print(f"Editorial: {self.editorial.nombre} (Ciudad: {self.editorial.ciudad})")
        print("-" * 30)

# --- Programa Principal ---

# 1. Crear el objeto Autor (Colaboración)
escritor = Autor("Gabriel García Márquez", "Colombia")

# 2. Crear el objeto Libro 
# (Notar que enviamos datos para que el Libro cree su propia Editorial - Composición)
mi_libro = Libro("Cien años de soledad", escritor, 1967, "Editorial Sudamericana", "Buenos Aires")

# 3. Mostrar información inicial
mi_libro.mostrar_info()

# 4. Uso de Accesadores y Mutadores
mi_libro.set_titulo("Cien años de soledad (Edición Especial)")
print(f"Título modificado: {mi_libro.get_titulo()}")

# 5. Prueba de la Sobrecarga del método resumen
mi_libro.resumen() # Sin parámetros
mi_libro.resumen("Una saga familiar en el pueblo ficticio de Macondo.") # Con parámetro