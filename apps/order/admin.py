from django.contrib import admin
from apps.order.models import *
# Register your models here.
class SOrderAdmin(admin.ModelAdmin):
	list_display = ('user_id', 'goods_id', 'addr_id','goods_price','goods_num','goods_ex_price','order_price','payment_method','order_status')
	search_fields = ('user_id', 'goods_id', 'addr_id','goods_price','goods_num','goods_ex_price','order_price','payment_method','order_status')
	list_filter = ['user_id', 'goods_id', 'addr_id','goods_price','goods_num','goods_ex_price','order_price','payment_method','order_status']

admin.site.register(SOrder,SOrderAdmin)
