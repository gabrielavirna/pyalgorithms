#eval - evaluates any expression(not a definition: x = 5!) you pass in the form of a string, an returns the value
#can evaluate : 5<10 -> returns value: True
list_str = "[6,6,2,1,2]"        #list as a string

list_str = eval(list_str)

print(list_str)
print(list_str[2])

x = input("code:")
check_this_out = eval(input("code"))
print(check_this_out)