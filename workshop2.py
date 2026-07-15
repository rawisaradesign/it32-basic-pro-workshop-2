name = input("ชื่อ")
age = int(input("อายุ (ปี)"))
height = int(input('ส่วนสูง (cm)'))
power = int(input("พละกำลัง (1-10)"))
money = int(input("เงินติดตัว (starter pack dollar)"))
if age >= 15 and age <= 18 :
    if height >= 160 and height <= 170 :
        if power >= 4 and power <= 5 :
            if money >= 5000 and money <= 10000 :
                print("ผ่าน")
                print("ตำแหน่ง tiny")
if age >= 18 and age <= 25 :
    if height >= 170 and height <= 190 :
        if power >= 6 and power <= 7 :
            if money >= 10000 and money <= 50000 :
                print("ผ่าน")
                print("ตำแหน่ง giant")
if age > 25 :
    if height > 190 :
        if power > 8 :
            if money > 100000 :
                print("ผ่าน")
                print("ตำแหน่ง boss")
                
                

