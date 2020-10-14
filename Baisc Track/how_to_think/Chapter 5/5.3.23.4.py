this = ["I", "am", "not", "a", "crook"]
that = ["I", "am", "not", "a", "crook"]
print("Test 1: {0}".format(this is that))
#FALSE they do not refer to the same object
that = this
print("Test 2: {0}".format(this is that))
#TRUE they refer to the same object