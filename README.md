# Genera INSERT en base a una tabla en Excel

- **Construye la imagen en docker**
```bash
docker build -t py-inserts .
```

- **Ejecute el contenedor**
```bash
docker run -it --rm -v './docs':/app/docs py-inserts
```

- Remplace './docs' por la carpeta donde tendra la información
