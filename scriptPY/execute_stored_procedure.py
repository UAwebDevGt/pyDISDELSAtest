import pyodbc
import sys

def execute_stored_procedure(consulta, dbSap):
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                          'SERVER=192.168.16.3;'
                          'DATABASE=PedidosEnLinea;'
                          'UID=sa;'
                          'PWD=P@ssw0rd')
    cursor = conn.cursor()

    # Using EXEC to call the stored procedure with parameters
    query = "EXEC dbo.SP_Conteo ?, ?"
    cursor.execute(query, (consulta, dbSap))

    # Fetch the result
    result = cursor.fetchall()

    # Clean up the connection
    conn.close()

    # Return result as a string, JSON-like
    return str(result)


if __name__ == '__main__':
    consulta = sys.argv[1]  # Get consulta argument
    dbSap = sys.argv[2]  # Get dbSap argument
    print(execute_stored_procedure(consulta, dbSap))  # Output the result
