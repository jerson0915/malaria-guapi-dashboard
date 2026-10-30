# Malaria Guapi Dashboard

Proyecto para analizar y consultar datos de malaria en Guapi, Cauca, con estructura lista para trabajar desde GitHub y ejecutar consultas SQL en Google Colab.

## Archivos
- `index copia.html`: dashboard visual de Guapi
- `queries.sql`: consultas SQL base para explorar los datos de Guapi
- `colombia_sql_ready.py`: crea una base SQLite y muestra consultas para Google Colab

## Repositorio GitHub
Este proyecto se puede clonar y usar con una conexión a SQLite, BigQuery o cualquier base de datos compatible.

## Consultas SQL de ejemplo
```sql
SELECT anio, casos, ipa FROM anual ORDER BY anio;
SELECT zona, SUM(casos) AS total FROM zona GROUP BY zona;
SELECT nombre, rio, total, poblacion, ROUND((2024 / poblacion) * 1000, 2) AS tasa_2024
FROM veredas;
```
