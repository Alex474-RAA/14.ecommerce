from models import Product, Category

# Создаем товары
product1 = Product("iPhone", "Smartphone", 999.99, 5)
product2 = Product("MacBook", "Laptop", 1999.99, 3)

# Создаем категорию
electronics = Category("Electronics", "Tech devices", [product1, product2])

print(f"Категорий: {Category.category_count}")
print(f"Товаров: {Category.product_count}")
print(f"Товары в {electronics.name}: {[p.name for p in electronics.products]}")
