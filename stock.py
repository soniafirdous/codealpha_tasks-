stock_rate={"Aldoachemicals":150,
            "UBL Bank":200,
            "Engro chemicals":300,
            "Fauji fertilizer company":500}


user_stock={}
while True:
    stock=input("enter stock name :")
    if stock=="done":
        break
    if stock in stock_rate:
        try :
            quantity=int(input("enter quantity :"))
            user_stock[stock]=quantity
            print(f"you have {quantity} quantity of {stock}")
        except ValueError:
            print("enter a valid number")
    else:
        print("stock not available")
        
print("user stock summary:")   
     
total_investment_value=0    
for stock,quantity in user_stock.items():   
    rate=stock_rate[stock]
    price=quantity*rate
    print(f"{stock}: {quantity} x Rs.{rate} = Rs.{price}")
    print(f"the price of {stock} is {price}")
    total_investment_value+=price
print(f"Total investment = {total_investment_value}")
    
print("Saving to txt file")


with open("User stock summary.txt","w")as f:
    for stock,quantity in user_stock.items():
        rate=stock_rate[stock]
        price=quantity*rate
        f.write(f"{stock}: {quantity} x Rs.{rate} = Rs.{price}")
        f.write(f"the price of {stock} is {price}\n")
        f.write(f"Total investment = Rs.{total_investment_value}")
        
        