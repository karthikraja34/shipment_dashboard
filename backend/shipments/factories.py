import factory

from products.models import Product
from users.models import User, Company
from factory.django import DjangoModelFactory


class CompanyFactory(DjangoModelFactory):
    class Meta:
        model = Company

    name = factory.Faker("name")
    address = factory.Faker("address")
    vat_id = factory.Faker("ean")


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    password = factory.Faker("password")
    company = factory.SubFactory(CompanyFactory)


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product
