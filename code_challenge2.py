#breakdown fix money value to PH denominations
# 1000, 500, 200, 100, 50, 20, 10, 5, 1

amount = 19877

money = eval(input("Enter Money to DEPOSIT ---->>> ")) # int(), eval(), type()
#print(type(money))
print("=============== PH BANK DENOMINATION ================")
print("MONEY TO DEPOSIT --------> ", money, "php")

libo = money // 1000 #19, 19.877
libo_sukli = money % 1000

five_h = libo_sukli // 500
five_sukli = libo_sukli % 500

two_h = five_sukli // 200
two_sukli = five_sukli % 200

one_h = two_sukli // 100
one_sukli = two_sukli % 100

fifty = one_sukli // 50
fifty_sukli = one_sukli % 50

twenty = fifty_sukli // 20
twenty_sukli = fifty_sukli % 20

ten = twenty_sukli // 10
ten_sukli = twenty_sukli % 10

five = ten_sukli // 5
five_sukli = ten_sukli % 5

piso = five_sukli // 1
piso_sukli = five_sukli % 1

print()
print("\n\t1000 - ", libo)
print("\n\t 500 - ", five_h)
print("\n\t 200 - ", two_h)
print("\n\t 100 - ", one_h)
print("\n\t 50 - ", fifty)
print("\n\t 20 - ", twenty)
print("\n\t 10 - ", ten)
print("\n\t 5 - ", five)
print("\n\t 1 - ", piso)






print("================= END OF BREAKDOWN ==================")