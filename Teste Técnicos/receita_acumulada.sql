-- Script SQL para cálculo de receita acumulada mês a mês em 2023
-- Situação: Projeto com a Secretaria da Fazenda para análise de receitas
-- Objetivo: Calcular a receita acumulada para planejamento do próximo período

-- A função SUM(...) OVER (ORDER BY ...) permite realizar a soma acumulativa
-- dos valores da coluna actual_revenue, mantendo a ordem cronológica dos meses.

-- ORDER BY period ASC para garantir que a soma seja crescente no tempo.

SELECT
    actual_revenue,
    SUM(actual_revenue) OVER (ORDER BY period ASC) AS cumulative_revenue,
    period
FROM
    revenue;

-- Explicação:
-- Esta query calcula a receita acumulada mês a mês ao longo do ano de 2023.
-- A cláusula OVER (ORDER BY period ASC) faz com que a soma seja realizada do primeiro mês (janeiro)
-- até o último (junho), exatamente como esperado para o planejamento orçamentário.
