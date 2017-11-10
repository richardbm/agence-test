SELECT *
FROM cao_os
INTO OUTFILE '/tmp/cao_os10.csv'
CHARACTER SET utf8
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
ESCAPED BY '\\'
LINES TERMINATED BY '\n';

SELECT *
FROM cao_usuario
INTO OUTFILE '/tmp/cao_usuario4.csv'
CHARACTER SET utf8
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
ESCAPED BY '\\'
LINES TERMINATED BY '\n';

SELECT *
FROM cao_salario
INTO OUTFILE '/tmp/cao_salario5.csv'
CHARACTER SET utf8
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
ESCAPED BY '\\'
LINES TERMINATED BY '\n';

SELECT *
FROM permissao_sistema
INTO OUTFILE '/tmp/permissao_sistema5.csv'
CHARACTER SET utf8
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
ESCAPED BY '\\'
LINES TERMINATED BY '\n';


UPDATE  cao_os SET dt_sol=NULL  WHERE dt_sol LIKE '%0000%';


source /home/richard/Documentos/paquete_evaluacion_es/datos.sql