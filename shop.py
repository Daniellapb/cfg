class YouArePoorError(Exception):
    pass


def simulate_shop():
    items = {
        "duck": 10,
        "fancy duck": 50,
        "noble duck": 75,
        "royal duck": 120
    }
    customer_money = 100
    max_purchase_attempts = 3

    try:
        print("Welcome to duck-off!")
        print("We have a range of ducks to suit your needs and budget:")
        for item, price in items.items():
            print(f"{item}: £{price}")

        while max_purchase_attempts > 0:
            print("\nWhich duck would you like to buy today? (or 'exit' to leave the shop):")
            option = input()

            if option == "exit":
                print("Thank you for visiting. Goodbye!")
                return

            try:
                price = items[option]
                if customer_money >= price:
                    print(f"Here's your {option}!")
                    customer_money -= price
                    max_purchase_attempts = 3  # Reset attempts after successful purchase
                else:
                    raise YouArePoorError

            except KeyError:
                print("That's not a duck we have here! Please choose from the stock.")

            except YouArePoorError:
                print("I'm afraid that duck is out of your budget.")

                if max_purchase_attempts > 1:
                    print("Do you have more money? Please let us know how much more money you have found!")
                    try:
                        additional_money = int(input())
                        customer_money += additional_money
                        max_purchase_attempts -= 1
                    except ValueError:
                        raise ValueError("That's not a currency we accept, I'm afraid.")

                else:
                    print("You've tried too many times! Restarting the shop.")
                    simulate_shop()  # Restart the shop simulation

    except ValueError as e:
        print(f"Error: {str(e)}")


simulate_shop()
