#import from same directory -> import class_name
import Part5_Class
#if different folder -> from folder_name import class_name
# from OOP import book
b1 = Part5_Class.Book("Opekkha", "Humayun ahmed") #mention the class
b1.details()
b1.set_price(255)
print(b1.get_price())
x = b1.get_price()
print(x)

