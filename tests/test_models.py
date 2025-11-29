import pytest

from src.models import BaseProduct, Category, LawnGrass, Product, Smartphone


class TestBaseProduct:
    def test_base_product_is_abstract(self):
        """Проверяем, что BaseProduct абстрактный"""
        with pytest.raises(TypeError):
            BaseProduct("Test", "Desc", 100.0, 5)


class TestProduct:
    def test_product_zero_quantity_raises_error(self):
        """Проверяем, что товар с нулевым количеством вызывает ValueError"""
        with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
            Product("Invalid Product", "Description", 100.0, 0)

    def test_product_positive_quantity_works(self):
        """Проверяем, что товар с положительным количеством создается нормально"""
        product = Product("Valid Product", "Description", 100.0, 1)
        assert product.quantity == 1

    def test_product_inherits_from_base_product(self):
        product = Product("Phone", "Smartphone", 500.0, 10)
        assert isinstance(product, BaseProduct)

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
        product1 = Product("Product1", "Desc1", 100.0, 5)
        product2 = Product("Product2", "Desc2", 200.0, 3)
        total = product1 + product2
        assert total == 1100

    def test_product_add_method_different_type(self):
        product = Product("Product", "Desc", 100.0, 5)
        smartphone = Smartphone("Smartphone", "Desc", 500.0, 2, 2.5, "ModelX", 128, "Black")
        with pytest.raises(TypeError):
            product + smartphone


class TestSmartphone:
    def test_smartphone_inheritance(self):
        smartphone = Smartphone("Phone", "Desc", 50000.0, 3, 2.5, "Model", 128, "White")
        assert isinstance(smartphone, Product)
        assert isinstance(smartphone, BaseProduct)


class TestLawnGrass:
    def test_lawn_grass_inheritance(self):
        grass = LawnGrass("Grass", "Desc", 3000.0, 5, "USA", 10, "Green")
        assert isinstance(grass, Product)
        assert isinstance(grass, BaseProduct)


class TestCategory:
    def setup_method(self):
        Category.category_count = 0
        Category.product_count = 0

    def test_middle_price_with_products(self):
        """Проверяем расчет средней цены с товарами"""
        product1 = Product("Product1", "Desc1", 100.0, 5)
        product2 = Product("Product2", "Desc2", 200.0, 3)
        product3 = Product("Product3", "Desc3", 300.0, 2)
        category = Category("Test Category", "Desc", [product1, product2, product3])

        # (100 + 200 + 300) / 3 = 200
        assert category.middle_price() == 200.0

    def test_middle_price_empty_category(self):
        """Проверяем расчет средней цены для пустой категории"""
        category = Category("Empty Category", "Desc", [])
        assert category.middle_price() == 0

    def test_middle_price_single_product(self):
        """Проверяем расчет средней цены для одного товара"""
        product = Product("Single Product", "Desc", 150.0, 1)
        category = Category("Single Category", "Desc", [product])
        assert category.middle_price() == 150.0

    def test_add_product_with_base_product_check(self):
        category = Category("Test Category", "Desc", [])
        product = Product("Product", "Desc", 100.0, 5)
        smartphone = Smartphone("Phone", "Desc", 50000.0, 2, 2.5, "Model", 128, "Black")

        category.add_product(product)
        category.add_product(smartphone)

        assert len(category.products_list) == 2

    def test_add_product_invalid_type(self):
        category = Category("Test Category", "Desc", [])
        with pytest.raises(TypeError):
            category.add_product("not_a_product")
