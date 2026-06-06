<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&color=FF69B4&center=true&vCenter=true&width=500&height=50&lines=👨‍💻+Curso+Python+--+Alex;🐍+Fundamentos+y+Estructuras+de+Datos;📊+Tuplas%2C+Conjuntos+y+Excepciones;🐙+Control+de+Versiones+con+Git%2FGitHub;🚀+¡¡Seguimos!!" alt="Typing SVG" />
</p>

---

![Python](https://img.shields.io/badge/Python-%23E91E63.svg?style=for-the-badge&logo=python&logoColor=white)
![Git](https://img.shields.io/badge/Git-%23F06292.svg?style=for-the-badge&logo=git&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-%23F8BBD0.svg?style=for-the-badge&logo=visual-studio-code&logoColor=black)

---

# 🚀 Mi Repositorio de Python - `python_basics`

¡Bienvenid@ a mi repositorio de fundamentos de Python! 

Este espacio está diseñado para consolidar todos los conceptos clave de programación, estructuras de datos y buenas prácticas que he estado estudiando en el curso de Python del Banco Santander.

**Autor:** Alejandra Sanz González (`alexescent`)  
**Lenguaje:** Python
**Contenido:** Fundamentos de Python  
**Entorno de Desarrollo:** VS Code + Git  

---

## 🎯 Objetivos del Repositorio

Este repositorio almacena scripts organizados y notas de código optimizadas para dominar los pilares de Python de manera limpia y profesional:

1. **Estructuras de Datos:** Comprensión profunda de colecciones inmutables (`Tuplas`) y colecciones sin elementos duplicados (`Conjuntos`).
2. **Control de Errores:** Gestión robusta de excepciones con bloques `try-except` y lanzamientos personalizados mediante `raise Exception`.
3. **Flujo de Ejecución:** Uso correcto del "guardián" de script principal con la estructura `if __name__ == "__main__":`.
4. **Control de Versiones:** Configuración correcta del repositorio local con Git y despliegue seguro en la nube a través de GitHub.

---

## 🛠️ Conceptos Clave Implementados

### 📦 Métodos de Tuplas
Las tuplas son colecciones inmutables excelentes para proteger datos. Implementación y uso de:
* `len(tupla)`: Obtiene la cantidad total de elementos almacenados.
* `.count(elemento)`: Cuenta cuántas veces exactas se repite un valor específico.
* `.index(elemento, [inicio], [fin])`: Localiza el índice de la primera aparición con rangos de búsqueda delimitados.

### 📐 Operaciones con Conjuntos (`Sets`)
Uso avanzado de colecciones sin orden ni duplicados para lógica matemática directa:
* **Unión (`|`)**: Combina elementos de ambos conjuntos eliminando repetidos.
* **Intersección (`&`)**: Extrae únicamente los elementos en común.
* **Diferencia (`-`)**: Elimina del primer conjunto todo elemento presente en el segundo.
* **Diferencia Simétrica (`^`)**: Conserva todos los elementos exclusivos de cada conjunto, descartando los compartidos.

### ⚠️ Gestión de Excepciones
Diseño de código defensivo para evitar "crashes" de aplicación ante fallos lógicos (por ejemplo, control de saldos insuficientes en una simulación de cajero automático).

---

## 📚 A modo resumen
Este proyecto contiene todos los ejercicios, pruebas de código y apuntes prácticos desarrollados durante el curso de **Python de Banco Santander**.
Más que un simple repositorio, he diseñado este espacio como una **guía de estudio analítica** personal para consolidar la lógica de programación, el manejo de datos y la estructuración de código.

---

## 📂 Arquitectura del Proyecto

Todos los archivos se encuentran en el directorio principal para facilitar el acceso rápido y la ejecución de los scripts. La estructura exacta es la siguiente:

```text
curso-python-santander/
│
├── README.md          # Documentación general y guía del repositorio
├── __init__.py        # Archivo de inicialización para tratamiento de módulos
├── datos.txt          # Archivo de texto autogenerado para prácticas de I/O
├── main.py            # 🧠 Script central: Guía interactiva de conceptos y sintaxis
├── mi_modulo.py       # Módulo de prueba combinando funciones de saludo y cálculo
├── operaciones.py     # Módulo enfocado en aislar la lógica matemática
└── utilidades.py      # Módulo de herramientas para la interacción con el usuario
