quantity = int(input("จำนวนปืนที่รับมาขาย :"))
cost_price = int(input("ต้นทุนของปืนที่รับมา :"))
sell_price = int(input("ราคาที่จะนำไปขายต่อ :"))
team_member = int(input("จำนวนลูกน้องในทีมที่ไปทำงาน :"))
print(cost_price * quantity)#ต้นทุน
print(sell_price * quantity)#รายรับ
print((sell_price * quantity) - (cost_price * quantity))#กำไร
print((sell_price * quantity) - (cost_price * quantity)  *0.2)
print((sell_price * quantity) - (cost_price * quantity) / team_member)
