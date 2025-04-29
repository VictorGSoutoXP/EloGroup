-- Script SQL para encontrar o consultor com a maior venda anual (2021, 2022, 2023)
-- Situação: Auditoria interna da EloGroup para identificar os consultores com melhor desempenho por ano
-- Objetivo: Usar ROW_NUMBER() com PARTITION BY year para encontrar o top 1 de cada ano

WITH CTE AS (
  SELECT 
    year, consultant_name, sale_amount, branch,
    ROW_NUMBER() OVER (PARTITION BY year ORDER BY sale_amount DESC) AS row_number
  FROM yearly_sales
)
SELECT year, consultant_name 
FROM CTE 
WHERE row_number = 1;

-- Explicação:
-- A função ROW_NUMBER() é usada para classificar os registros dentro de cada ano (PARTITION BY year),
-- ordenando as vendas do maior para o menor (ORDER BY sale_amount DESC).
-- O WHERE row_number = 1 garante que estamos selecionando apenas o consultor com a maior venda em cada ano.

-- Resultado esperado:
-- 2021 | Pablo Ramos
-- 2022 | Celia Matos
-- 2023 | Giovanni Belo