from abc import ABC, abstractmethod


class LogMixin:
    """Миксин для логирования создания объектов"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Не вызываем __repr__ здесь, чтобы избежать проблем с порядком инициализации
        print(f"Создан объект: {self.__class__.__name__}")


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, value):
        pass


class Product(BaseProduct, LogMixin):
    """Основной класс продукта, наследует от BaseProduct и LogMixin"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        BaseProduct.__init__(self, name, description, price, quantity)
        LogMixin.__init__(self)  # Просто логируем факт создания

    def __str__(self):
        return f"{self.name}, {self._price} руб. Остаток: {self.quantity} шт."

    def __repr__(self):
        return f"Product('{self.name}', '{self.description}', {self._price}, {self.quantity})"

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных классов")
        return (self._price * self.quantity) + (other._price * other.quantity)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self._price = new_price

    @classmethod
    def new_product(cls, product_data: dict):
        return cls(
            name=product_data['name'],
            description=product_data['description'],
            price=product_data['price'],
            quantity=product_data['quantity']
        )


class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __repr__(self):
        return f"Smartphone('{self.name}', '{self.description}', {self.price}, {self.quantity}, {self.efficiency}, '{self.model}', {self.memory}, '{self.color}')"


class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: int, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __repr__(self):
        return f"LawnGrass('{self.name}', '{self.description}', {self.price}, {self.quantity}, '{self.country}', {self.germination_period}, '{self.color}')"


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product):
        if not isinstance(product, BaseProduct):
            raise TypeError("Можно добавлять только объекты класса BaseProduct или его наследников")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        return "\n".join(str(product) for product in self.__products)

    @property
    def products_list(self):
        return self.__products
