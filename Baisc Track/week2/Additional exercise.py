#Your program may ask the user for additional information, or
#you can assume values for these, e.g.;
#– Speeds for walking/biking/driving,
#– Time to get going (take bicycle out of the shed, scratch ice
#from the window),
#– Time to find parking (and, when some distance away, time
#to get to the actual destination)


dist=int(input("What is the distance in km?"))

walk=int(input("What is your average speed walking in km/h?"))

bik=int(input("What is your average speed biking in km/h?"))

dri=int(input("What is your average speed driving in km/h?"))

twalk=float(dist/walk)
tbik=float(dist/bik)
tdri=float(dist/dri)

print("Time to walk there",twalk,
      "Time to bike there",tbik,
      "Time to drive there",tdri,
      "Values in hours")






