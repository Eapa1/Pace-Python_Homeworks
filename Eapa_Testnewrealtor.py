                #Eapa Choudhury
                #Python Final Exam 12/21/2018

class Realtor():
#the __init__ method takes arguments
    def __init__(self,pptyId,zip,sqft,bed,bath):
        self.pptyId=pptyId
        self.zip=zip
        self.sqft=sqft
        self.bed= bed
        self.bath=bath
#Write getters and setters for all
    def set_pptyId(self,pptyId):
        self.pptyId=pptyId
    def set_zip(self,zip):
        self.zip=zip
    def set_sqft(self,sqft):
        self.sqft=sqft
    def set_bed(self,bed):
        self.bed=bed
    def set_bath(self,bath):
        self.bath=bath

    def get_pptyId(self):
        return self.pptyId
    def get_zip(self):
        return self.zip
    def get_sqft(self):
        return self.sqft
    def get_bed(self):
        return self.bed
    def get_bath(self):
        return self.bath

    def isAvailable(self):
        return False
    
    def pptyTax(self):
        if self.zip==11322:
            return (self.sqft*0.0305)+(self.bed*150)+(self.bath*100)
        elif self.zip==11333:
            return (self.sqft * 0.0315) +( self.bed * 150) + (self.bath * 100)
        else:
            return 0
#________________________________________________________      
class Newrealtor(Realtor):

    def __init__(self,pptyId,zip,sqft,bed,bath,price):
        Realtor.__init__(self,pptyId,zip,sqft,bed,bath)
#two dictionaries - inventory1 and inventory2
        self.inventory1={'pptyId':[2110,2115],'price':[495000,489000]}
        self.inventory2={'pptyId':[3260,3266],'price':[624000,599000]}
        self.price=price
#Write getter and setter methods for Price
    def get_price(self):
        return self.price
    def set_price(self,price):
        self.price=price
#_______________________________________________________
#import Realtor
#class Testnewrealtor:
def main():
    Property_Des1=Newrealtor(2110,11322,3500,3,4,495000)
    print ('property id: ', Property_Des1.get_pptyId())
    print('zip: ',Property_Des1.get_zip())
    print('sqft: ',Property_Des1.get_sqft())
    print('bed: ',Property_Des1.get_bed())
    print('bath: ',Property_Des1.get_bath())
    print('price: ',Property_Des1.get_price())
    print('tax: $',Property_Des1.pptyTax())
    print("Property ID is 2110 and Zip code is 11322 therefore 3.05% tax added", "\n")

    Property_Des1.set_pptyId("6754")
    Property_Des1.set_zip("10465")
    Property_Des1.set_sqft("786")
    Property_Des1.set_bed("3")
    Property_Des1.set_bath("1")
    Property_Des1.set_price("456000")
   
    
    Property_Des2=Newrealtor  (3266,11333,455,5,3,599000)
    print ('property id: ', Property_Des2.get_pptyId())
    print('zip: ',Property_Des2.get_zip())
    print('sqft: ',Property_Des2.get_sqft())
    print('bed: ',Property_Des2.get_bed())
    print('bath: ',Property_Des2.get_bath())
    print('price: ',Property_Des2.get_price())
    print('tax: $',Property_Des2.pptyTax())
    print("Property ID is 3266 and Zip code is 11333 therefore 3.15% tax added","\n")

    Property_Des3=Newrealtor  (8270,11373,200,1,3,789000)
    print ('property id: ', Property_Des3.get_pptyId())
    print('zip: ',Property_Des3.get_zip())
    print('sqft: ',Property_Des3.get_sqft())
    print('bed: ',Property_Des3.get_bed())
    print('bath: ',Property_Des3.get_bath())
    print('price: ',Property_Des3.get_price())
    print('tax: $',Property_Des3.pptyTax())
    print("Property ID is not in the database therefore no tax added","\n")
    

main()
