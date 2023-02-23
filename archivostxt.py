f = open('alumnos2.txt', 'w')
#f.write('Hola mundo')


f.write('Nuevo hola')
f.write('\n'+ 'Nuevo hola')
'''alumnos = f.read()
print(alumnos)
f.seek(20)
alumnos2 = f.read()
print(alumnos2)'''

#alumnos = f.readlines()
# alumnos = f.readline()
# print(alumnos)
## print(alumnos[0]) 
# for item in alumnos:
# print(item, end ='')
f.close()