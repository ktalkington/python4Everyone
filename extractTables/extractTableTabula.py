import tabula
import os
import sys

# Read PDF table
# Reverse comments below to pass pdf via command line
#tables = tabula.read_pdf(sys.argv[1], pages="all")
tables = tabula.read_pdf("pdfs/Bashir-2018.pdf", pages="all")

# Save tables to directory
folder_name = "tables"

if not os.path.isdir(folder_name):
    os.mkdir(folder_name)

# Iterate over extracted tables
for i, table in enumerate(tables, start=1):
    table.to_excel(os.path.join(folder_name, f"table_{i}.xlsx"), index=False)

tabula.convert_into_by_batch("pdfs", output_format="csv", pages="all")