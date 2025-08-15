#importando pandas para manipulação de dados
import pandas as pd

#listas para armazenar os dados
livros = []
paginas = []          
autores = []

#início do programa
print("\nOlá, vamos falar sobre os livros que você tem lido!")
while True:
    try:
        quantidade = int(input("Quantos livros você leu ano passado? "))
        if quantidade <= 0:
            print("Que pena, vamos ler mais esse ano!")
            continue
        break
    except ValueError:
        print("Por favor, insira um número válido.")

#loop for para coletar os dados das leituras
for i in range(quantidade):
    livro = input(f"\nDigite o nome do livro {i + 1}: ")
    while True:
        try:
             autor = input(f"\nDigite o nome do autor do livro {livro}: ")
             if autor == "":
                 print("O nome do autor está vazio, tente novamente.")
                 continue
             break
        except ValueError:
            print("Por favor, insira um nome válido.")
   
    while True:
        try:
            pagina = int(input(f"\nDigite o número de páginas de {livro}:"))
            if pagina <= 0:
                print("Digite um número válido de páginas.")
                continue
            break
        except ValueError:
            print("Por favor, insira um número válido.")
#adicionando os dados às listas
    livros.append(livro)
    autores.append(autor)
    paginas.append(pagina)

#estrutura de decisão para avaliar o número de páginas
    if pagina > 300:
        print(f"Nossa, {livro} é um grande livro!")
    elif pagina == 300:
        print(f"{livro} é um livro razoável")
    else:
        print(f"{livro} é um livro curto, mas bom.")

#calculando a média, o livro mais longo e o mais curto
media = sum(paginas) / len(paginas)
mais_longo = max(paginas)
mais_curto = min(paginas)
maior_livro = livros[paginas.index(mais_longo)]
menor_livro = livros[paginas.index(mais_curto)]

#exibindo o resumo das leituras
print("\nResumo das suas Leituras:")
print(f"Média das páginas dos livros: {media:.2f}")
print(f"O livro mais longo que você leu foi {maior_livro} com {mais_longo} pags.")
print(f"O livro mais curto que você leu foi {menor_livro} com {mais_curto} pags.")

#criando dataframe e salvando os dados em um arquivo CSV
df = pd.DataFrame({'Livro': livros, 'Páginas': paginas, 'Autor': autores})
print("\nDados das suas Leituras:")
print(df)

df.to_csv('Leituras.csv', index=False, encoding='utf-8')
print("\nDados salvos em 'Leituras.csv'.")

#importando matplotlib para visualização gráfica
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5,))
plt.bar(livros, paginas, color= "skyblue")
plt.xlabel('Livros')
plt.ylabel('Número de Páginas')
plt.title('Número de Páginas por Livro')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
