class Person():
    def __init__(self, name, address, telephone):
        self.__name = name
        self.__address = address
        self.__telephone = telephone
        

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_telephone(self, telephone):
        self.__telephone = telephone


    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_telephone(self):
        return self.__telephone
#_________________________________________________________________________
#import Person

class Customer(Person):
    def __init__(self, name, address, telephone,  mail, number):  
        super().__init__(name, address, telephone) 
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
        add_me = input("Do you wish to be on the Mailing List? Yes or No?")
        if add_me == "Yes": 
            return "On the mailing list"
       

    def __str__(self):
        return "\nName: {}\nAddress: {}\nTelephone:  {}\nOn_MailingList: {}\nCustomer_Number: {}".\
                format(self.get_name(), self.get_address(),\
                       self.get_telephone(), self.mailList(),self.get_number())
#______________________________________________________________________________
#import Customer

def main():

    person1 = Customer('Eapa Choudhury', '913 Burke Ave, Bronx NY, NY 10469',\
                                 '347-615-5870','Y','10089')
    print(person1)
    person1 = Customer('Samantha sam', '100 Crosby street, Brooklyn NY, NY 10789',\
                                 '347-695-5897','Y','10879')
    print(person1)
main()
