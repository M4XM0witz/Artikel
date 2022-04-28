#skapa ett program för att beräknna summan och medel för summan du matar in, antal tal ska läsas in från användaren
avg = int(input("ange hur många tal som du ska beräkna summa och medel för:  "))
def calcAvg ():
    sum = 0 
    counter = avg 
    while counter > 0:
        num = float(input("mata in ett tal:  "))
        sum = sum + num

        counter = counter -1
    print(f"summan är: {sum} medel är {sum / avg}")

calcAvg()

