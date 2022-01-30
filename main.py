print("Welcome to the tip calculator.")
total=input("What was the total bill? ")
person=input("How many people to split the bill? ")
tip=input("What percentage tip would you like to leave? 10, 12, or 15? ")
payment=(int(total)/int(person))
tipPayed=(int(tip)/100)*int(payment)
payment1=int(payment) + int(tipPayed)
print("Each person should pay ")
print(payment1)


