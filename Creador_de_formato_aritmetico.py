def arithmetic_arranger(problems,show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    primera_linea = []
    segunda_linea = []
    guiones = []
    respuestas = []

    for problem in problems:
        partes = problem.split()

        if partes[1] not in ["+","-"]:
            return "Error: Operator must be '+' or '-'."
        if not (partes[0].isdigit() and partes[2].isdigit()): 
            return 'Error: Numbers must only contain digits.'
        if len(partes[0]) > 4 or len(partes[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        operador_1 = partes[0]
        operador = partes[1]
        operador_2 = partes[2]
            
        if partes[1] == "+":
            resultado = int(operador_1) + int(operador_2)
        else:
            resultado = int(operador_1) - int(operador_2)
            
        ancho = max(len(operador_1), len(operador_2)) + 2

        primera_linea.append(operador_1.rjust(ancho))
        segunda_linea.append(operador + operador_2.rjust(ancho - 1))
        guiones.append("-" * ancho)
        respuestas.append(str(resultado).rjust(ancho))
            
    problemas_ordenados = (
    "    ".join(primera_linea) + "\n" +
    "    ".join(segunda_linea) + "\n" +
    "    ".join(guiones) )
    if show_answers:
            problemas_ordenados += "\n" + "    ".join(respuestas)

    return problemas_ordenados

    return problems

print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"],True)}')
