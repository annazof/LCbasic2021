layout = "{0:>4}{1:>4}{2:>4}{3:>3}{4:>4}{5:>4}{6:>4}{7:>4}{8:>4}{9:>4}{10:>4}{11:>6}{12:>6}{13:>6}"
print (layout.format("\t","\t",1,2,3,4,5,6,7,8,9,10,11,12))
print ("\t","  :--------------------------------------------------")
c = 0
for i in range(1, 13):
    c+=1
    print(layout.format(c,":", 1*c, 2*c, 3*c,  4*c, 5*c,  6*c,7*c, 8*c,  9*c, 10*c,  11*c, 12*c))