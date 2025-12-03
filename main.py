import products
import store


product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250),
]
best_buy = store.Store(product_list)


def start(store_obj):

    options = [
        "List all products in store",
        "Show total amount in store",
        "Make an order",
        "Quit",
    ]

    while True:
        print("  Store Menu")
        print("  ----------")

        for i, opt in enumerate(options, start=1):
            print(f"{i}. {opt}")

        input_option = int(input("Please choose a number: "))

        if input_option == 1:
            print("----------")
            list_all_active_products = store_obj.get_all_products()
            for i, product in enumerate(list_all_active_products, start=1):
                print(f"{i}. {product.show()}")
            print("----------\n")

        elif input_option == 2:
            total_item_amount = store_obj.get_total_quantity()
            print(f"Total of {total_item_amount} items in store.\n")

        elif input_option == 3:
            print("----------")
            active_products = store_obj.get_all_products()
            for i, product in enumerate(active_products, start=1):
                print(f"{i}. {product.show()}")
            print("----------")
            print("When you want to finish order, enter empty text.")

            order_list = []

            while True:
                product_choice = input(f"Which product # do you want? ")

                if product_choice == "":
                    break

                product_choice = int(product_choice)
                product_index = int(product_choice) - 1

                product_amount = int(input(f"What amount do you want? "))
                order_list.append((active_products[product_index], product_amount))

            try:
                total = store_obj.order(order_list)
                print(f"\nOrder successful! Total price: ${total}\n")
            except Exception as e:
                print("Error", e)

        elif input_option == 4:
            exit()


if __name__ == "__main__":
    start(best_buy)
