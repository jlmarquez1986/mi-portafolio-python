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
   ![Gestión de productos](/assets/Gestión_producto_servicio.png)

5. **Facturación:**  
   Creación de facturas, cálculo automático de impuestos y exportación en PDF.  
   ![Creación de facturas](/images/facturas.png)

6. **Configuración de la empresa:**  
   Permite personalizar los datos fiscales (nombre, CIF/NIF, dirección).  

7. **Gestión de usuarios:**  
   Control de cuentas y roles (Administrador / Empleado).  
   ![Gestión de usuarios](/images/usuarios.png)

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

![Esquema de base de datos](/images/database_schema.png)

---

## Requisitos de la aplicación

- Python 3.10 o superior  
- Bibliotecas:  
  ```bash
  pip install bcrypt reportlab ttkbootstrap
