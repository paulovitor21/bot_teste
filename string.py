import locale

# Definindo o locale para o formato de moeda dos Estados Unidos
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

def format_to_dollar(number_str):
    if ',' in number_str:
        # Remover vírgulas para converter corretamente
        number_str = number_str.replace(',', '')
    
    try:
        # Convertendo a string para float
        number_float = float(number_str)
        
        # Formatando o número como dólar
        formatted_number = locale.currency(number_float, grouping=True)
        return formatted_number
    except ValueError:
        return "Número inválido"

# Exemplo de uso
number = "1,234.56"  # Número com vírgula como separador de milhar
formatted_number = format_to_dollar(number)
print(formatted_number)  # Resultado: $1,234.56

number = "1234.56"  # Número sem vírgula
formatted_number = format_to_dollar(number)
print(formatted_number)  # Resultado: $1,234.56