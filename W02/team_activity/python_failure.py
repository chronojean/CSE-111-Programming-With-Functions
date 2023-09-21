def to_float(element):
    try:
        converted = float(element)
        return converted
    except:
        return element

cans = [['#5', '13.02', '14.29', '$0.83'], ['#8Z short', '6.83', '7.62', '$0.26'], ['#10', '15.72', '17.78', '$1.53']]
print(cans)
print("---------------------------------")
array = [set(to_float(column.strip("$")) for column in can) for can in cans]

print(array)
