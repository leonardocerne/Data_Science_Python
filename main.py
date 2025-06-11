arq1 = open("arq2.csv", "r")
data = arq1.read()
rows = data.split("\n")
full_data = []
for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)
names = []
for i in range(len(full_data)):
    if(i != 0):
        if(names.count(full_data[i][2]) == 0):
            names.append(full_data[i][2])
print("\n\nLISTA DE NOMES:\n")
for n in names:
    print(n)