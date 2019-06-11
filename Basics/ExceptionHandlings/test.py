try:
    import calc1
    calc1.add()
except Exception as e:
     print("No module found",e)
finally:
    print("close")
