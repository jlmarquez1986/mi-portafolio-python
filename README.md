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

4. **Gestión de productos y servicios:**  
   Control completo de productos o servicios facturables.
     
   ![Gestión de productos](/assets/Gestión_productos_servicio.png)

6. **Facturación:**  
   Creación de facturas, cálculo automático de impuestos y exportación en PDF.
     
   ![Creación de facturas](/assets/pantalla_de_facturas.png)

8. **Configuración de la empresa:**  
   Permite personalizar los datos fiscales (nombre, CIF/NIF, dirección).  

9. **Gestión de usuarios:**  
   Control de cuentas y roles (Administrador / Empleado).
     
   ![Gestión de usuarios](/assets/Gestión_de_usuario.png)

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
- **Tipo de aplicación:** Se optó por aplicación de escritorio en lugar de web (Flask/Django) para simplificar el despliegue local.  

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
- Bibliotecas:  
  ```bash
  pip install bcrypt reportlab ttkbootstrap

  ¡Por supuesto! Ya tienes la documentación final. He tomado el texto que me has proporcionado y lo he formateado profesionalmente a Markdown para que luzca perfecto en tu README.md.

Este contenido debe ir después de la sección "Stack Tecnológico" y el "Modelo de Datos" que ya creamos previamente.

⚙️ **Manual de Instalación y Ejecución**
Aquí se explica cómo poner en marcha el proyecto, ya sea en modo desarrollo o como un ejecutable independiente.

1. ## Ejecución Local (Modo Desarrollo)
Asegúrate de tener Python 3.10+ instalado.

1. ## Clona el repositorio:
git clone https://github.com/jlmarquez1986/mi-portafolio-python.git
cd FacturaX

2. ## Instala las dependencias:
pip install -r requisitos.txt

3. ## Ejecuta la aplicación:
python aplicación.py

2. ## Generación del Ejecutable (.exe)
Para crear un archivo ejecutable que no dependa de la instalación de Python o librerías:
pyinstaller --onefile --windowed aplicación.py
El archivo aplicación.py.exe se generará en la carpeta /dist.

## Nota sobre la firma digital:
Si Windows muestra la advertencia "Windows protegió su PC", haz clic en **“Más información” → “Ejecutar de todas formas”**. Esto ocurre por la falta de una firma digital, no por problemas de seguridad.

🖥️ **Uso de la Aplicación**
Los módulos y el flujo de trabajo principal de **FacturaX** se organizan de la siguiente manera:

1. **Pantalla de Inicio de Sesión:** Autenticación de usuarios con contraseñas cifradas y control de roles.

2. **Menú Principal:** Acceso centralizado a todos los módulos: Clientes, Productos, Facturas, Usuarios y Configuración.

3. **Gestión de Clientes:** Altas, ediciones y eliminaciones de clientes, con funciones de búsqueda.

4. **Gestión de Productos y Servicios:** Control de inventario, precios e impuestos asociados a cada ítem facturable.

5. **Creación de Facturas:** Flujo guiado para seleccionar un cliente, añadir ítems y guardar la factura.

6. **Exportación en PDF:** Generación de una factura profesional en formato PDF (usando ReportLab).

7. **Gestión de Usuarios:** Permite añadir, editar o eliminar cuentas de usuario y asignar roles de acceso.

8. **Configuración de Empresa:** Edición de los datos fiscales de la empresa que se imprimen en las facturas.

## Base de Datos (Gestión Interna)
Cada acción (añadir, editar o eliminar) se refleja **automáticamente** en la base de datos **SQLite**. Esto garantiza la **integridad** y **coherencia** de la información sin necesidad de intervención manual.

🏆 **Conclusiones**
FacturaX demuestra la capacidad de Python para desarrollar aplicaciones de escritorio completas, seguras y útiles para la gestión administrativa.

## Logros Principales

· Interfaz moderna e intuitiva con ttkbootstrap.

· Seguridad en credenciales mediante cifrado **bcrypt**.

· Generación automática de documentos PDF profesionales.

· Diseño modular que permite la escalabilidad futura para integraciones web o nube.

## Aprendizajes Personales

· Profundización en programación orientada a objetos (POO) en Python y gestión de bases de datos **SQLite**.

· Diseño y arquitectura de interfaces gráficas funcionales.

· Refuerzo en la modularidad, organización y resolución de problemas.

📈 **Evolutivos del Proyecto (Futuras Mejoras)**
Categoría	Evolutivo	Descripción
**Grado 1 (Operativo)**	**Automatización**	Sistema de plantillas personalizadas de factura, envío automático por correo, y copias de seguridad automáticas.
**Grado 1 (Visual)**	**Reportes Gráficos**	Implementación de gráficos estadísticos con Matplotlib (ej. ventas por mes).
**Grado 2 (Integración)**	**AEAT / API**	Módulo de gestión de impuestos con conexión a la Agencia Tributaria.
**Grado 3 (IA)**	**"Contable Virtual"**	Implementación de un módulo basado en IA para automatizar la conciliación bancaria y la clasificación de transacciones.

👨‍💻 **Créditos**
Desarrollado por: **José Luis Márquez García**

## Repositorio:

## Project Summary (English)

FacturaX is a desktop billing system built with **Python**, **Tkinter**, and **SQLite**.
It enables small businesses and freelancers to manage clients, products, and invoices efficiently.
Invoices are automatically generated as professional **PDF** files using **ReportLab**.
The system includes user authentication, role management, and local data storage without requiring servers.

**Key technologies:** Python, Tkinter, ttkbootstrap, SQLite, bcrypt, ReportLab.
**Author:** José Luis Márquez García.


