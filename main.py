from src.models import Category, Product

if __name__ == "__main__":
    # Создаем товары
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Тестируем строковое представление товаров
    print("=== СТРОКОВОЕ ПРЕДСТАВЛЕНИЕ ТОВАРОВ ===")
    print(product1)
    print(product2)
    print(product3)

    # Создаем категорию
    category1 = Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни", [])
    category1.add_product(product1)
    category1.add_product(product2)
    category1.add_product(product3)

    # Тестируем строковое представление категории
    print("\n=== СТРОКОВОЕ ПРЕДСТАВЛЕНИЕ КАТЕГОРИИ ===")
    print(category1)

    # Тестируем магический метод сложения
    print("\n=== ТЕСТ СЛОЖЕНИЯ ТОВАРОВ ===")
    total_value = product1 + product2
    print(f"Общая стоимость {product1.name} и {product2.name}: {total_value} руб.")

    # Создаем еще товары для тестирования
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    product5 = Product("PlayStation 5", "Игровая консоль", 49990.0, 3)

    # Тестируем сложение разных товаров
    total_value2 = product4 + product5
    print(f"Общая стоимость {product4.name} и {product5.name}: {total_value2} руб.")

    # Создаем вторую категорию
    category2 = Category("Телевизоры", "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником", [])
    category2.add_product(product4)

    print("\n=== СТАТИСТИКА ===")
    print(f"Категорий: {Category.category_count}")
    print(f"Товаров: {Category.product_count}")
