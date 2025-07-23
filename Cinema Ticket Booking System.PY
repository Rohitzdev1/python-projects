name=input("enter your name")
age=int(input("enter your age"))
options=int(input("choose your movie from 1,2,3 \n 1.Avengers \n 2.Jawaan \n 3.Jani dhushman \n "))
quantity=int(input(" enter tickets quantity in numbers "))
if options==1:
    movie="Avengers"
    price=300
elif options==2:
    movie="Jawaan"
    price=250
elif options==3:
    movie="Jani Dushman"
    price=150
else:
    print("invalid option choose from list")
base_price=price*quantity
if age<18:
    discount=20
elif age>60:
    discount=30
else:
    discount=0
discount_amount=(base_price*discount)/100
final_price_with_discount=base_price-discount_amount
popcorn=str(input("do you want popcorn YES/NO "))
if popcorn=="YES":
    final_price=final_price_with_discount+(150*quantity)
    popcorn_price=150*quantity
elif popcorn=="NO":
    final_price=final_price_with_discount+0
    popcorn_price=0

print("Username :",name)
print("Movie Name :",movie)
print("Tickets Count :",quantity)
print("Total Before Discount :",base_price)
print("Discount Amount :",discount_amount)
print("Popcorn Charge :",popcorn_price)
print("Final Total :",final_price)
