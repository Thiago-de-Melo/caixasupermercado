import csv
def grava(a):
    with open('dict.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Valor","Produto"])
        for key, value in a.items():
            writer.writerow([key, value])
