import graphene
from graphene_django import DjangoObjectType
from customerinfo.models import Customer


class CustomerType(DjangoObjectType):
    class Meta:
        model = Customer
        fields = "__all__"
        convert_choices_to_enum = False


class Query(graphene.ObjectType):
    customer = graphene.Field(CustomerType, id=graphene.Int())
    all_customers = graphene.List(CustomerType)

    def resolve_customer(self, info, **kwargs):
        id = kwargs["id"]
        return Customer.objects.get(pk=id)

    def resolve_all_customers(self, info, **kwargs):
        return Customer.objects.all()


schema = graphene.Schema(query=Query)
