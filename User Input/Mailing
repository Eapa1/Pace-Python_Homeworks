class Person:
    def __init__(self, name,address,phone):
        self.names=name
        self.addresses=address
        self.phones = phone
    def set_names(self, name):
        self.__names = name

    def set_addresses(self, address):
        self.__addresses = address

    def set_phones(self, phone):
        self.__phones = phone
   
    def get_names(self):
        return self.__names

    def get_addresses(self):
        return self.__addresses
    
    def get_phones(self):
        return self.__phones
#____________________________________________________________________
class customer(Person):
    def __init__(self, name, address, phone, mail, number):
        Person.__init__(self, name,address,phone)
        self.mailing = True if mail == 'Y' else False
        self.__mail = mail
        self.__number = number

    def set_mail(self, mail):
        self.__mail = mail

    def set_number(self, number):
        self.__number = number

    def get_mail(self):
        return self.__mail

    def get_number(self):
        return self.__number
    def mailList(self): 
        mailing = input("Do you wish to be on the Mailing List? Yes or No?")
        if mailing == "Yes": 
            return "On the mailing list"

#____________________________________________________________________
#import Person
def main():
    Person1 = customer("Name:Bob Crays","Address:344 Water street NY, NY 10067","Number:347-987-7865","Phone_Number:347-654-4532 ", "number:345-786-3456")
    print(Person1.names)
    print(Person1.addresses)
    print(Person1.phones)
    print("Person 1 information", "\n")

    Person1.set_names("Eapa Choudhury")
    Person1.set_addresses("913 Burke Ave Bronx NY 10469")
    Person1.set_phones("347-615-5870")

    Person2 =customer("Name:Eapa Chowww","Address:100 Houston street NY, NY 10984","Phone_Number:646-534-6584 ","Number:345-678-9086","mailing")
    print(Person2.names)
    print(Person2.addresses)
    print(Person2.phones)
    print("Person 2 information", "\n")

    print ("Name:", Person1.get_names())
    print ("Address:", Person1.get_addresses())
    print ("Phone number:", Person1.get_phones())
    print("Thank you for sharing your Information!!", "\n")
    

   
    Person2.set_names("Selina Gomes")
    Person2.set_addresses("100 Crosby Street, NY NY 10012")
    Person2.set_phones("646-255-0265")
    

  
    print ("Name:",Person2.get_names())
    print ("Address:", Person2.get_addresses())
    print ("Phone number:", Person2.get_phones())
    print("Thank you for sharing your Information!!", "\n")
   

    
    Person1.set_names("Sam Smith")
    Person1.set_addresses("1 Pace Plaza NY NY 10023")
    Person1.set_phones("718-799-3789")

  
    print ("Name:",Person1.get_names())
    print ("Address:", Person1.get_addresses())
    print ("Phone number:", Person1.get_phones())
    print("TThank you for sharing your Information!!","\n")
    print("\n")
def MailList():
    mail = input("Do you wish to be on the Mailing List? Yes or No?")
    if mail == "Yes":
        print("Added to Mailing List successfully!")
    if mail == "No":
        print("I don't want to be added to the Mailing List")
    return MailList

MailList()
main()

