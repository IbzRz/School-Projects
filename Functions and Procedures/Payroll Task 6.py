#Ibrahim Sarker     Payroll Task 6
#4/3/24

def InpHrs():
    UHrs = int(input("Enter the hours you have worked: "))
    while UHrs < 0 or UHrs > 48:
        UHrs = int(input("""Incorrect Value
Enter the hours you have worked: """))
    return UHrs

def InpRate():
    URate = float(input("Enter the rate of pay your recieve: "))
    while URate < 4.62 or URate > 15.50:
        URate = float(input("""Incorrect Value
Enter the rate of pay your recieve: """))
    return URate

def CheckDTime(UHrs):
    if UHrs > 40:
        DTime = UHrs - 40
    else:
        DTime = UHrs
    return DTime

def TotPayCalc(UHrs, URate, DTime):
    if DTime >0:
        SubTotPay = URate*2
        TotPay = SubTotPay*DTime
    else:
        TotPay = UHrs*URate
    return TotPay

def displayOutput():
    UHrs = InpHrs()
    URate = InpRate()
    DTime = CheckDTime(UHrs)
    TotPay = TotPayCalc(UHrs, URate, DTime)
    print(f"Your pay is £{TotPay} for {DTime} hours of work.")
displayOutput()