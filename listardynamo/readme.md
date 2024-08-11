- Crear los Archivos ZIP
Navega a esta carpeta por terminal /listardynamo y ejecuta el siguiente comando para crear el ZIP:

zip listardynamo.zip index.py

- Subir los Archivos ZIP a S3

aws s3 cp listardynamo.zip s3://s3demomanve/code/listardynamo.zip


** Nota: Los comandos de la línea 1-8 NO serían necesarios si se corre el script script1_upload_s3.sh, siguiendo los pasos del Readme.md root que ya los contiene.