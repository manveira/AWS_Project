- Crear los Archivos ZIP
Navega a esta carpeta por terminal /listars3 y ejecuta el siguiente comando para crear el ZIP:

zip listars3.zip index.py

- Subir los Archivos ZIP a S3

aws s3 cp listars3.zip s3://s3demomanve/code/listars3.zip


** Nota: Los comandos de la línea 1-8 NO serían necesarios si se corre el script script1_upload_s3.sh, siguiendo los pasos del Readme_general.md que ya los contiene.