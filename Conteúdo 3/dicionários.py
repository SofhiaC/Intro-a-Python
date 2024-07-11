#exercício 1
pessoa = {'nome':'Sofhia', 'idade':17, 'cidade':'Curitiba'}

#exercício 2
pessoa['idade'] = 18
pessoa.update({'profissão': 'Programadora'})
del pessoa['cidade']
print(pessoa)

#exercício 3 
dicionario_numeros_e_quadrados = {x: x**2 for x in range (1, 6)}
print(dicionario_numeros_e_quadrados)

#exercício 4
dicionario = {'doce':'bala, chocolate', 'salgado':'coxinha, arroz'}

if 'salgado' in dicionario:
    print("A chave 'salgado' se encontra no dicionário.")
else: 
    print("A chave 'salgado' não se encontra no dicionário.")

#exercício 5
frase = 'Se Deus tivesse concedido todas as orações que eu fiz na miha vida, onde eu estaria agora?'
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)