import pandas as pd
import matplotlib.pyplot as plt

# Dados de uso do celular (em horas) e produtividade (escala 0 a 10)
dados = {
    "Dia": ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"],
    "Uso_Celular": [5, 4.5, 6, 5.5, 7, 8, 6.5],
    "Produtividade": [8, 7.5, 6, 6.5, 5, 3, 4]
}

# Criar DataFrame
df = pd.DataFrame(dados)
print(df)

# Calcular médias
media_celular = df["Uso_Celular"].mean()
media_produtividade = df["Produtividade"].mean()

print(f"\nMédia de uso do celular: {media_celular:.2f} horas")
print(f"Média de produtividade: {media_produtividade:.2f} (escala de 0 a 10)")

# Criar gráfico de linhas
plt.figure(figsize=(10, 6))
plt.plot(df["Dia"], df["Uso_Celular"], label="Uso do Celular (h)", marker='o', color='blue')
plt.plot(df["Dia"], df["Produtividade"], label="Produtividade", marker='s', color='green')

# Adicionar título e rótulos
plt.title("Uso do Celular vs Produtividade")
plt.xlabel("Dia da Semana")
plt.ylabel("Valor")
plt.legend()
plt.grid(True)

# Exibir gráfico
plt.tight_layout()
plt.show()
