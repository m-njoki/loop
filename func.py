def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount
    20% or higher.
    """

    if discount_percent >= 20:
        # Apply a 20% discount for discounts of 20% or higher and return the final price
        final_price = price * (1 - discount_percent / 100)
        return final_price
    else:
        return price
    
#Get user input
price = float(input("Enter the price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(price, discount_percent)

# Print the final price
print(f"The final price after applying a discount of {discount_percent}% is: {final_price:.2f}")