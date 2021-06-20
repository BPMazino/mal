def READ(param):
    return param

def EVAL(param):
    return param

def PRINT(param):
    return param

def rep(param):
    return PRINT(EVAL(READ(param)))

while True:
    try:
        line = input("user> ")
        print(rep(line))
    except EOFError:
        break