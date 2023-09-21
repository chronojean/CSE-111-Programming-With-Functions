def print_list(lista, sorted_by_column=0, row_separator="-", column_separator="|"):
    for i in range(len(lista)):
        row = lista[i]
        for j in range(len(row)):
            column = row[j]
            print(column, end="") if isinstance(column, str) else None
            for k in range(12 - len(str(column))):
                print(" ", end="")if not(i==0 and j==sorted_by_column) else print("♦",end="")
            print(column, end="") if not isinstance(column, str) else None
            print(column_separator, end="")
        print() if row_separator != "" and column_separator != "" else None
        for x in range(len(row) * 12):
            print(column_separator, end="") if x > 0 and x % 12 == 0 else None
            print(row_separator, end="")
        print(row_separator)

# Lista original
cans = [['Name', 'Radius cm', 'Height cm', 'Cost/Can $', 'Volume cm3', 'Surface cm3', 'Stor. Eff.', 'Cost Eff $'],
        ['#1 Picnic', 6.83, 10.16, 0.28, 1488.97, 729.11, 2.04, 5317.75],
        ['#1 Tall', 7.78, 11.91, 0.43, 2264.75, 962.51, 2.35, 5266.86],
        ['#2', 8.73, 11.59, 0.45, 2774.99, 1114.6, 2.49, 6166.64],
        ['#2.5', 10.32, 11.91, 0.61, 3984.93, 1441.45, 2.76, 6532.67],
        ['#3 Cylinder', 10.79, 17.78, 0.86, 6503.16, 1936.92, 3.36, 7561.81],
        ['#5', 13.02, 14.29, 0.83, 7610.34, 2234.15, 3.41, 9169.08],
        ['#6Z', 5.4, 8.89, 0.22, 814.4, 484.85, 1.68, 3701.82],
        ['#8Z short', 6.83, 7.62, 0.26, 1116.73, 620.11, 1.8, 4295.12],
        ['#10', 15.72, 17.78, 1.53, 13803.42, 3308.85, 4.17, 9021.84],
        ['#211', 6.83, 12.38, 0.34, 1814.31, 824.38, 2.2, 5336.21],
        ['#300', 7.62, 11.27, 0.38, 2055.81, 904.41, 2.27, 5410.03],
        ['#303', 8.1, 11.11, 0.42, 2289.99, 977.67, 2.34, 5452.36]]
copied_cans = cans.copy()
copied_cans[2] = []
print_list(cans)