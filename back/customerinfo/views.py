from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from customerinfo.models import Customer
from customerinfo.serializer import CustomerSerializer


@api_view(["GET"])
def customers(request):
    all_customers = Customer.objects.all()
    serializer = CustomerSerializer(all_customers, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def customer_by_id(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    serializer = CustomerSerializer(customer, many=False)
    return Response(serializer.data)
