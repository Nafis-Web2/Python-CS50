
def main():

    name = input("What is you'r name: ")

    item_price = float(input("Item price: "))

    how_many_item = int(input("How many items do you have? "))

    original_total = how_many_item * item_price

    discount = 0
    if original_total > 100:
       discount = original_total * .10

    final_total = original_total - discount

    print(f"Customer: {name}")
    print(f"Original Total: ${original_total:.2f}")
    print(f"Discount: ${discount:.2f}")
    print(f"Final Total: ${final_total:.2f}")

main()
