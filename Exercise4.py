
def manager_money(manager):
    manager_money = 0
    if manager < 500:
        manager_money = manager + manager/100*3
    elif manager >= 500 and manager <= 1000:
        manager_money = manager + manager/100*5
    else:
        manager_money = manager + manager/100*8
    return manager_money


first_manager = int(input("Enter sales amount first manager:  "))
first_manager = manager_money(first_manager)

second_manager = int(input("Enter sales amount second manager:  "))
second_manager = manager_money(second_manager)

third_manager = int(input("Enter sales amount third manager:  "))
third_manager = manager_money(third_manager)

if first_manager > second_manager and first_manager > third_manager:
    print("First manager the best : " + str(first_manager + 200))

if second_manager > first_manager and second_manager > third_manager:
    print("Second manager the best : " + str(second_manager + 200))

if third_manager > first_manager and third_manager > second_manager:
    print("Third manager the best : " + str(third_manager + 200))

