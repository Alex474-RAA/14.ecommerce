from src.models import Category, Product

if __name__ == "__main__":
    # Создаем товары
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Создаем категорию и добавляем товары через метод
    category1 = Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни", [])
    category1.add_product(product1)
    category1.add_product(product2)
    category1.add_product(product3)

    # Тестируем геттер products
    print("=== СПИСОК ТОВАРОВ ===")
    print(category1.products)

    # Тестируем класс-метод
    print("\n=== СОЗДАНИЕ ТОВАРА ЧЕРЕЗ КЛАСС-МЕТОД ===")
    new_product_data = {
        'name': 'Google Pixel 8',
        'description': '128GB, Black',
        'price': 75000.0,
        'quantity': 4
    }
    product4 = Product.new_product(new_product_data)
    print(f"Создан товар: {product4.name}, {product4.price} руб.")

    # Тестируем сеттер цены
    print("\n=== ТЕСТ СЕТТЕРА ЦЕНЫ ===")
    print(f"Текущая цена: {product1.price}")
    product1.price = -1000  # Должно вывести сообщение об ошибке
    print(f"Цена после попытки установить -1000: {product1.price}")
    product1.price = 190000.0  # Корректное изменение
    print(f"Цена после установки 190000: {product1.price}")

    # Создаем вторую категорию
    product5 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры", "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником", [])
    category2.add_product(product5)

    print("\n=== СТАТИСТИКА ===")
    print(f"Категорий: {Category.category_count}")
    print(f"Товаров: {Category.product_count}")
