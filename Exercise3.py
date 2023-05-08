
operators = [
    {"operator": "vodafon", "price": int(input("Enter price for Vodafone :   "))},
    {"operator": "kievstar", "price": int(input("Enter price for Kievstar :   "))},
    {"operator": "lifecell", "price": int(input("Enter price for Lifecell :   "))}           
    ]

print("Please,  choose two operators")

for i in operators:
    print (str(operators.index(i)) + ") " + i["operator"])

first_operator = int(input("Enter first operator:   "))
second_operatop = int(input("Enter second operator:   "))

if first_operator >=0 and first_operator < len(operators):
    if second_operatop >=0 and second_operatop < len(operators):
        total_sum = operators[first_operator]["price"] + operators[second_operatop]["price"] 
        print("Total price:   " + str(total_sum))
    else:
        print("Incorrect second operator.")
else:
    print("Incorrect first operator.")
