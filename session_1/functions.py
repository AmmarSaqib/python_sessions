def toString(value="default"):

    try:
        value = str(value)
        return True, value
    except:
        return False, None


ret, value = toString()
if not ret:
    print("print some error")
else:
    print(value)
