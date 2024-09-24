idade = int(input("Qual a sua idade?\n"))

if idade >= 18:
    print("Você é maior de idade.")
elif 13 <= idade < 18:
    print("Você é adolescente.")
else:
    print("Você é menor de idade.")