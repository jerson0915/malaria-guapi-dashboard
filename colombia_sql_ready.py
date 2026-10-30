import sqlite3
import pandas as pd

conn = sqlite3.connect('malaria_guapi.db')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS anual;
CREATE TABLE anual (
  anio TEXT,
  casos INTEGER,
  poblacion INTEGER,
  ipa REAL
);

INSERT INTO anual (anio, casos, poblacion, ipa) VALUES
('2022', 1317, 28736, 45.83),
('2023', 2713, 28979, 93.62),
('2024', 2009, 29275, 68.62),
('2025', 932, 29530, 31.56);

DROP TABLE IF EXISTS zona;
CREATE TABLE zona (
  anio TEXT,
  zona TEXT,
  casos INTEGER
);

INSERT INTO zona (anio, zona, casos) VALUES
('2022', 'Urbana', 103), ('2023', 'Urbana', 334), ('2024', 'Urbana', 150), ('2025', 'Urbana', 58),
('2022', 'Periurbana', 282), ('2023', 'Periurbana', 947), ('2024', 'Periurbana', 288), ('2025', 'Periurbana', 98),
('2022', 'Rural', 932), ('2023', 'Rural', 1432), ('2024', 'Rural', 1571), ('2025', 'Rural', 423);

DROP TABLE IF EXISTS veredas;
CREATE TABLE veredas (
  nombre TEXT,
  rio TEXT,
  poblacion INTEGER,
  total INTEGER,
  casos_2022 INTEGER,
  casos_2023 INTEGER,
  casos_2024 INTEGER,
  casos_2025 INTEGER
);

INSERT INTO veredas (nombre, rio, poblacion, total, casos_2022, casos_2023, casos_2024, casos_2025) VALUES
('Belén', 'Napi', 689, 1285, 86, 591, 501, 107),
('El Carmelo', 'Guajuí', 850, 902, 282, 221, 364, 35),
('San José de Guare', 'Guajuí', 588, 502, 135, 154, 188, 25),
('Limones', 'Guajuí', 1392, 187, 26, 36, 81, 44),
('Santa Rosa', 'Guajuí', 249, 138, 42, 60, 24, 12),
('Calle Larga', 'Napi', 387, 129, 1, 35, 61, 32),
('Quiroga', 'Guajuí', 927, 89, 17, 17, 20, 35),
('San Agustín', 'Napi', 343, 55, 18, 36, 1, 0);

DROP TABLE IF EXISTS municipio_evento_460;
CREATE TABLE municipio_evento_460 (
  municipio TEXT,
  anio INTEGER,
  casos_confirmados INTEGER,
  PRIMARY KEY (municipio, anio)
);

INSERT INTO municipio_evento_460 (municipio, anio, casos_confirmados) VALUES
('Guapi', 2018, 5), ('Guapi', 2019, 0), ('Guapi', 2020, 0), ('Guapi', 2021, 3),
('Guapi', 2022, 1), ('Guapi', 2023, 1), ('Guapi', 2024, 5), ('Guapi', 2025, 12),
('Timbiquí', 2018, 18), ('Timbiquí', 2019, 2), ('Timbiquí', 2020, 2), ('Timbiquí', 2021, 0),
('Timbiquí', 2022, 0), ('Timbiquí', 2023, 2), ('Timbiquí', 2024, 5), ('Timbiquí', 2025, 1),
('López de Micay', 2018, 0), ('López de Micay', 2019, 0), ('López de Micay', 2020, 0), ('López de Micay', 2021, 0),
('López de Micay', 2022, 0), ('López de Micay', 2023, 0), ('López de Micay', 2024, 1), ('López de Micay', 2025, 1);
''')

print('\n=== ANUAL ===')
print(pd.read_sql_query('SELECT * FROM anual ORDER BY anio', conn))

print('\n=== ZONA ===')
print(pd.read_sql_query('SELECT zona, SUM(casos) AS total_casos FROM zona GROUP BY zona ORDER BY total_casos DESC', conn))

print('\n=== VEREDAS ===')
print(pd.read_sql_query('''
SELECT nombre, rio, poblacion, total,
       ROUND((casos_2024 * 1000.0) / poblacion, 2) AS tasa_2024
FROM veredas
ORDER BY tasa_2024 DESC
''', conn))

print('\n=== TENDENCIA POR VEREDA ===')
print(pd.read_sql_query('''
SELECT nombre, casos_2022, casos_2023, casos_2024, casos_2025,
       (casos_2024 - casos_2023) AS cambio_2024_vs_2023
FROM veredas
ORDER BY total DESC
''', conn))

print('\n=== EVENTO 460 POR MUNICIPIO Y AÑO ===')
print(pd.read_sql_query('''
SELECT municipio, anio, casos_confirmados
FROM municipio_evento_460
ORDER BY anio, municipio
''', conn))

conn.close()
