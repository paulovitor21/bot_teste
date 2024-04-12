import os

# Supõe que DATA_SEGUNDA_FEIRA é uma variável previamente definida que contém uma data.
date_str = DATA_SEGUNDA_FEIRA.strftime("%Y-%m-%d")
filename = f"{date_str}_onhand_inquiry.csv"
filepath = os.path.join(output_path, filename)

bot.kb_type(filepath)
