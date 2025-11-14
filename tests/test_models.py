from src.models import Product, Category


class TestProduct:
    def test_product_init(self):
        product = Product("Phone", "Smartphone", 500.0, 10)
        assert product.name == "Phone"
        assert product.price == 500.0  # Используем геттер
        assert product.quantity == 10

    def test_price_setter_positive(self):
        product = Product("Test", "Desc", 100.0, 5)
        product.price = 150.0  # Используем сеттер
        assert product.price == 150.0

    def test_price_setter_negative(self):
        product = Product("Test", "Desc", 100.0, 5)
        product.price = -50.0  # Пытаемся установить отрицательную цену
        assert product.price == 100.0  # Цена не должна измениться

    def test_new_product_class_method(self):
        product_data = {
            'name': 'New Product',
            'description': 'New Description',
            'price': 200.0,
            'quantity': 3
        }
        product = Product.new_product(product_data)
        assert product.name == 'New Product'
        assert product.price == 200.0
        assert product.quantity == 3


class TestCategory:
    def setup_method(self):
        Category.category_count = 0
        Category.product_count = 0

    def test_category_init(self):
        product = Product("Test", "Desc", 100.0, 5)
        category = Category("Electronics", "Tech", [product])
        assert category.name == "Electronics"
        assert len(category.products_list) == 1

    def test_counters(self):
        product = Product("Test", "Desc", 100.0, 5)
        Category("Cat1", "Desc", [product])
        Category("Cat2", "Desc", [product, product])
        assert Category.category_count == 2
        assert Category.product_count == 3

    def test_add_product_method(self):
        category = Category("Test Category", "Desc", [])
        product = Product("New Product", "Desc", 150.0, 8)

        initial_count = Category.product_count
        category.add_product(product)

        assert len(category.products_list) == 1
        assert Category.product_count == initial_count + 1

    def test_products_getter(self):
        product1 = Product("Product1", "Desc1", 100.0, 5)
        product2 = Product("Product2", "Desc2", 200.0, 3)
        category = Category("Test Category", "Desc", [product1, product2])

        products_str = category.products
        assert "Product1, 100.0 руб. Остаток: 5 шт." in products_str
        assert "Product2, 200.0 руб. Остаток: 3 шт." in products_str
