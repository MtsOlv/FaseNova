anoATL = int(input('Informe o ano em que estamos: '))
anoNASC = int(input('Informe o ano em que a pessoa nasceu: '))
meses = (anoATL - anoNASC) * 12
dias = (anoATL - anoNASC) * 365
print(f'A idade da pessoa em meses é de {meses} meses, logo, a idade em dias é igual de {dias} dias.')
