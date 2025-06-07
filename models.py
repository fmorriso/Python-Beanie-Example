from beanie import Document

class Products(Document):
    category: str
    name: str
    price: float
    image: str

    class Settings:
        name = 'products'
