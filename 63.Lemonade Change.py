def lemonadeChange(bills):
    five = ten = 0
    for b in bills:
        if b == 5: five += 1
        elif b == 10: five, ten = five-1, ten+1
        else: five, ten = (five-3, ten) if ten == 0 else (five-1, ten-1)
        if five < 0: return False
    return True
print(lemonadeChange([5,5,5,10,20]))   # True
print(lemonadeChange([5,5,10,10,20]))  # False

                #(OR)

def lemonadeChange(bills):
    five = ten = 0

    for bill in bills:
        if bill == 5:
            five += 1
        elif bill == 10:
            if five == 0:
                return False
            five -= 1
            ten += 1
        else:  # bill == 20
            if ten > 0 and five > 0:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False

    return True

# Examples
print(lemonadeChange([5,5,5,10,20]))   # True
print(lemonadeChange([5,5,10,10,20]))  # False
