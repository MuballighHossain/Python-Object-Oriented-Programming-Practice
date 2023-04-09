class Book:

    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.price = 0

    def set_price(self, price): #set price
        self.price = price

    def get_price(self):    #get price
        return self.price   #returning

    def details(self):  #return details
        print("Book Name:", self.name,
              "\nAuthor:", self.author,
              "\nPrice:", self.price)



