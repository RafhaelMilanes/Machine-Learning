import pandas as pd
import matplotlib.pyplot as plt

# Carregando dados do arquivo 'dados4.csv' para uma tabela chamada DataFrame
df = pd.read_csv('dados4.csv')

# Ajustando idades que estão faltando ou são estranhas para a idade que aparece mais vezes (moda)
# fillna é usado para substituir valores ausentes
moda_idade = df['age'].mode()[0]
df['age'].fillna(moda_idade, inplace=True)

# Salvando a saída no arquivo Resposta01.txt
# 'df' carreguei o Data Frame anterior. 
# 'to_string' representação do DataFrame em uma string.
# 'index=False' não incluir os índices (números de linha) no arquivo, apenas os dados.
# 'file.write' escrever a string gerada pelo to_string no arquivo 'Resposta01.txt'.
with open('Resposta01.txt', 'w') as file:
    file.write(df.to_string(index=False))

# Contando quantos homens e quantas mulheres existem na tabela
somatorio_genero = df['sex'].value_counts()
print("Somatório de homens (male):", somatorio_genero['male'])
print("Somatório de mulheres (female):", somatorio_genero['female'])

# Contando quantas pessoas sobreviveram e quantas não sobreviveram
sobreviventes = df['survived'].value_counts()

# Fazendo um gráfico redondo (como uma pizza) para mostrar a porcentagem de quem sobreviveu e quem não
# labels = ['Não Sobreviventes', 'Sobreviventes'] Define as legendas
# sobreviventes: É a variável que contém a contagem de sobreviventes e não sobreviventes.
# labels=labels: Usa os rótulos definidos anteriormente.
# autopct='%1.1f%%': Adiciona as porcentagens nos setores da pizza.
# startangle=90: Define o ângulo inicial para começar a desenhar os setores.
# plt.axis('equal'): Garante que o gráfico de pizza seja desenhado como um círculo perfeito,
# plt.title('Porcentagem de Sobreviventes e Não Sobreviventes'): Adiciona um título ao gráfico.
# plt.show(): Exibe o gráfico.
labels = ['Não Sobreviventes', 'Sobreviventes']
plt.pie(sobreviventes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('Porcentagem de Sobreviventes e Não Sobreviventes')
plt.show()

# Convertendo 'age' e 'fare' para tipo numérico
df['age'] = pd.to_numeric(df['age'], errors='coerce')
df['fare'] = pd.to_numeric(df['fare'], errors='coerce')

# Fazendo um gráfico que mostra a relação entre a idade e o preço pago (tarifa)
plt.scatter(df['age'], df['fare'], alpha=0.5)
plt.xlabel('Idade')
plt.ylabel('Tarifa')
plt.title('Gráfico de Dispersão: Idade pela Tarifa')
plt.show()
