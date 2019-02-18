from django import forms
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Category,Item,Client,Transaction
from .serializers import itemsSerializer,transactionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
def home(request):
    items=Item.objects.all()
    context={'items':items}
    return render(request,'fire/home.html',context)

def details(request,item_id):
    item=get_object_or_404(Item,pk=item_id)
    clients=Client.objects.all()
    context={'item':item,'clients':clients}
    return render(request,'fire/details.html',context)

def transferitem(request,item_id):
    client=Client.objects.get(place=request.POST.get('client'))
    item=Item.objects.get(pk=item_id)
    quantity=request.POST.get('quantity')
    transaction=Transaction(quantity=quantity,item=item,client=client)
    transaction.save()
    item.quantity=item.quantity-int(quantity)
    item.save()
    context={'transaction':transaction,'quantity':quantity,'item':item,'client':client}
    return render(request,'fire/transferitem.html',context)

def returnitem(request,item_id):
    client=Client.objects.get(place=request.POST.get('client'))
    item=Item.objects.get(pk=item_id)
    quantity=request.POST.get('quantity')
    transaction=Transaction(quantity=quantity,item=item,client=client)
    transaction.save()
    item.quantity=item.quantity+int(quantity)
    item.save()
    context={'transaction':transaction,'quantity':quantity,'item':item,'client':client}
    return render(request,'fire/returnitem.html',context)
 ##transaction history page
def transact(request):
    clients=Client.objects.all()
    trans=Transaction.objects.all()
    context={'clients':clients,'trans':trans}
    return render(request,'fire/trans_details.html',context)
def transaction_details(request,client_id):
    clients=get_object_or_404(Client,pk=client_id)
    transactions=Transaction.objects.all()
    context={'clients':clients,'transactions':transactions}
    return render(request,'fire/transactions.html',context)
# api views
class itemsView(APIView):
    def get(self,request):
        items=Item.objects.all()
        serializer=itemsSerializer(items,many=True)
        return Response(serializer.data)
    def post(self,request):
        pass
class transactionsView(APIView):
    def get(self,request):
        transactions=Transaction.objects.all()
        serializer=transactionSerializer(transactions,many=True)
        return Response(serializer.data)
    def post(self,request):
        pass