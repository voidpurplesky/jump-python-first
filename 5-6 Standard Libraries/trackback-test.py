from traceback import format_exc

def a():
    return 1/0

def b():
    a()

def main():
    try:
        b()
    except:
        print(format_exc())

main()