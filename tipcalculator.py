total = float(input("Enter total amount:"))
tip = float(input("enter tip percentage amount"))
tipPer = tip /100
tipAmount = round(total * tipPer, 2)
print(tipAmount)
