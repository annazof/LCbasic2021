
def dot_product(vec1,vec2):
    new=0
    for i in range(len(vec1)):
        new+=vec1[i]*vec2[i]
    print(new)

dot_product([1, 1], [1, 1])
#== 2
dot_product([1, 2], [1, 4])
#== 9
dot_product([1, 2, 1], [1, 4, 3])
#== 12