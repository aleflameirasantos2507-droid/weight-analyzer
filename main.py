highest = 0
lowest = 0

for i in range(1, 6):
    weight = float(input('What is the {}th weight? '.format(i)))

    if i == 1:
        lowest = weight
        highest = weight

    elif weight > highest:
        highest = weight

    elif weight < lowest:
        lowest = weight

print('The highest weight is {} and the lowest weight is {}'.format(highest, lowest))
