# A função print!

# usada para escrever coisas na tela.
# recebe argumentos, pode ser mais de 1 separado por virgula
# Existem argumentos nomeados e não nomeados, argumentos nomeados recebem algum "comando"

print(10, 20, 'Lucas')

print('Arroz', "Feijão", sep=' e ') # 'sep' argumento nomeado que define o tipo de separação do que será exibido

print('Arroz', "Feijão", sep='+')

print(5, 10, sep='-', end='**') # end define o que será exibido no final do print, por padrao é a quebra de linha "\n"
print(20, 15, sep='-')

print(6, 9, sep='-', end='**\n') 
print(29, 65, sep='-')