import tkinter as tk

def calculate():
    # Obtenha o valor dos campos de entrada
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())

    # Obtenha o valor do botão de operação pressionado
    operation = operation_var.get()

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    elif operation == "%":
        result = num1 * num2 /100
    else:
        result = "Operação Inválida"

    # Exiba o resultado
    result_label.config(text="Resultado: " + str(result))

# Crie uma janela principal
root = tk.Tk()
root.title("MatPy")

# Crie os campos de entrada para os números
num1_entry = tk.Entry(root)
num1_entry.grid(row=0, column=0, padx=10)
num2_entry = tk.Entry(root)
num2_entry.grid(row=1, column=0)

# Crie as opções de operação
operation_var = tk.StringVar(value="+")
operation_dropdown = tk.OptionMenu(root, operation_var, "+", "-", "*", "/","%")
operation_dropdown.grid(row=0, column=1, padx=10, pady=15)

# Crie o botão de calcular
calculate_button = tk.Button(root, text="Calcular", command=calculate)
calculate_button.grid(row=2, column=0, padx=10, pady=15)

# Crie a etiqueta para exibir o resultado
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0)

# Inicie o loop de eventos
root.mainloop()