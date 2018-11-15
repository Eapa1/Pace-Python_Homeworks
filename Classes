##Name the file for class as: information.py
#Write a class named Information, which holds the following data attributes
class Information:
    def __init__(self, name,address,age,number):
        self.names=name
        self.addresses=address
        self.ages = age
        self.numbers = number
#accessor (get) and mutator (set) methods
    def set_names(self, name):
        self.__names = name

    def set_addresses(self, address):
        self.__addresses = address

    def set_ages(self, age):
        self.__ages = age

    def set_numbers(self, number):
        self.__numbers = number

        
    def get_names(self):
        return self.__names

    def get_addresses(self):
        return self.__addresses

    def get_ages(self):
        return self.__ages

    def get_numbers(self):
        return self.__numbers
#____________________________________________________________________
#and the program with objects of information as testinformation.py
#New class inheriting Class Information    
class testinformation(Information):
   def __init__(self):
        Information.__init__(self, name,address,age,number)
def main():
#The instances (objects) could be person1 and person2. Display the information.
    Person1 = Information("Name:Tom Fritz","Address:344 Water street NY, NY 10067","Age:40","Phone_Number:347-654-4532 ")
    print(Person1.names)
    print(Person1.addresses)
    print(Person1.ages)
    print(Person1.numbers)
    print("Person 1 information", "\n")

    Person2 =Information("Name:Eapa Chowww","Address:100 Houston street NY, NY 10984","Age:25","Phone_Number:646-534-6584 ")
    print(Person2.names)
    print(Person2.addresses)
    print(Person2.ages)
    print(Person2.numbers)
    print("Person 2 information", "\n")
# display the information
    Person1.set_names("Eapa Choudhury")
    Person1.set_addresses("913 Burke Ave Bronx NY 10469")
    Person1.set_ages("24")
    Person1.set_numbers("347-615-5870")

   
    print ("Name:", Person1.get_names())
    print ("Address:", Person1.get_addresses())
    print ("Age:", Person1.get_ages())
    print ("Phone number:", Person1.get_numbers())
    print("Thank you for sharing your Information!!", "\n")
    

   
    Person2.set_names("Patricia Gomes")
    Person2.set_addresses("100 Crosby Street, NY NY 10012")
    Person2.set_ages("28")
    Person2.set_numbers("646-255-0265")
    

  
    print ("Name:",Person2.get_names())
    print ("Address:", Person2.get_addresses())
    print ("Age:", Person2.get_ages())
    print ("Phone number:", Person2.get_numbers())
    print("Thank you for sharing your Information!!", "\n")
   

    
    Person1.set_names("John Smith")
    Person1.set_addresses("1 Pace Plaza NY NY 10023")
    Person1.set_ages("25")
    Person1.set_numbers("718-799-3789")

  
    print ("Name:",Person1.get_names())
    print ("Address:", Person1.get_addresses())
    print ("Age:", Person1.get_ages())
    print ("Phone number:", Person1.get_numbers())
    print("TThank you for sharing your Information!!","\n")
    print("\n")

main()

