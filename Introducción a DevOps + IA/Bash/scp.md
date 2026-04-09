# Uso de SCP

Para hacer el envío de la información a la instancia de EC2 que se encuentra desplegada en AWS, se requiere:
- Llave SSH y ruta específica
- Archivo que se desea enviar y su ruta específica
- DNS de conexíon SSH de la instancia
- Ruta de destino de la instancia a donde se desea enviar el archivo

## Ejemplo base
```bash
scp -i  ~/.ssh/<LLAVE.pem> <ARCHIVO> <DNS SSH EC2 AWS>:~/<RUTA DESTINO>
```

## Código para cargue de bash a instancia
```bash
scp -i  ~/.ssh/llave-JuanHincapie.pem test.sh ec2-user@ec2-44-204-247-250.compute-1.amazonaws.com:~/
```