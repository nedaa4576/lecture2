####################################
# following variables are the same #
####################################
 str1=" hi "
# str2='salam'

######################
## concat two string #
######################
 name='neda'
 family = "sadegian"
 greeting= str1+name+family
 print(greeting)
#
 greeting2=str1+" "+name+" "+family
 print(greeting2)
#
 print(("\'"+greeting2+" \'") * 3)
######################################
## some useful operations on strings #
######################################
 print(greeting2.capitalize())
 print(greeting2.upper())
 print(greeting2.rsplit(' ')) # splitting the string by blank
 print(greeting2.strip(' ')) # remove the blanks before and after the string

###########################################
### another sample of printing a varibale #
###########################################
pa = 1743.783
print(pa)
str_pi = str(pa)
print("pa number is : ", pa)  # print each part of input separately
print("pa number is : " + str(pa))  # concat two string
