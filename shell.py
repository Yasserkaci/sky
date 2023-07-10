import sky
while True: 
    text = input("sky >>> ")
    result, error = sky.run('<stdin>', text)

    if error:print(error.as_string())
    else: print(result)