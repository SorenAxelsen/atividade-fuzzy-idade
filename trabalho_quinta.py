import numpy as np
import matplotlib.pyplot as plt


def gbellmf(x, a, b, c):
    return 1 / (1 + np.abs((x - c) / a) ** (2 * b))


def jovem(x):
    return gbellmf(x, a=10, b=4, c=15)

def adulto(x):
    return gbellmf(x, a=10, b=4, c=40)

def idoso(x):
    return gbellmf(x, a=10, b=4, c=70)


idade = float(input("Digite uma idade entre 0 e 90: "))


mu_jovem = jovem(idade)
mu_adulto = adulto(idade)
mu_idoso = idoso(idade)


print(f"\nIdade: {idade}")
print(f"Grau de pertinência Jovem: {mu_jovem:.3f}")
print(f"Grau de pertinência Adulto: {mu_adulto:.3f}")
print(f"Grau de pertinência Idoso: {mu_idoso:.3f}")


grupos = {"Jovem": mu_jovem, "Adulto": mu_adulto, "Idoso": mu_idoso}
grupo_max = max(grupos, key=grupos.get)
print(f"=> A idade {idade} pertence mais ao grupo: {grupo_max}")


x = np.linspace(0, 90, 500)
y_jovem = jovem(x)
y_adulto = adulto(x)
y_idoso = idoso(x)

plt.figure(figsize=(10,6))
plt.plot(x, y_jovem, label="Jovem", color="blue")
plt.plot(x, y_adulto, label="Adulto", color="green")
plt.plot(x, y_idoso, label="Idoso", color="red")


plt.axvline(idade, color="black", linestyle="--", alpha=0.7)
plt.scatter([idade], [mu_jovem], color="blue")
plt.scatter([idade], [mu_adulto], color="green")
plt.scatter([idade], [mu_idoso], color="red")

plt.title("Conjuntos Fuzzy - Idade")
plt.xlabel("Idade")
plt.ylabel("Grau de Pertinência")
plt.legend()
plt.grid(True)
plt.show()
