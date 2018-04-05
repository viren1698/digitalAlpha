import copy
import numpy
a = ([['Rhia',10,20,30,40,50], ['Alan',75,80,75,85,100], ['Smith',80,80,80,90,95]])
b = copy.deepcopy(list(a))
matrix_value = numpy.array(a)
print(matrix_value[:,:2])
matrix_value[2,:] = ['Sam',82,79,88,97,99]
print(matrix_value)
matrix_value[0][3] = 95
print(matrix_value)
matrix_value = numpy.append(matrix_value,[[73],[80],[85]],axis=1)
print(matrix_value)
