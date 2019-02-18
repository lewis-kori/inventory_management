from django.urls import path
from . import views
app_name='fire'

urlpatterns=[
    path('',views.home,name='home'),
    path('<int:item_id>/',views.details,name='details'),
    path('<int:item_id>/transfer',views.transferitem,name='transfer'),
    path('<int:item_id>/return',views.returnitem,name='return'),
    path('history',views.transact,name='transact'),
    # path(r'<int:tran.client.client_id>/',views.transaction_details,name='trans_history'),

]

