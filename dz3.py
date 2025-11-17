class Product:
    def __init__(self, name, price, available=True):
        self.name = name
        self.price = price
        self.available = available

    def __str__(self):
        if self.available:
            status = "Є в наявності"
        else: status = "Немає в наявності"
        return f"{self.name} — {self.price} грн ({status})"


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        if not product.available:
            print(f"Товар '{product.name}' недоступний!")
            return
        self.items.append(product)
        print(f"Товар '{product.name}' додано в кошик.")

    def remove_product(self, product_name):
        for item in self.items:
            if item.name == product_name:
                self.items.remove(item)
                print(f"Товар '{product_name}' видалено з кошика.")
                return
        print(f"Товар '{product_name}' не знайдено в кошику.")

    def total_price(self):
        return sum(item.price for item in self.items)

    def show_cart(self):
        if not self.items:
            print("Кошик порожній.")
            return

        print("Ваш кошик:")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name} — {item.price} грн")
        print(f"\nЗагальна сума: {self.total_price()} грн\n")

if __name__ == "__main__":
    p1 = Product("Ноутбук", 25000)
    p2 = Product("Мишка", 500)
    p3 = Product("Клавіатура", 1200, available=False)

    cart = Cart()

    cart.add_product(p1)
    cart.add_product(p2)
    cart.add_product(p3)

    cart.show_cart()

    cart.remove_product("Мишка")

    cart.show_cart()