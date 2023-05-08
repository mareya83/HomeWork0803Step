messege_fizz = 'Fizz'
messege_buzz = 'Buzz'

i = int(input("Enter a number  :"))

if i > 0 and i < 100:

    if i%3 == 0 and i%5 == 0:
        print(messege_fizz + messege_buzz)

    elif i%3 == 0:
        print(messege_fizz)

    elif i%5 == 0:
        print(messege_buzz)

    else:
        print(i)

else:
    print("Incorret number!!")