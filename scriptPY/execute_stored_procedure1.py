import pyodbc
import sys

def execute_stored_procedure(consulta, dbSap):
    try:
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                              'SERVER=192.168.16.3;'
                              'DATABASE=PedidosEnLinea;'
                              'UID=sa;'
                              'PWD=P@ssw0rd')
        cursor = conn.cursor()

        query = "EXEC dbo.SP_Conteo ?, ?"
        cursor.execute(query, (consulta, dbSap))

        result = cursor.fetchall()

        conn.close()

        return str(result)

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    consulta = sys.argv[1]  # Get consulta argument
    dbSap = sys.argv[2]  # Get dbSap argument
    print(execute_stored_procedure(consulta, dbSap))  # Output the result
