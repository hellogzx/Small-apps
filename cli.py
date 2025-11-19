def get_average():
    with open("files/data.txt",'r') as file:
        data = file.readlines()
        values = data[1:]
        values = [float(i) for i in values]
        average = sum(values)/len(values)
        print("this is update")
    return average



average = get_average()
print(average)
