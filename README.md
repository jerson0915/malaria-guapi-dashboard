# Malaria Guapi Dashboard

Proyecto para analizar y consultar datos de malaria en Guapi, Cauca, con estructura lista para trabajar desde GitHub y ejecutar consultas SQL en Google Colab.

## Archivos
- `index copia.html`: dashboard con mapa municipal y agregado del evento 460
- `queries.sql`: consultas SQL, incluidos agregados municipales del evento 460
- `colombia_sql_ready.py`: crea una base SQLite y muestra consultas para Google Colab

## Cobertura de los datos
Los indicadores principales de la dashboard son de Guapi. La tabla municipal adicional resume registros confirmados del evento 460 (malaria asociada, formas mixtas) por municipio de ocurrencia y año, a partir de los archivos `Datos_2018_460.xlsx` a `Datos_2025_460.xlsx` suministrados localmente. Este evento no representa el total de malaria. Los Excel originales contienen registros individuales y no se incluyen en el repositorio; solo se publican los agregados.

## Repositorio GitHub
Este proyecto se puede clonar y usar con una conexión a SQLite, BigQuery o cualquier base de datos compatible.

## Consultas SQL de ejemplo
```sql
SELECT anio, casos, ipa FROM anual ORDER BY anio;
SELECT zona, SUM(casos) AS total FROM zona GROUP BY zona;
SELECT nombre, rio, total, poblacion, ROUND((2024 / poblacion) * 1000, 2) AS tasa_2024
FROM veredas;
```
