 
#calc1.py module is added in my library,
#ImportError
try:
    import calc1
    a=10
    b=2
    print("Open")
    print(calc1.div(a,b))
   
except ModuleNotFoundError as e2:
    print("Module is not found",e2)

finally:  
    print("Close") 


