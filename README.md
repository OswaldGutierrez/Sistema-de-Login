# 🔐 Sistema de Login y Autenticación

Sistema web completo de autenticación que permite el registro de usuarios, inicio de sesión seguro y control de acceso basado en roles. Desarrollado con una arquitectura desacoplada: backend en **FastAPI + PostgreSQL** y frontend en **Angular**.

---

## 🛠️ Tecnologías utilizadas

| Capa | Tecnología |
|------|------------|
| Frontend | Angular |
| Backend | Python + FastAPI + Uvicorn |
| Base de datos | PostgreSQL + SQLAlchemy |
| Seguridad | bcrypt (hash de contraseñas) |
| Configuración | python-dotenv |

---

## ✅ Funcionalidades

- Registro de nuevos usuarios
- Inicio de sesión con validación de credenciales
- Contraseñas cifradas con bcrypt
- Control de acceso por roles y permisos
- API REST documentada automáticamente por FastAPI


## ▶️ ¿Cómo ejecutarlo?

### Backend (FastAPI)

1. Crea y activa un entorno virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Mac/Linux
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Crea un archivo `.env` en la carpeta del backend con tus credenciales:
   ```env
   DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/nombre_db
   ```

4. Inicia el servidor:
   ```bash
   uvicorn main:app --reload
   ```

5. La API estará disponible en `http://localhost:8000` y la documentación interactiva en `http://localhost:8000/docs`.

---

### Frontend (Angular)

1. Instala las dependencias:
   ```bash
   npm install
   ```

2. Inicia la aplicación:
   ```bash
   ng serve
   ```

3. Abre el navegador en `http://localhost:4200`.


## 📚 Lo que aprendí

Este proyecto me permitió construir una aplicación web con arquitectura desacoplada, separando completamente el backend del frontend. Aprendí a diseñar una API REST con FastAPI, conectarla a PostgreSQL mediante SQLAlchemy y proteger las contraseñas usando bcrypt. Implementar un sistema de roles me obligó a pensar en el control de acceso desde el diseño de la base de datos, no solo desde la interfaz. Integrar el frontend en Angular con el backend mediante peticiones HTTP me dio una visión completa del flujo de una aplicación real.

---

## 👤 Autor

**Oswald David Gutiérrez Cortina**  
Estudiante de Ingeniería — Universidad  
[LinkedIn](www.linkedin.com/in/oswald-david-gutierrez-1a452939a) · [GitHub]([https://github.com/tu-usuario](https://github.com/OswaldGutierrez))
