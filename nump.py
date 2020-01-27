import numpy as np
import numpy.matlib


"""a=np.array([[1,2,3],[4,5,6]])
print(a)
a=np.array([[1567,254354,32424,234234],[445756,23523453455,623345,726545]],complex)
print(a)"""
a=np.array([[101,22,34,467],[587,456,576,8454],[9545,1543,9349,6587]])
print(a.ndim)
print(a)
print('Each item contains',a.itemsize,'bytes')
print('Data type: ',a.dtype)
print('Array size',a.size)
print('Shape',a.shape)
print('Original Array',a)
a=a.reshape(4,3)
print('Printing the reshaped array...')
print(a)
a=np.linspace(3,9,99)
print(a)
a=np.array([[101,22,34,467],[587,456,576,8454],[9545,1543,9349,6587]])
b=np.array([[7,8,9,5],[3,2,4,1],[9,8,7,6]])
print('Original Array',a)
print('Max element', a.max())
print('Min element', a.min())
print('Sum of element', a.sum())
print('Max element in column', a.max(axis=0))
print('Min element in row', a.min(axis=1))
print('Sum of element of row', a.sum(axis=1))
print(np.sqrt(a))
print(np.std(a))
print('Sum of array a and b\n',a+b)
print('Multiplication of a and b\n',a*b)
print('Division of a with b\n',a/b)
print('vertically concatenated: ',np.vstack((a, b)))
print('Horizontally concatenated',np.hstack((a, b)))
arr=np.empty((7,9),dtype=int,order='C')
print(arr)
arr=np.asarray(a)
print(type(a))
print(arr)
l= b'hello python world'
print(type(l))
a=np.frombuffer(l,dtype='S1')
print(a)
print(type(a))
arr=np.arange(11,99,3,float)
print('The array between 11 to 99: ',arr)
brr=np.linspace(11,21,6,endpoint=True)
print(brr)
brr=np.logspace(11,21,6,endpoint=True)
print(brr)
for x in np.nditer(b):
    print(x,end='')
for x in np.nditer(b,op_flags=['readwrite']):
    x[...]=3*x
    print(x,end='')

c=10
d=99
print('binary representation of c: ',bin(c))
print('bitwise-and of a and b: ',np.bitwise_and(c,d))

sub=np.char.encode('this is just basics of numpy, so no need to be highly critical','cp500')
print(sub)

crr=np.array([99,34,54,76,12,76,89,566])
print('sin value of angles', np.sin(crr*np.pi/180))
print('cos value of angles', np.cos(crr*np.pi/180))
print('tan value of angles', np.tan(crr*np.pi/180))
sinvalue=np.sin(crr*np.pi/180)
cosvalue=np.cos(crr*np.pi/180)
tanvalue=np.tan(crr*np.pi/180)
print(np.arcsin(sinvalue))
print(np.arccos(cosvalue))
print(np.arctan(tanvalue))
drr=([66.6767,99.76, 45.676,53.698])
print('floor value',np.floor(drr))
print('cieling value',np.ceil(drr))
print('minimum in array',np.amin(crr))
print('maximum in array',np.amax(crr))
print('peak to peak along axis',np.ptp(b,0))
print('percentile value',np.percentile(b,9,0),(b,7,1))
print('median along axis 0',np.median(b,0))
print('mean along axis 0',np.mean(b,0))
print('mod along axis 1',np.mod(b,1))
print('average along axis 1',np.average(b,1))
print('sorting',np.sort(b))
print('sorting along axis 0', np.sort(b,0))
print('sorting along columns 1', np.sort(b,1))
print(numpy.matlib.eye(n=3, M=3, k=0, dtype=int))
print(numpy.matlib.identity(5, dtype=int))
print(numpy.matlib.rand(9,9))
aa=np.array([[100,200],[22,33]])
bb=np.array([[230,324],[656,876]])
dot=np.dot(aa,bb)
vdot=np.vdot(aa,bb)
inner=np.inner(aa,bb)
mat=np.matmul(aa,bb)
print('dot values of two arrays',dot)
print('dot values two vectors',vdot)
print('inner elements value',inner)
print('multiplication of two matrices',mat)
print('determinant of aa array',np.linalg.det(aa))
print('determinant of bb array',np.linalg.det(bb))
print('linear algebra solve',np.linalg.solve(aa,bb))
print('original bb arrray: \n',bb)
bb=np.linalg.inv(aa)
print('inverse to aa: \n',bb)
degreevalue=np.degrees(aa)
print('degree values; ',degreevalue)
