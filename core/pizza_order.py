# This app is for calculating the price of Pizza.

# from tkinter import N, Y


# Sample Input:
#  Size = "L"
#  add_pepperoni = Y
#  extra_cheese = N
# ------------------------------
# Output:
# Your final bill is $28

def pizza():
    small_pizza = 15
    medium_pizza = 20
    large_pizza = 25

    small_pepperoni = 2
    m_l_pepperoni = 3

    cheese = 1

    name = input("Enter Customer Name")
    size = input(" Enter size of pizza")
    add_pepperoni = input("Enter add_ pepperoni or not")
    extra_cheese = input("Do you need extra cheese")

    if size == "L":
        if (add_pepperoni == "Y") and (extra_cheese == "Y"):
            bill = large_pizza + m_l_pepperoni + cheese
        elif (add_pepperoni == "N") and (extra_cheese == "Y"):
            bill = large_pizza + cheese
        elif (add_pepperoni == "Y") and (extra_cheese == "N"):
            bill = large_pizza + m_l_pepperoni
        else:
            bill = large_pizza
    elif size == "M":
        if (add_pepperoni == "Y") and (extra_cheese == "Y"):
            bill = medium_pizza + m_l_pepperoni + cheese
        elif (add_pepperoni == "N") and (extra_cheese == "Y"):
            bill = medium_pizza + cheese
        elif (add_pepperoni == "Y") and (extra_cheese == "N"):
            bill = medium_pizza + m_l_pepperoni
        else:
            bill = medium_pizza
    else:
        if (add_pepperoni == "Y") and (extra_cheese == "Y"):
            bill = small_pizza + small_pepperoni + cheese
        elif (add_pepperoni == "N") and (extra_cheese == "Y"):
            bill = small_pizza + cheese
        elif (add_pepperoni == "Y") and (extra_cheese == "N"):
            bill = small_pizza + small_pepperoni
        else:
            bill = small_pizza
    print(f" Hello, {name}. Your final bill is : $ {bill}")


pizza()
