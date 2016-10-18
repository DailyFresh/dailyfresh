from django.contrib import admin
from apps.goods.models import *

# Register your models here.
class GoodsAdmin(admin.ModelAdmin):
	list_display = ('goods_type_id', 'goods_type_name', 'goods_name','goods_price','goods_unit','goods_ex_price','goods_info','goods_status')
	search_fields = ('goods_type_id', 'goods_type_name', 'goods_name','goods_price','goods_unit','goods_ex_price','goods_info','goods_status')
	list_filter = ['goods_type_id', 'goods_type_name', 'goods_name','goods_price','goods_unit','goods_ex_price','goods_info','goods_status']

admin.site.register(Goods,GoodsAdmin)
