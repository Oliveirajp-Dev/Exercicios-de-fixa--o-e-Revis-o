# 1 - imposto a pagar no lucro presumido

## - 5% sobre faturamento de ISS (mensal)
## - 0,65% de pis sobre faturamento (mensal)
## - 3% de cofins sobre faturamento (mensal)
## - 4.8% de IR(trimestral)
## - 10% de IR adicional sobre o que ultrapassar 20 mil do faturamento (trimestral)
## - 2,88% de CSLL sobre faturamento (trimestral)

faturamento ={
    "janeiro": 'R$ 10.000,00',
    'fevereiro': 'R$ 20.000,00',
    'marco': 'R$ 30.000,00',
    'abril': 'R$ 40.000,00',
    'maio': 'R$ 50.000,00',
    'junho': 'R$ 60.000,00',
    'julho': 'R$ 70.000,00',
    'agosto': 'R$ 80.000,00',
    'setembro': 'R$ 90.000,00',
    'outubro': 'R$ 100.000,00',
    'novembro': 'R$ 110.000,00',
    'dezembro': 'R$ 120.000,00'
}

def transforma_numero(texto):
    texto = texto.replace('R$', '')
    texto = texto.replace(' ', '')
    texto = texto.replace('.', '')
    texto = texto.replace(',', '.')
    valor=float(texto)
    return valor
    
def calcular_imposto_mensal(valor_faturamento):
    iss= valor_faturamento * 0.05
    pis= valor_faturamento * 0.0065
    cofins= valor_faturamento * 0.03
    imposto_mensal= iss + pis + cofins
    return imposto_mensal
    
    
    
def calcular_imposto_trimestral(valor_faturamento): 
    ir = valor_faturamento * 0.048
    csll = valor_faturamento * 2.88
    adicional_ir=0
    if valor_faturamento > 20000:
        adicional_ir=(valor_faturamento - 20000)*0.1
    imposto_trimestral= ir + csll + adicional_ir
    
    return imposto_trimestral
   
resultados={}
for mes in faturamento:
    valor_faturamento=transforma_numero(faturamento[mes])
    imposto_mensal = calcular_imposto_mensal(valor_faturamento)
    imposto_trimestral = calcular_imposto_trimestral(valor_faturamento)
    resultados[mes] = (valor_faturamento,imposto_mensal,imposto_trimestral)

print(resultados)
