# Scopes and Namespaces
def mainfunction():

    def first():
        name="sha"
        return name
    def second():
        nonlocal name
        name="shalu"
    def third():
        global name
        name="shalinie"
    name="shalinie22"
    # print the name as shalinie22 
    print(name)
    first()
    # after calling the first function the name does'nt change as value "sha" is accesed only inside first function 
    # it prints shalinie22
    print(name)
    second()
    # in second function the name is non local hence the value changes to shalu
    # it prints shalu
    print(name)
    third()
    # after third function the value of name changed to shalinie but not inside the function mainfunction
    # it prints shalu
    print(name)
    
mainfunction()
#it prints shalinie
print(name) 


# final output
# shalinie22
# shalinie22
# shalu
# shalu
# shalinie
