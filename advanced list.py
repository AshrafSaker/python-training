c = ['$', '£', '€', '¥']
print(c[-2:])
print(c[-3:-1])

vehicle = 'motorbike'
print(vehicle[-4:])

c = ['$', '£', '€', '¥']
print(c[1:-1])

c = ['$', '£', '€', '¥']
print(c[0:-2])

c = ['$', '£', '€', '¥']
c[1] = '₣'
print(c)

c = ['$', '£', '€', '¥']
c[:2] = ['₣', '฿']
print(c)

vehicle = 'airplane'
#vehicle[:3] = 'water'
print(vehicle)

vehicle = 'airplane'
vehicle[:3] = 'water' 
