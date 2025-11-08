# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento. 🇧🇷
# Write an algorithm that reads an employee's salary and displays their new salary, which includes a 15% increase. 🇺🇸
# Escriba un algoritmo que lea el salario de un empleado y muestre su nuevo salario, que incluye un aumento del 15%. 🇪🇸
# Écrivez un algorithme qui lit le salaire d'un employé et affiche son nouveau salaire, qui inclut une augmentation de 15 %. 🇫🇷

salario = float(input("Enter an employee's salary: R$ "))
novo_salario = salario + (salario * 0.15)
print(f"This employee received a 15% raise in their salary; their new salary is R$ {novo_salario:.2f}.")
