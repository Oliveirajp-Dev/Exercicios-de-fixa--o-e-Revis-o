informacoes = [(1, 'NATHANIEL FORD', 'GENERAL MANAGER-METROPOLITAN TRANSIT AUTHORITY', 167411.18, 0.0, 400184.25, None, 567595.43, 567595.43, 2011, '', 'San Francisco', ''), (2, 'GARY JIMENEZ', 'CAPTAIN III (POLICE DEPARTMENT)', 155966.02, 245131.88, 137811.38, None, 538909.28, 538909.28, 2011, '', 'San Francisco', ''), (3, 'ALBERT PARDINI', 'CAPTAIN III (POLICE DEPARTMENT)', 212739.13, 106088.18, 16452.6, None, 335279.91, 335279.91, 2011, '', 'San Francisco', ''), (4, 'CHRISTOPHER CHONG', 'WIRE ROPE CABLE MAINTENANCE MECHANIC', 77916.0, 56120.71, 198306.9, None, 332343.61, 332343.61, 2011, '', 'San Francisco', ''), (5, 'PATRICK GARDNER', 'DEPUTY CHIEF OF DEPARTMENT,(FIRE DEPARTMENT)', 134401.6, 9737.0, 182234.59, None, 326373.19, 326373.19, 2011, '', 'San Francisco', ''), (6, 'DAVID SULLIVAN', 'ASSISTANT DEPUTY CHIEF II', 118602.0, 8601.0, 189082.74, None, 316285.74, 316285.74, 2011, '', 'San Francisco', ''), (7, 'ALSON LEE', 'BATTALION CHIEF, (FIRE DEPARTMENT)', 92492.01, 89062.9, 134426.14, None, 315981.05, 315981.05, 2011, '', 'San Francisco', ''), (8, 'DAVID KUSHNER', 'DEPUTY DIRECTOR OF INVESTMENTS', 256576.96, 0.0, 51322.5, None, 307899.46, 307899.46, 2011, '', 'San Francisco', ''), (9, 'MICHAEL MORRIS', 'BATTALION CHIEF, (FIRE DEPARTMENT)', 176932.64, 86362.68, 40132.23, None, 303427.55, 303427.55, 2011, '', 'San Francisco', ''), (10, 'JOANNE HAYES-WHITE', 'CHIEF OF DEPARTMENT, (FIRE DEPARTMENT)', 285262.0, 0.0, 17115.73, None, 302377.73, 302377.73, 2011, '', 'San Francisco', '')]
descricao = (('Id', "<class 'int'>", None, 10, 10, 0, True), ('EmployeeName', "<class 'str'>", None, 65536, 65536, 0, True), ('JobTitle', "<class 'str'>", None, 65536, 65536, 0, True), ('BasePay', "<class 'float'>", None, 54, 54, 0, True), ('OvertimePay', "<class 'float'>", None, 54, 54, 0, True), ('OtherPay', "<class 'float'>", None, 54, 54, 0, True), ('Benefits', "<class 'float'>", None, 54, 54, 0, True), ('TotalPay', "<class 'float'>", None, 54, 54, 0, True), ('TotalPayBenefits', "<class 'float'>", None, 54, 54, 0, True), ('Year', "<class 'int'>", None, 10, 10, 0, True), ('Notes', "<class 'str'>", None, 65536, 65536, 0, True), ('Agency', "<class 'str'>", None, 65536, 65536, 0, True), ('Status', "<class 'str'>", None, 65536, 65536, 0, True))
import pandas as pd

colunas=[]
for tupla in descricao:
    colunas.append(tupla[0]) # pega o indice 0 de todas as tuplas dentro de DESCRIÇÃO
    
tabela= pd.DataFrame.from_records(informacoes,columns=colunas)
print(tabela)

# precisamos enviar por e-mail para o RH uma lista com o nome e o cargo de cada pessoa da tabela 
texto= 'RH, segue a lista dos funcionarios'
# passo a passo
    # - para cada item da nossa lista de informações 
        # - pegar o nome do funcionario -> tupla[1]
        # - pegar o cargo do funcionario -> tupla[2]
        # - adicionar uma nova linha no texto com nome do funcionario e cargo
        
for item in informacoes:
    nome_funcionario= item[1]
    cargo_funcionario= item[2]
    texto= texto + f"\n{nome_funcionario}, Cargo: {cargo_funcionario}"
print(texto)