# Genera INSERT en base a una tabla en Excel

- **Construye la imagen en docker**
```bash
docker build -t py-inserts .
```

- **Ejecute el contenedor**
```bash
docker run -it --rm -v /ruta/a/input.xlsx:/app/input.xlsx py-inserts
```

- Remplace /ruta/a/input.xlsx por la ruta donde se encuentra tu archivo Excel
