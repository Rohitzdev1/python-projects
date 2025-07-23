name=input("enter your name:")
age=int(input("enter your age :"))
item=int(input("choose item (1,2,3) \n  1_t-shirt :500$ \n 2_shoes :1200$ \n 3_bagpack :800$ \n"))
quantity=int(input("enter the desired quantity :"))
if item==1:
    item_name="T-SHIRT"
    item_price=int(500)
elif item==2:
    item_name="SHOE'S"
    item_price=int(1200)
elif item==3:
    item_name="BAGPACK"
    item_price=int(800)

    total_price=quantity*item_price
if age<18:
        discount=10
elif age>=60:
        discount=15
else:
        discount=0

discount_amount=(total_price*discount)/100
delivery=str(input("do you want express delivery at for 100$ ,YES/NO \n"))
if delivery=="YES":
            delivery_charge=100
            final_price=total_price-discount_amount+100
else:
            delivery_charge=0
            final_price=total_price-discount_amount

print("customer :",name)
print("item purchased :",item_name)
print("quantity :",quantity)
print("original total :",total_price)
print("discount amount :",discount_amount)
print("delivery charge:",delivery_charge)
print("final amount to pay :",final_price)



