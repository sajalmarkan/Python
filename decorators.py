def greet(fx):
    def mfx(*args,**kwargs):
        print("Good Morning")
        fx(*args,**kwargs)
        print("Thank you for usig this function")
    return mfx
    
@greet
def hello():
    print("Hello World")

@greet
def add(a,b):
    print(a+b)
hello()
add(1,2)