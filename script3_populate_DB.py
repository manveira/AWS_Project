import boto3
from botocore.exceptions import ClientError

region_name = 'us-east-1'  
table_name = 'productos'

dynamodb = boto3.resource('dynamodb', region_name=region_name)

table = dynamodb.Table(table_name)

def put_item(item):
    try:
        response = table.put_item(Item=item)
        print(f"Item insertado con éxito: {item}")
        return response
    except ClientError as e:
        print(f"Error al insertar el ítem: {e.response['Error']['Message']}")

# Datos a insertar en tabla
items = [
    {"Id": 1, "Nombre": "Tomate", "Cantidad": 10},
    {"Id": 2, "Nombre": "Cebolla", "Cantidad": 5}
]

# Call function
for item in items:
    put_item(item)