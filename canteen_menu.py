menu = {
    1: {"name": "Burger", "price": 80},
    2: {"name": "Pizza", "price": 120},
    3: {"name": "Sandwich", "price": 60},
    4: {"name": "Cold Coffee", "price": 70},
    5: {"name": "French Fries", "price": 50}
}
menu
cart = []

while True:
    print("MINI CANTEEN")
    print("1. Display Menu")
    print("2. Add Food Item")
    print("3. Remove Food Item")
    print("4. View Cart")
    print("5. Generate Bill")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("MENU")
        for key, item in menu.items():
            print(key, item["name"], "- ₹", item["price"])

    elif choice == 2:
        print("MENU")
        for key, item in menu.items():
            print(key, item["name"], "- ₹", item["price"])

        item_no = int(input("Enter item number: "))
        if item_no in menu:
            quantity = int(input("Enter quantity: "))

            if quantity > 0:
                cart.append({
                    "name": menu[item_no]["name"],
                    "price": menu[item_no]["price"],
                    "quantity": quantity
                })
                print("Item added to cart.")
            else:
                print("Quantity must be greater than 0.")
        else:
            print("Invalid item number.")

    elif choice == 3:
        if len(cart) == 0:
            print("Cart is empty.")
        else:
            print("CART")
            for i in range(len(cart)):
                print(i + 1, cart[i]["name"], "x", cart[i]["quantity"])

            remove_no = int(input("Enter item number to remove: "))

            if 1 <= remove_no <= len(cart):
                cart.pop(remove_no - 1)
                print("Item removed.")
            else:
                print("Invalid choice.")

    elif choice == 4:
        if len(cart) == 0:
            print("Cart is empty.")
        else:
            print("YOUR CART")
            for item in cart:
                amount = item["price"] * item["quantity"]
                print(item["name"], "x", item["quantity"], "=", "₹", amount)

    elif choice == 5:
        if len(cart) == 0:
            print("Cart is empty. Add some items first.")
        else:
            total = 0

            print("BILL")
            for item in cart:
                amount = item["price"] * item["quantity"]
                total = total + amount
                print(item["name"], "x", item["quantity"], "=", "₹", amount)

            if total >= 500:
                discount = total * 10 / 100
                print("Discount (10%) = ₹", discount)
            else:
                discount = 0
                print("Discount = ₹ 0")

            final_amount = total - discount

            print("Total       = ₹", total)
            print("Discount    = ₹", discount)
            print("Final Bill  = ₹", final_amount)

    elif choice == 6:
        print("Thank you for using Mini Canteen!")
        break

    else:
        print("choose between 1-6.")