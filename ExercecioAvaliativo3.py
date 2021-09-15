import random  # random é uma biblioteca que ajuda a fazer escolhas aleatorias
# a ideia deste algoritio é solucionar o problema de sorteio de um ganhador.
# foi utilizado nele os dados do aluno e seu RU da Uninter.
doador = input('Nome do doador:') # nessa variável, pede se ao usuário iserir o nome de quem está participando do sorteio
lista = ['jardel', 'batista', 'cruz', 5 , 0]
random.shuffle(lista)
sorteado = random.choice(lista)
print(random.choice(lista))
