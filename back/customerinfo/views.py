from rest_framework.decorators import api_view
from rest_framework.response import Response
from customerinfo.models import Customer
from customerinfo.serializer import CustomerSerializer


@api_view(["GET"])
def customers(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def customer_by_id(request, pk):
    customers = Customer.objects.get(id=pk)
    serializer = CustomerSerializer(customers, many=False)
    return Response(serializer.data)
