import random
n = random.randint(1, 38)

# part 1
print ("The spin resulted in {0}...".format(n))
if n < 37:
    print("Pay ", n)
elif n == 37:
    print("Pay ", 0)
else:
    print("Pay ", '00')

#part 2
red_space = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21,
23, 25, 27, 30, 32, 34, 36]

green_space = [37, 38]

if n in red_space:
    print("Pay Red")
elif n in green_space:
    pass
else:
    print("Pay Black")

#part3
if n%2 == 0 and n != 38:
    print('Pay Even')
elif n%2 != 0 and n != 37:
    print('Pay Odd')

#part4
if n < 19:
    print("Pay 1 to 18")
elif n < 37:
    print("Pay 19 to 36")