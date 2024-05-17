def cafe_computer_problem(N, S):
    computers_available = N
    customer_usage = {}
    turned_away = 0

    for customer in S:
        if customer in customer_usage:
            # Customer is departing, free up a computer
            if customer_usage[customer]:
                computers_available += 1
        else:
            # Customer is arriving, check for available computers
            if computers_available > 0:
                computers_available -= 1
                customer_usage[customer] = True  # Mark this customer as having used a computer
            else:
                turned_away += 1
                customer_usage[customer] = False  # Mark this customer as turned away

    return turned_away

# Example usage:
N1 = 3
S1 = "GACCBDDBAGEE"
result1 = cafe_computer_problem(N1, S1)
print("Output for Example 1:", result1)  

N2 = 1
S2 = "ABCBAC"
result2 = cafe_computer_problem(N2, S2)
print("Output for Example 2:", result2)  
