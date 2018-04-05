file = open("city.txt","w+")
n = int(input("Enter the total number of cities"))
for i in range(n):
    city = input("Enter city name : ") 
    population = input("Enter population : ") 
    area = input("Enter the area : ") 
    file_input = city+","+population+","+area
    file.write(file_input)
    file.write(" ")
file.close()

file = open("city.txt","r+")
file_data = file.read()
print(file_data)
file.close()
file_data_list = file_data.split()
file_data_list.sort()

file = open("city.txt","w+")
for i in range(len(file_data_list)):
    file.write(str(file_data_list[i]))
    file.write(" ")
file.close()

file = open("city.txt","r+")
print(file.read())
