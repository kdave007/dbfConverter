
from dbfread import DBF, DBFNotFound
import json
from datetime import date,datetime  # Para manejar objetos de tipo date


# Función para convertir objetos date a cadenas
def date_parser(record):
    for key, value in record.items():
        if isinstance(value, date):  # Si el value es de tipo date
            record[key] = value.isoformat()  # Convertir a cadena en formato ISO
    return record
def unique_key_gen():
    now = datetime.now()
    return now.strftime('%d%m%Y%H%M%S')

path_dbf = 'mockDBF/PARTVTA.DBF'  # Ruta relativa o absoluta
path_json = 'records/registros_'+unique_key_gen()+'.json'  # Ruta donde se guardará el archivo JSON

try:
    # Intenta abrir el archivo DBF
    table = DBF(path_dbf)

    # Lista para almacenar los registros
    records = []

    # Itera sobre los primeros 10 registros
    for i, record in enumerate(table):
        if i >= 3:
            break
        # Convierte los objetos date a cadenas
        parsedRecord = date_parser(record)
        records.append(parsedRecord)  # Agrega el registro a la lista
       # print(f"Registro {i + 1}:")
       # print(parsedRecord)
       # print("-" * 40)

    # Guarda los registros en un archivo JSON
    with open(path_json, 'w', encoding='utf-8') as f:
        json.dump(records, f, indent=4, ensure_ascii=False)

    print(f"\nSe han guardado {len(records)} registros en '{path_json}'.")

except DBFNotFound as e:
    # Maneja el caso en que el archivo no se encuentre
    print(f"Error: No se encontró el archivo DBF en la ruta '{path_dbf}'.")
    print(f"Detalle del error: {e}")

except Exception as e:
    # Maneja otros errores inesperados
    print(f"Ocurrió un error inesperado al intentar leer el archivo DBF.")
    print(f"Detalle del error: {e}")