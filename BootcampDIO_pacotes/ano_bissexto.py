def verificador_ano_bissexto():
    ano = int(input())
    if (ano % 4) == 0 and (ano % 100) != 0:
      resultado = "SIM"
    else:
      resultado = "NÃO"
  
    print(resultado)

# TODO: Verifique se o ano é bissexto utilizando uma estrutura de controle condicional, como if/else:


verificador_ano_bissexto()