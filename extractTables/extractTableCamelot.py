import camelot

# Read PDF table
# Reverse comments below to pass pdf via command line
#tables = camelot.read_pdf(sys.argv[1])
#tables = camelot.read_pdf("pdfs/table_areas.pdf", flavor='stream', table_areas=['316,499,566,337'])
#tables = camelot.read_pdf("pdfs/Bashir-2018.pdf", flavor='stream', table_areas=['243,389,2240,950'])
tables = camelot.read_pdf("pdfs/Bashir-2018.pdf", flavor='stream')

#number of tables extracted
print("Total tables extracted:", tables.n)

# print the first table as Pandas DataFrame
print(tables[0].df)

# export individually as CSV
tables[0].to_csv("tables/table1.csv")