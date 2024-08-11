import json
import logging
import boto3
from botocore.exceptions import ClientError
from decimal import Decimal

# Configura el logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')
table_name = 'productos'

def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

def lambda_handler(event, context):
    table = dynamodb.Table(table_name)
    items = []
    last_evaluated_key = None

    try:
        logger.info('Iniciando el escaneo de la tabla: %s', table_name)
        
        while True:
            scan_kwargs = {}
            if last_evaluated_key:
                scan_kwargs['ExclusiveStartKey'] = last_evaluated_key
            
            response = table.scan(**scan_kwargs)
            items.extend(response.get('Items', []))
            
            last_evaluated_key = response.get('LastEvaluatedKey')
            if not last_evaluated_key:
                break
        
        logger.info('Escaneo completado. Total de ítems obtenidos: %d', len(items))
        
        return {
            'statusCode': 200,
            'body': json.dumps(items, default=decimal_default),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'  # Para habilitar CORS si es necesario
            }
        }
    
    except ClientError as e:
        logger.error('Error al realizar el escaneo de la tabla: %s', str(e))
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Error al acceder a DynamoDB', 'details': str(e)}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
    
    except Exception as e:
        logger.error('Error inesperado: %s', str(e))
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Error inesperado', 'details': str(e)}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }