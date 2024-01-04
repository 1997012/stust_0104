class Chicken:
    def __init__(self, name, flavor, size, price, is_spicy):
        # 炸雞的五個屬性
        self.name = name
        self.flavor = flavor
        self.size = size
        self.price = price
        self.is_spicy = is_spicy

    def display_info(self):
    
        print(f"Chicken: {self.name}")
        print(f"Flavor: {self.flavor}")
        print(f"Size: {self.size}")
        print(f"Price: ${self.price}")
        print("Spicy: Yes" if self.is_spicy else "Spicy: No")
        print()

    def increase_price(self, amount):
        # 炸雞漲價
        self.price += amount
        print(f"{self.name} price increased by ${amount}. New price: ${self.price}")

    def make_spicy(self):
        # 炸雞加辣
        if not self.is_spicy:
            self.is_spicy = True
            print(f"{self.name} is now a spicy chicken!")

    def change_flavor(self, new_flavor):
        # 修改炸雞口味
        self.flavor = new_flavor
        print(f"{self.name} flavor changed to {new_flavor}")


# 4種口味的炸雞
chicken1 = Chicken("Original", "Savory", "Medium", 10.99, False)
chicken2 = Chicken("Spicy", "Hot", "Large", 12.99, True)
chicken3 = Chicken("BBQ", "Smoky", "Small", 9.99, False)
chicken4 = Chicken("Honey Mustard", "Sweet", "Medium", 11.49, False)

#顯示炸雞原始信息
print("Initial Chicken Information:")
chicken1.display_info()
chicken2.display_info()
chicken3.display_info()
chicken4.display_info()

# 使用副函式：增加炸雞價格
chicken1.increase_price(1.5)

# 使用副函式：炸雞加辣
chicken3.make_spicy()

# 使用副函式：更改炸雞口味
chicken4.change_flavor("Garlic Parmesan")

# 顯示通過副函式的結果
print("\nUpdated Chicken Information:")
chicken1.display_info()
chicken2.display_info()
chicken3.display_info()
chicken4.display_info()
