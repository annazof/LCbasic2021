

def add_vectors(m,n):
    a=[]
    for i in range(len(m)):
        new= m[i]+n[i]
        a.append(new)
    print(a)




add_vectors([1, 1], [1, 1])
#== [2, 2]
add_vectors([1, 2], [1, 4])
#== [2, 6]
add_vectors([1, 2, 1], [1, 4, 3])
#== [2, 6, 4]
