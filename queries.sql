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

CREATE TABLE zona (
  anio TEXT,
  zona TEXT,
  casos INTEGER
);

INSERT INTO zona (anio, zona, casos) VALUES
('2022', 'Urbana', 103), ('2023', 'Urbana', 334), ('2024', 'Urbana', 150), ('2025', 'Urbana', 58),
('2022', 'Periurbana', 282), ('2023', 'Periurbana', 947), ('2024', 'Periurbana', 288), ('2025', 'Periurbana', 98),
('2022', 'Rural', 932), ('2023', 'Rural', 1432), ('2024', 'Rural', 1571), ('2025', 'Rural', 423);

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
('Limones', 'Guajuí', 1392, 187, 26, 36, 81, 44);

SELECT * FROM anual ORDER BY anio;
SELECT zona, SUM(casos) AS total_casos FROM zona GROUP BY zona ORDER BY total_casos DESC;
SELECT nombre, rio, casos_2024, poblacion, ROUND((casos_2024 * 1000.0) / poblacion, 2) AS tasa_2024
FROM veredas
ORDER BY tasa_2024 DESC;
