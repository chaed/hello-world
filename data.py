import os
import sys


def print_this(n):
    # in window
    # os.system('cls')
    os.system('clear')
    print("  +-Xn-+-Yn-+--n-+-An-+-Bn-+")
    print("r +----+----+----+----+----+")
    for i in range(n):

        print("%2d| %3d| %3d| %3d| %3d| %3d|" %(i+1,x[i],y[i],m[i],a[i],b[i]))
        print("  +----+----+----+----+----+")

def calculate_EP():
    print("Enter EF number (Ex. 2-7): ")
    first = input("First number: ")

    if first in m:
        index = m.index(first)
        second = input("Second number: ")
        EP_number = x[index] + second -1
        if EP_number >= x[index] and EP_number <= y[index]:

            print("EP1(%d)" %(EP_number))
        else:
            print("There is no this EP1")
    else:
        print("There is no EF%d" %(first))

def calculate_EF(n):
    flag = False
    print("Enter EP1 number (Ex. 151)")
    EP1 = input("EP1 ")
    for i in range(n):
        if (EP1 - x[i]) >= 0 and (EP1 <= y[i]):
            second = EP1 - x[i] +1
            first = m[i]
            flag = True

    if flag:
        print("EF%d-%d" %(first, second))
    else:
        print("Wrong number")

def exit():

    print("Program end")
    sys.exit()

if __name__ == "__main__":

    x = []
    y = []
    m = []
    a = []
    b = []

    #switcher = {1:calculate_EF(),
                #2:calculate_EP(),
                #3:exit()}

    n = input("Enter n (How many sets?): ")

    for i in range(n):
        x.append(0)
        y.append(0)
        m.append(0)
        a.append(0)
        b.append(0)

    print_this(n)

    for i in range(n):

        print("Enter row_%d X value: " %(i+1))
        x[i] = input()
        print_this(n)
        print("Enter row_%d Y value: " %(i+1))
        y[i] = input()
        print_this(n)
        print("Enter row_%d n value: " %(i+1))
        m[i] = input()
        print_this(n)
        print("Enter row_%d A value: " %(i+1))
        a[i] = input()
        print_this(n)
        print("Enter row_%d B value: " %(i+1))
        b[i] = input()
        print_this(n)


    while(True):
        print("Input EF: 1; Input EP: 2; Exit program: 3")
        option = input("Enter option 1 or 2 or 3: ")
        #switcher.get(option)
        if option == 1:
            print_this(n)
            calculate_EP()
        elif option == 2:
            print_this(n)
            calculate_EF(n)
        else:
            exit()
