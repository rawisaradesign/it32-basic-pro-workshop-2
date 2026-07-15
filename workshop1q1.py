quantity = int(input("จำนวนปืนที่รับมาขาย :"))
cost_price = int(input("ต้นทุนของปืนที่รับมา :"))
sell_price = int(input("ราคาที่จะนำไปขายต่อ :"))
team_member = int(input("จำนวนลูกน้องในทีมที่ไปทำงาน :"))
total_cost = cost_price * quantity
total_rub = quantity * sell_price
profit = total_rub - total_cost
money_boss = profit * 0.2
team_share = ( profit - money_boss ) / team_member
print("ต้นทุนทั้้งหมด" , total_cost ,"บาท")
print(f"รายรับทั้งหมด {total_rub} บาท")
print(f"กำไรสุทธิ {profit} บาท")
print(f"จำนวนเงินที่หักไปให้บอส {money_boss} บาท")
print(f"จำนวนเงินที่บอสแต่ละคนได้ {team_share} บาท")