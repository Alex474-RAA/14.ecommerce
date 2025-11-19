from src.models import Category, Product, Smartphone, LawnGrass

if __name__ == "__main__":
    # Создаем обычные товары
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    # Создаем смартфоны
    smartphone1 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14,
                             2.5, "Redmi Note 11", 128, "Синий")
    smartphone2 = Smartphone("Google Pixel 8", "128GB, Black", 75000.0, 6,
                             3.2, "Pixel 8", 256, "Черный")

    # Создаем газонную траву
    lawn_grass1 = LawnGrass("Газонная трава Premium", "Высококачественная газонная трава",
                            5000.0, 20, "Россия", 14, "Зеленый")
    lawn_grass2 = LawnGrass("Газонная трава Standard", "Стандартная газонная трава",
                            3000.0, 15, "Беларусь", 21, "Темно-зеленый")

    # Создаем категории и добавляем товары
    smartphones_category = Category("Смартфоны",
                                    "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                                    [])
    smartphones_category.add_product(product1)
    smartphones_category.add_product(product2)
    smartphones_category.add_product(smartphone1)
    smartphones_category.add_product(smartphone2)

    lawn_grass_category = Category("Газонная трава",
                                   "Газонная трава для вашего сада",
                                   [])
    lawn_grass_category.add_product(lawn_grass1)
    lawn_grass_category.add_product(lawn_grass2)

    # Тестируем строковые представления
    print("=== КАТЕГОРИИ И ТОВАРЫ ===")
    print(smartphones_category)
    print(lawn_grass_category)

    print("\n=== ТОВАРЫ В КАТЕГОРИИ СМАРТФОНЫ ===")
    print(smartphones_category.products)

    print("\n=== ТОВАРЫ В КАТЕГОРИИ ГАЗОННАЯ ТРАВА ===")
    print(lawn_grass_category.products)

    # Тестируем сложение товаров одного типа
    print("\n=== ТЕСТ СЛОЖЕНИЯ ОДИНАКОВЫХ ТОВАРОВ ===")
    try:
        total_smartphones = smartphone1 + smartphone2
        print(f"Общая стоимость смартфонов: {total_smartphones} руб.")
    except TypeError as e:
        print(f"Ошибка: {e}")

    try:
        total_grass = lawn_grass1 + lawn_grass2
        print(f"Общая стоимость газонной травы: {total_grass} руб.")
    except TypeError as e:
        print(f"Ошибка: {e}")

    # Тестируем сложение товаров разных типов
    print("\n=== ТЕСТ СЛОЖЕНИЯ РАЗНЫХ ТОВАРОВ ===")
    try:
        invalid_total = smartphone1 + lawn_grass1
        print(f"Результат: {invalid_total}")
    except TypeError as e:
        print(f"Ошибка (ожидаемо): {e}")

    # Тестируем добавление неверного типа в категорию
    print("\n=== ТЕСТ ДОБАВЛЕНИЯ НЕВЕРНОГО ТИПА ===")
    try:
        smartphones_category.add_product("не товар")
        print("Неверный объект добавлен (это ошибка!)")
    except TypeError as e:
        print(f"Ошибка (ожидаемо): {e}")

    print("\n=== СТАТИСТИКА ===")
    print(f"Категорий: {Category.category_count}")
    print(f"Товаров: {Category.product_count}")
