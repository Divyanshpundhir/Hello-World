while True:
    try:
        num = int(input("Enter the number: "))
       
    except:
        print("Sorry, that entry is invalid")
        continue
    else:
        [print('Hello World') for x in range(num)]
        break
