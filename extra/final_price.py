
def main():

    price = float(input("What is the price? "))

    discount = float(input("What is the discount? "))

    final_price = calculate_discount(price,discount)

    print(f"You'r final price is:${final_price:.2f}")


def calculate_discount(price,discount):

    final_price = price - (price * discount / 100)

    return final_price



main()

