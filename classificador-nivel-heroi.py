import random

#variáveis
heroName = ""
heroXP = 0
heroLevel = ""

#definindo nome e XP do herói
print("\n")
print("=========================================================")
print("============ CLASSIFICADOR DE NÍVEL DO HERÓI ============")
print("=========================================================")
print("\n")

heroName = input("Digite um nome para nosso herói: ")
heroXP = random.randint(0, 11000)

#defiindo Nível do Herói
if heroXP <= 1000:
    heroLevel = "Ferro"
elif heroXP > 1000 and heroXP <= 2000:
    heroLevel = "Bronze"
elif heroXP > 2000 and heroXP <= 5000:
    heroLevel = "Prata"
elif heroXP > 5000 and heroXP <= 7000:
    heroLevel = "Ouro"
elif heroXP > 7000 and heroXP <= 8000:
    heroLevel = "Platina"
elif heroXP > 8000 and heroXP <= 9000:
    heroLevel = "Ascendente"
elif heroXP > 9000 and heroXP <= 10000:
    heroLevel = "Imortal"
elif heroXP > 10000:
    heroLevel = "Radiante"

#output de dados
print("\n")
print("================= NÍVEL DO HERÓI =================")
print("\n")
print("O  herói de nome ", heroName, " possui ", heroXP, " de XP!")
print("O herói de nome ", heroName, " está no Nível ", heroLevel, "!")
print("\n")
print("==================================================")
