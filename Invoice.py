lop=list()
tot=0
print(lop)
nop=int(input("Enter No Of Product to buy  : "))
for i in range(nop):
    pp=int(input("Enter Price of Product : "))
    lop.append(pp)
    tot=tot+pp
gst=tot*18/100
amount=tot+gst
print("Your Total Bill is : ",amount)
