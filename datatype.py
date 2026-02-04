age = 29 #integer
length = 45.6 #float
greeting = "Hello There." #string
hasFeathers = True #Boolean

#data structures - Multiple values stored in one variable

fruits = ["Banana","Mango","Pineapple"] #list - Ordered and changeable "can carry any type of data type"

courses = ["MIT","Data Science","Cybersecurity"] #array - carries only data types of similar kind

cars = ("Mercedes","Ford","Nissan","Mustang") #tuple - Ordered and unchangeable

countries = {"Kenya","Argentina","Peru","China","Wales"} #set - Unordered and unchangeable

student = {
    "firstname" : "Esther",
    "course" : "MIT",
    "age" : 19,
    "nationality" : "Kenya",
    "gender" : "Female"
}  #dictionary - Key value pair

print(age)
print("The length is",length)
print(fruits)
print(countries)
print(student["gender"])

#typecasting - converting one data type to another

print(float(age))
print(int(length))