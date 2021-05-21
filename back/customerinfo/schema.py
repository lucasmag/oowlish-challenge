import graphene
from graphene_django import DjangoObjectType

from customerinfo.models import Customer, City


class CustomerType(DjangoObjectType):
    class Meta:
        model = Customer
        fields = "__all__"
        convert_choices_to_enum = False


class City(DjangoObjectType):
    class Meta:
        model = City


class Query(graphene.ObjectType):
    customer = graphene.Field(CustomerType, id=graphene.Int())
    all_customers = graphene.List(CustomerType)

    def resolve_customer(self, info, **kwargs):
        id = kwargs.get("id")

        if id is not None:
            return Customer.objects.get(pk=id)

        return None

    def resolve_all_customers(self, info, **kwargs):
        return Customer.objects.all()


schema = graphene.Schema(query=Query)
