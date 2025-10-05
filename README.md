# FacturaX

**Autor:** José Luis Márquez García  
**Curso:** Programación en Python  
**Fecha:** 2025  

---

## Descripción general del proyecto

**FacturaX** es una aplicación de escritorio desarrollada en **Python**, diseñada como una solución práctica para **pequeñas empresas y autónomos** que necesiten gestionar facturación, clientes, productos y servicios de forma eficiente.

El sistema ofrece una interfaz intuitiva, visual y accesible, que permite automatizar tareas administrativas, generar facturas en PDF y centralizar la información en una base de datos local.  

### Principales características

- **Automatización:** Generación rápida y segura de facturas.  
- **Centralización:** Gestión de clientes, productos y facturas en una única base de datos.  
- **Seguridad:** Autenticación con roles y contraseñas cifradas.  
- **Eficiencia:** Interfaz intuitiva desarrollada con *Tkinter* y *ttkbootstrap*.  
- **Portabilidad:** No requiere servidores externos; funciona de manera local.  

---

## Objetivos y alcance

### Objetivos

- Sistema de login con gestión de roles (Administrador y Empleado).  
- Gestión completa de clientes, productos y servicios.  
- Creación, almacenamiento y consulta de facturas.  
- Exportación de facturas a **PDF** con cálculo automático de **IVA** e **IRPF**.  
- Configuración de datos de la empresa mediante archivo JSON.  
- Base de datos local **SQLite**.  
- Interfaz gráfica amigable.  

### Alcance funcional

El sistema incluye los siguientes módulos principales:

1. **Login y control de acceso:**  
   Sistema de autenticación seguro con contraseñas cifradas mediante *bcrypt* y control de roles.

2. **Gestión de clientes:**  
   Registro, edición y eliminación de clientes.  
   ![Gestión de clientes](/assets/pantalla_clientes.png)

3. **Gestión de productos y servicios:**  
   Control completo de productos o servicios facturables.  
   ![Gestión de productos](/assets/gestion_productos_servicio.png)

4. **Facturación:**  
   Creación de facturas, cálculo automático de impuestos y exportación en PDF.  
   ![Pantalla de facturas](/assets/pantalla_de_facturas.png)

5. **Configuración de la empresa:**  
   Permite personalizar los datos fiscales (nombre, CIF/NIF, dirección).  

6. **Gestión de usuarios:**  
   Control de cuentas y roles (Administrador / Empleado).  
   ![Gestión de usuarios](/assets/gestion_de_usuario.png)

---

## Stack tecnológico

| Componente | Tecnología |
|-------------|-------------|
| Lenguaje principal | Python |
| GUI Framework | Tkinter + ttkbootstrap |
| Base de datos | SQLite |
| Seguridad | bcrypt |
| Generación de PDF | ReportLab |

### Alternativas evaluadas

- **Base de datos:** MySQL y PostgreSQL se descartaron por complejidad y necesidad de servidor externo.  
- **Tipo de aplicación:** Se optó por una aplicación de escritorio en lugar de una aplicación web (Flask/Django) para simplificar el despliegue local.  

---

## Modelo de datos

La aplicación utiliza una base de datos **SQLite** denominada `facturacion.db`.  

### Esquema principal

| Tabla | Descripción |
|-------|--------------|
| usuarios | Datos de acceso y roles de usuario |
| clientes | Información de los clientes |
| productos | Productos y servicios facturables |
| facturas | Datos principales de cada factura |
| detalles_factura | Relación entre facturas y productos |
| sqlite_sequence | Control interno de autoincrementos |

![Esquema de base de datos](/assets/diagrama.png)

---

## Requisitos de la aplicación

- Python 3.10 o superior  
- Bibliotecas necesarias:
  ```bash
  pip install bcrypt reportlab ttkbootstrap
  ```

---

## Manual de instalación y ejecución

### 1. Ejecución local (modo desarrollo)

Asegúrate de tener **Python 3.10+** instalado. Luego:

1. Clona el repositorio:
   ```bash
   git clone https://github.com/jlmarquez1986/mi-portafolio-python.git
   cd FacturaX
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requisitos.txt
   ```

3. Ejecuta la aplicación:
   ```bash
   python main.py
   ```

### 2. Generación del ejecutable (.exe)

Para crear un archivo ejecutable independiente:
```bash
pyinstaller --onefile --windowed main.py
```

El archivo `FacturaX.exe` se generará en la carpeta `/dist`.

> **Nota sobre la firma digital:**  
> Si Windows muestra la advertencia *"Windows protegió su PC"*, haz clic en **“Más información” → “Ejecutar de todas formas”**.  
> Esto ocurre por la falta de una firma digital, no por problemas de seguridad.

---

## Uso de la aplicación

1. **Pantalla de inicio de sesión:** Autenticación de usuarios con contraseñas cifradas y control de roles.  
2. **Menú principal:** Acceso centralizado a Clientes, Productos, Facturas, Usuarios y Configuración.  
3. **Gestión de clientes:** Altas, ediciones y eliminaciones con búsqueda por nombre o apellidos.  
4. **Gestión de productos y servicios:** Control de inventario, precios e impuestos.  
5. **Creación de facturas:** Flujo guiado para seleccionar un cliente, añadir ítems y guardar la factura.  
6. **Exportación en PDF:** Generación de facturas profesionales mediante ReportLab.  
7. **Gestión de usuarios:** Alta, edición o eliminación de cuentas y roles.  
8. **Configuración de empresa:** Edición de los datos fiscales incluidos en las facturas.  

---

## Base de datos (gestión interna)

Cada acción (añadir, editar o eliminar) se refleja **automáticamente** en la base de datos **SQLite**, garantizando la integridad y coherencia de la información.

---

## Conclusiones

**FacturaX** demuestra la capacidad de Python para desarrollar aplicaciones de escritorio completas, seguras y útiles para la gestión administrativa.

### Logros principales

- Interfaz moderna e intuitiva con **ttkbootstrap**.  
- Seguridad en credenciales mediante **bcrypt**.  
- Generación automática de documentos PDF profesionales.  
- Diseño modular y escalable para futuras integraciones web o nube.

### Aprendizajes personales

- Profundización en POO con Python y gestión de bases de datos **SQLite**.  
- Diseño y arquitectura de interfaces gráficas.  
- Mejora de habilidades en modularidad, organización y resolución de problemas.  

---

## Evolutivos del proyecto (futuras mejoras)

| Categoría | Evolutivo | Descripción |
|------------|------------|-------------|
| **Grado 1 (Operativo)** | Automatización | Sistema de plantillas personalizadas, envío automático por correo y copias de seguridad automáticas. |
| **Grado 1 (Visual)** | Reportes gráficos | Implementación de reportes estadísticos con Matplotlib. |
| **Grado 2 (Integración)** | AEAT / API | Módulo de gestión de impuestos con conexión a la Agencia Tributaria. |
| **Grado 3 (IA)** | Contable Virtual | Uso de IA para conciliación bancaria y clasificación de transacciones. |

---

## Créditos

**Desarrollado por:** José Luis Márquez García  

**Repositorio:**  
[https://github.com/jlmarquez1986/mi-portafolio-python](https://github.com/jlmarquez1986/mi-portafolio-python)

---

## Project Summary (English)

**FacturaX** is a desktop billing system built with **Python**, **Tkinter**, and **SQLite**.  
It allows small businesses and freelancers to manage clients, products, and invoices efficiently.  
Invoices are automatically generated in **PDF** format using **ReportLab**.  
The system includes user authentication, role management, and local data storage without servers.

**Author:** José Luis Márquez García  
**Repository:** [FacturaX GitHub](https://github.com/jlmarquez1986/mi-portafolio-python)
