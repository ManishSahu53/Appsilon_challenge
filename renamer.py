"""
Category Codes - 
['Convertible'] = 0
['Hatchback'] = 1
['Sedan'] = 2
['StationWagon'] = 3
['SUV'] = 4
['VanPickup'] = 5

"""
import os

llist = ['Convertible', 'Hatchback', 'Sedan', 'StationWagon', 'SUV', 'VanPickup']
for j in range(len(llist)):
    path_data = 'Cars/' + llist[j]
    print('yeas')
    for root, dirs, files in os.walk(path_data):
        for file in files:
            if file.endswith('.png'):
                name = os.path.splitext(file)[0]
                os.rename(os.path.join(root, file), os.path.join(root, name + '.jpg'))
                print('Renamed %s' % (name))

            elif file.endswith('.jpeg'):
                name = os.path.splitext(file)[0]
                os.rename(os.path.join(root, file), os.path.join(root, name + '.jpg'))
                print('Renamed %s' % (name))
            else:
                continue
