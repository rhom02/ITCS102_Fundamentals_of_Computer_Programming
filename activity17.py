#List

# fruits1 = "Lipute" #10kb #1kb
# fruits2 = "Longgan"
# fruits3 = "Duhat"
# fruits4 = "Atis"
# fruits = "Pinya"
# fruits = "Kaimito"

fruits = [] #empty list
#fruits = list() #empty list
#inserting value to a list
fruits = ["Lipute", "Longgan", "Duhat", "Atis"]
print(fruits)
#list functions
fruits.append("Pinya")
fruits.append("Kaimito")
fruits.append("Pakwan")
fruits.append("Mangga")
fruits.append("Rambutan")
fruits.append("Passion Fruit")
print(fruits)
print(fruits[3])
print(fruits[0])
print(fruits[-1])
fruits.insert(1, "Lansones")
print(fruits)

#list slicing
print(fruits[0:4])
print(fruits[-5: ])
print(fruits[:-2])