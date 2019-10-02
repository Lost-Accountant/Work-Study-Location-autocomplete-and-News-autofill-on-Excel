import pandas as pd
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter

# load main worksheet
main_file = 'Kevin-coded-edited.xlsx'
main_book = load_workbook(filename=main_file)
main_sheet = main_book.active

# dictionaries for agents
ref_file = 'LAND - Variable dictionary.xlsx'
ref_book = load_workbook(filename=ref_file)
ref_sheet = ref_book.active

agents = {}

# Populate dict "agents"
for row in range(2, 9):
    agents[ref_sheet['A' + str(row)].value] = []
    col_ch = 'B'
    for col in range(2, len(ref_sheet[row])):
        if ref_sheet[col_ch + str(row)].value is not None:
            # Use this check to avoid filtering later to find None values
            agents[ref_sheet['A' + str(row)].value].append(
                ref_sheet[col_ch + str(row)].value)
        col_ch = chr(ord(col_ch) + 1)

print(agents)

# c1 = sheet['E3'].value
# c2 = sheet['E'+str(3)].value

# print(c1==c2)
