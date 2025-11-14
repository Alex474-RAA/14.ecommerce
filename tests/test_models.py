from src.models import Product, Category


class TestProduct:
    def test_product_init(self):
        product = Product("Phone", "Smartphone", 500.0, 10)
        assert product.name == "Phone"
        assert product.price == 500.0
        assert product.quantity == 10


class TestCategory:
    def setup_method(self):
        Category.category_count = 0
        Category.product_count = 0

    def test_category_init(self):
        product = Product("Test", "Desc", 100.0, 5)
        category = Category("Electronics", "Tech", [product])
        assert category.name == "Electronics"
        assert len(category.products) == 1

    def test_counters(self):
        product = Product("Test", "Desc", 100.0, 5)
        Category("Cat1", "Desc", [product])
        Category("Cat2", "Desc", [product, product])
        assert Category.category_count == 2
        assert Category.product_count == 3
    def test_product_repr(self):
        product = Product("Test", "Desc", 100.0, 5)
        assert "Product('Test', 'Desc', 100.0, 5)" in repr(product)
