from fastapi import FastAPI, HTTPException, Query, Depends
from fastapi.middleware.cors import CORSMiddleware
from database import conexionBD  # ← Sin "backend."
import psycopg2

app = FastAPI(title="Login Proyecto Integrador 1")

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # URL de Angular
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ENDPOINTS
@app.get("/estado")
def estado():
    return{"status": "Funcionando"}

# Temporal - Es para verificar los usuarios
@app.get("/usuarios")
def obtenerUsuarios():
    conexion = conexionBD()
    if not conexion:
        raise HTTPException(status_code=500, detail="Error al conectar con la base de datos")
    try:
        with conexion.cursor() as cursor:
            query = "SELECT * FROM tbl_usuariosLogin"
            cursor.execute(query)
            usuarios = cursor.fetchall()
            return {"usuarios": usuarios}
    except psycopg2.Error as e:
        raise HTTPException(status_code=500, detail=f"Error en la consulta: {e}")
    finally:
        conexion.close()

@app.post("/validar-login")
def validarLogin(pUsuario: str, pClave: str):
    conexion = conexionBD()
    if not conexion:
        raise HTTPException(status_code=500, detail="Error al conectar con la base de datos")
    try:
        with conexion.cursor() as cursor:
            query = "SELECT nombreUsuario FROM tbl_usuariosLogin WHERE usuario= %s AND clave = %s"
            valores = (pUsuario, pClave)
            cursor.execute(query, valores)
            usuario = cursor.fetchone()
            if usuario:
                return{"login": True, "Nombre": usuario[0]}
            else:
                return{"login": False}
    except psycopg2.Error as e:
        raise HTTPException(status_code=500, detail=f"Error en la consulta: {e}")
    finally:
        conexion.close()