# 42_Python_Module_01
---
##  Cultivando Código  
**Sistemas de Cosecha Orientados a Objetos – Python**

Proyecto educativo enfocado en aprender **Python y Programación Orientada a Objetos (POO)** mediante la metáfora de un huerto digital. Cada ejercicio construye una parte del sistema, desde scripts básicos hasta arquitecturas complejas.

---

##  Estructura del Proyecto

Cada ejercicio se encuentra en su propio directorio (`ex0` a `ex6`) y archivo Python.

---

##  Ejercicio 0 – `ft_garden_intro.py`
**Objetivo:**  
Introducción a la estructura básica de un programa en Python.

**Requisitos:**
- Punto de entrada con `if __name__ == "__main__"`
- Variables simples: `nombre`, `altura`, `edad`
- Mostrar información usando `print()`

---

##  Ejercicio 1 – `ft_garden_data.py`
**Objetivo:**  
Organizar datos usando clases.

**Requisitos:**
- Crear clase `Plant` con atributos: `nombre`, `altura`, `edad`
- Gestionar al menos 3 plantas
- Mostrar información de manera organizada

---

##  Ejercicio 2 – `ft_plant_growth.py`
**Objetivo:**  
Simular crecimiento y envejecimiento de plantas.

**Requisitos:**
- Reutilizar clase `Plant`
- Implementar métodos: `grow()`, `age()`, `get_info()`
- Simular el crecimiento durante al menos una semana
- Mostrar cambios de estado de las plantas

---

##  Ejercicio 3 – `ft_plant_factory.py`
**Objetivo:**  
Optimizar la creación de múltiples plantas.

**Requisitos:**
- Crear plantas con atributos iniciales (`nombre`, `altura`, `edad`)
- Al menos 5 plantas con características diferentes
- Mostrar todas las plantas creadas
- Contar el total de plantas

---

##  Ejercicio 4 – `ft_garden_security.py`
**Objetivo:**  
Proteger la integridad de los datos mediante encapsulación.

**Requisitos:**
- Crear clase `SecurePlant`
- Métodos seguros: `set_height()`, `get_height()`, `set_age()`, `get_age()`
- Validar que altura y edad no sean negativas
- Mostrar mensajes de error en caso de valores inválidos

---

##  Ejercicio 5 – `ft_plant_types.py`
**Objetivo:**  
Aplicar herencia y especialización de clases.

**Requisitos:**
- Clase base `Plant` con atributos comunes
- Subclases: `Flower`, `Tree`, `Vegetable`
- Cada subclase con atributos y métodos específicos:
  - `Flower` → `color`, `bloom()`
  - `Tree` → `trunk_diameter`, `produce_shade()`
  - `Vegetable` → `harvest_season`, `nutritional_value`
- Crear al menos 2 instancias de cada tipo

---

##  Ejercicio 6 – `ft_garden_analytics.py`
**Objetivo:**  
Construir un sistema complejo con múltiples componentes.

**Requisitos:**
- Clase `GardenManager` que gestione múltiples huertos
- Clase anidada `GardenStats` para estadísticas
- Herencia avanzada: `Plant → FloweringPlant → PrizeFlower`
- Métodos de instancia, clase y estáticos
- Registro de plantas y estadísticas de cada huerto
- Función `create_garden_network()` para gestionar la red de huertos

---

##  Conceptos Clave Trabajados
- Programación Orientada a Objetos (POO)
- Encapsulación y validación de datos
- Herencia y reutilización de código
- Métodos de instancia, clase y estáticos
- Organización de sistemas complejos y escalables

---

 *Cada archivo está diseñado para ejecutarse sin errores y demostrar comprensión real del código.*
