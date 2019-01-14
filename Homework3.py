#the amount of county sales tax
def AmountOfCountySalesTax(price):
    county_sales_tax =  0.025
    return price * county_sales_tax
def main():
    price = float(input('Enter the price of the purchase: '))
    TotalSalesTax(price)
#the amount of state sales tax
def AmountOfStateSalesTax(price):
    state_sales_tax = 0.05
    return price * state_sales_tax
#the total sales tax  
def TotalSalesTax (price):
    print('Original price', price)
    state_tax = AmountOfStateSalesTax(price)
    print('State tax', state_tax)
    county_tax = AmountOfCountySalesTax(price)
    print('County tax', county_tax)
    print('Total sales tax' ,state_tax + county_tax)
    print('Total price of the purchase including sales tax is', price + \
          state_tax + county_tax)
    print ("Thank you for calculating!!!!")

# Call the main function
main()
