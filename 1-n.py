#1 den n e kadar olan tek sayıların toplamını ve çarpımını; çift sayıların ise karelerinin toplamını bulma

n = int(input("n: "))

i = 0
total = 0
multiplying = 0
sumofSquares = 0

while (i < n):
    i += 1
    if (i % 2 == 1):
        total = total + i
        print("Odd Number")
        print("Total = " + str(total)) 
        print("and")
        multiplying = multiplying * i
        print("Multiplying = " + str(multiplying))
    elif (i % 2 == 0):
        sumofSquares = sumofSquares**2 + i**2
        print("Even Number")
        print("Sum of Squares = " + str(sumofSquares))   
        print("**************")         