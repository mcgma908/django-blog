#deslugify
def deslugify(slug):
    unslug = ""
    for x in slug:
        if x =="_" or x=="-":
            unslug = unslug + " "
        else:
            unslug = unslug + x
            me = unslug[0].upper() + unslug[1:]
    return me