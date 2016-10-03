import StrinUtil

texto = input("Digite um texto aqui:\n")

StrinUtil.output(StrinUtil.tamanho(texto))
StrinUtil.output(StrinUtil.maiusculo(texto))
StrinUtil.output(StrinUtil.minusculo(texto))

letra = input("Informe uma letra:\n")
StrinUtil.encontrarLetra(letra, texto)