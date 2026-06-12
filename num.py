import numpy as np
# print(np.__version__)
# mylist=[1,2,3,4]
# mylist=mylist*2
# print(mylist)
array=np.array([[1,2,3,4],[1,3,5,6]])
array=array*2
print(type(array))
arraydim=np.array([[[1,2,3],[4,2,7],[7,1,4]],
                       [[3,5,6],[2,8,9],[7,4,7]],
                       [[4,7,8],[9,7,5],[3,9,5]]])
print(arraydim.shape)

print(arraydim[0][0][0]) #chain indexing

print(arraydim[0,0,0]) #multi dimensional indexing 

strarr=np.array([[['a','b','c'],['n','z','f'],['g','k','e']],
                 [['e','r','t'],['w','y','q'],['a','c','o']],
                 [['a','f','t'],['r','g','y'],['r','u','i']]])
word=(strarr[0,2,1]+strarr[0,0,2]+strarr[2,1,2])
print(word)
#array[start:end:step]
