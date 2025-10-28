import psycopg2

def conexionBD():
    try:
        conexion = psycopg2.connect(
            host="ep-square-flower-adq56ghg-pooler.c-2.us-east-1.aws.neon.tech",
            database="neondb",
            user="neondb_owner",
            password="npg_0IdJlym1siSh"
        )
        print("Conexión exitosa")
        return conexion

    except psycopg2.Error as e:
        print(f"No se pudo conectar a la BD: {e}")
        return None


if __name__ == "__main__":
    conexion = conexionBD()
    if conexion:
        print(conexion)
        conexion.close()
