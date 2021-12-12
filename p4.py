with open('scp.txt') as f:
    data = f.read()
    print("Old data:\n",data)
    new_data=""
    for char in data:
        if char.isalnum():
            new_data+=char
    print("after removing data:\n",new_data)