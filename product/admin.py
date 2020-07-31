from django.contrib import admin
from product.models import Product, Category, Images


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    # получение всех полей от 1 до последнего
    # fields = [field.name for field in Product._meta.get_fields()[1:]]
    # отображение полей в товаре
    fields = [
        "name", "user", "category",
        "price", "quantity_purchases",
        "availability_in_store", "deleted",
        "description"
    ]
    # отображение полей в товаре без редакт
    readonly_fields = [
        "name", "user",
        "price", "quantity_purchases",
        "availability_in_store", "deleted",
        "description"
    ]
    # отображение в продукуте
    list_display = [
        "name", "user", "category",
        "price", "quantity_purchases",
        "availability_in_store", "deleted"
    ]
    # ссылка на товар в продкуте
    list_display_links = [
        "name"
    ]
    # редакторование полей разом в продукте
    # есть ограниечние кроме 1 поля list_display
    list_editable = [
        "category", "price"
    ]
    # поиск в продукте
    search_fields = [
        "name",
        "price",
        "description",
        # поле__поле внешего ключа
        "user__username",
        "category__name"
    ]
    # фильтраия в продукте
    list_filter = ["category"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    fields = ["name"]
    list_display = ["id", "name"]
    list_editable = ["name"]
# способ №2 без декоратора (стр 5, 50)
# admin.site.register(Product, ProductAdmin)
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Product)

admin.site.register(Images)