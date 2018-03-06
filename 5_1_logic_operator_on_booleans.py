a= True
b= True
print("a is {0}".format(a))
print("b is {0}".format(b))
print("~a is {0}".format(not a))
print("~b is {0}".format(not b))
print("a & b is {0}".format((a and b) or a) # (True if both of them are True) true if one of them true
print("a or b is {0}".format((a or b) and b) # (True if one or both of them are True) true if both of them is true


#################################################
## A     ### B     ### A and B ### A or B #######
## True  ### True  ### True    ### True   #######
## True  ### False ### False   ### True   #######
## False ### True  ### False   ### True   #######
## False ### False ### False   ### False  #######
#################################################
