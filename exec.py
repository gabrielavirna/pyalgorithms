exec("print('so this works like eval')")

list_str = "[5,6,2,1,6]"
list_str = exec(list_str)           #this compiles and evaluates
print(list_str)

exec("list_str2 = [5,6,2,1,1]")
print(list_str2)

exec("def test(): print('o sniip snapp!!')")
test()

exec("""
def test2():
    print('multi-line works also...')
""")
test2()