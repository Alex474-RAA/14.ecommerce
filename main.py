from src.models import Product, Category

# Проверочный код из условия задачи
if __name__ == "__main__":
    # Создаем товары
    product1 = Product("Samsung Galaxy S23", "Смартфон", 79999.99, 5)
    product2 = Product("iPhone 15", "Смартфон", 89999.99, 3)
    product3 = Product("Xiaomi Redmi Note 12", "Смартфон", 24999.99, 8)

    # Создаем категорию
    smartphones = Category("Смартфоны", "Мобильные телефоны", [product1, product2, product3])

    print("Проверка корректности работы:")
    print(f"Категория: {smartphones.name}")
    print(f"Количество товаров: {len(smartphones.products)}")
    print(f"Общее количество категорий: {Category.category_count}")
    print(f"Общее количество товаров: {Category.product_count}")
