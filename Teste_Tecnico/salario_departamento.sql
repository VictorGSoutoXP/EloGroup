-- Script SQL para classificar funcionários por salário dentro de cada departamento
-- e calcular total de funcionários e salário médio por departamento

SELECT 
    departament, 
    name, 
    last_name, 
    salary, 
    RANK() OVER (PARTITION BY departament ORDER BY salary DESC) AS ranking,
    COUNT(*) OVER (PARTITION BY departament) AS total_funcionarios,
    AVG(salary) OVER (PARTITION BY departament) AS salario_medio
FROM employee;

-- Explicação:
-- RANK() OVER (PARTITION BY departament ORDER BY salary DESC): classifica os funcionários do maior para o menor salário dentro do departamento.
-- COUNT(*) OVER (PARTITION BY departament): conta quantos funcionários há em cada departamento.
-- AVG(salary) OVER (PARTITION BY departament): calcula o salário médio por departamento.
