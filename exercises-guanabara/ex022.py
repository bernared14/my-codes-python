# Crie um programa que leia o nome completo de uma pessoa e mostre: o nome com todas as letras maiúsculas e minúsculas, quantas letras ao todo (sem considerar espaços) e quantas letras tem o primeiro nome. 🇧🇷
# Create a program that reads a person's full name and shows: the name in all uppercase and lowercase letters, how many letters in total (excluding spaces), and how many letters are in the first name. 🇺🇸
# Crea un programa que lea el nombre completo de una persona y muestre: el nombre con todas las letras en mayúsculas y minúsculas, cuántas letras hay en total (sin contar los espacios) y cuántas letras tiene el primer nombre. 🇪🇸
# Créez un programme qui lit le nom complet d’une personne et affiche : le nom avec toutes les lettres en majuscules et en minuscules, le nombre total de lettres (sans compter les espaces) et le nombre de lettres du prénom. 🇫🇷

nome = str(input("Enter a full name: ")).strip()

print(f" — The full name with all uppercase letters is: {nome.upper()}")
print(f" — The full name with all lowercase letters is: {nome.lower()}")
print(f" — There are {len(nome.replace(' ', ''))} letters in the full name.")
print(f" — There are {len(nome.split()[0])} letters in the first name.")
