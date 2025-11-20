from src.models import Category, LawnGrass, Product, Smartphone


class TestProduct:
    def test_product_init(self):
        product = Product("Phone", "Smartphone", 500.0, 10)
        assert product.name == "Phone"
        assert product.price == 500.0
        assert product.quantity == 10

    def test_price_setter_positive(self):
        product = Product("Test", "Desc", 100.0, 5)
        product.price = 150.0
        assert product.price == 150.0

    def test_price_setter_negative(self):
        product = Product("Test", "Desc", 100.0, 5)
        product.price = -50.0
        assert product.price == 100.0

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

    def test_product_str_method(self):
        product = Product("Test Product", "Description", 150.0, 8)
        result = str(product)
        assert "Test Product" in result
        assert "150.0 руб." in result
        assert "8 шт." in result

    def test_product_add_method_same_type(self):
        product1 = Product("Product1", "Desc1", 100.0, 5)  # 100*5 = 500
        product2 = Product("Product2", "Desc2", 200.0, 3)  # 200*3 = 600
        total = product1 + product2
        assert total == 1100  # 500 + 600

    def test_product_add_method_different_type(self):
        product = Product("Product", "Desc", 100.0, 5)
        smartphone = Smartphone("Smartphone", "Desc", 500.0, 2, 2.5, "ModelX", 128, "Black")
        try:
            product + smartphone
            assert False, "Should raise TypeError"
        except TypeError:
            assert True


class TestSmartphone:
    def test_smartphone_init(self):
        smartphone = Smartphone(
            "iPhone 15", "Smartphone", 100000.0, 5,
            3.2, "15 Pro", 256, "Black"
        )
        assert smartphone.name == "iPhone 15"
        assert smartphone.price == 100000.0
        assert smartphone.quantity == 5
        assert smartphone.efficiency == 3.2
        assert smartphone.model == "15 Pro"
        assert smartphone.memory == 256
        assert smartphone.color == "Black"

    def test_smartphone_inheritance(self):
        smartphone = Smartphone("Phone", "Desc", 50000.0, 3, 2.5, "Model", 128, "White")
        assert isinstance(smartphone, Product)

    def test_smartphone_add_method_same_type(self):
        phone1 = Smartphone("Phone1", "Desc", 50000.0, 2, 2.5, "M1", 128, "Black")  # 100000
        phone2 = Smartphone("Phone2", "Desc", 60000.0, 3, 3.0, "M2", 256, "White")  # 180000
        total = phone1 + phone2
        assert total == 280000  # 100000 + 180000


class TestLawnGrass:
    def test_lawn_grass_init(self):
        grass = LawnGrass(
            "Green Grass", "Lawn grass", 5000.0, 10,
            "Russia", 14, "Green"
        )
        assert grass.name == "Green Grass"
        assert grass.price == 5000.0
        assert grass.quantity == 10
        assert grass.country == "Russia"
        assert grass.germination_period == 14
        assert grass.color == "Green"

    def test_lawn_grass_inheritance(self):
        grass = LawnGrass("Grass", "Desc", 3000.0, 5, "USA", 10, "Green")
        assert isinstance(grass, Product)

    def test_lawn_grass_add_method_same_type(self):
        grass1 = LawnGrass("Grass1", "Desc", 3000.0, 4, "RU", 10, "Green")  # 12000
        grass2 = LawnGrass("Grass2", "Desc", 4000.0, 3, "USA", 12, "Dark Green")  # 12000
        total = grass1 + grass2
        assert total == 24000  # 12000 + 12000


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

    def test_add_product_method_valid(self):
        category = Category("Test Category", "Desc", [])
        product = Product("New Product", "Desc", 150.0, 8)
        smartphone = Smartphone("Phone", "Desc", 50000.0, 2, 2.5, "Model", 128, "Black")

        category.add_product(product)
        category.add_product(smartphone)

        assert len(category.products_list) == 2
        assert Category.product_count == 2

    def test_add_product_method_invalid(self):
        category = Category("Test Category", "Desc", [])
        try:
            category.add_product("not_a_product")
            assert False, "Should raise TypeError"
        except TypeError:
            assert True

    def test_products_getter(self):
        product1 = Product("Product1", "Desc1", 100.0, 5)
        product2 = Product("Product2", "Desc2", 200.0, 3)
        category = Category("Test Category", "Desc", [product1, product2])

        products_str = category.products
        assert "Product1, 100.0 руб. Остаток: 5 шт." in products_str
        assert "Product2, 200.0 руб. Остаток: 3 шт." in products_str

    def test_category_str_method(self):
        product1 = Product("Product1", "Desc1", 100.0, 5)
        product2 = Product("Product2", "Desc2", 200.0, 3)
        category = Category("Test Category", "Description", [product1, product2])

        result = str(category)
        assert "Test Category" in result
        assert "количество продуктов: 8 шт." in result
