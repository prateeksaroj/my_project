with open('scp.txt') as f:
    data = f.read()
    print("Old data:\n",data)
    newdata=""
    for char in data:
        if char.isalnum():
            newdata+=char
    print("after removing data:\n",newdata)