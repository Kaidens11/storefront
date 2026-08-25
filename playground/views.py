from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product, Order, OrderItem
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F

def say_hello(request):
    # Product: inventory < 10 and unit_price < 20
    #queryset = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)
    # Product: inventory < 10 or unit_price < 20
    #queryset = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
    # Product: inventory == unit_price
    #queryset = Product.objects.filter(inventory=F('unit_price'))
    #queryset = Product.objects.filter(inventory=F('collection__id'))

    #queryset = Product.objects.order_by('unit_price', '-title').reverse()
    #queryset = Product.objects.order_by('unit_price')[0:1]
    #return render(request, 'hello.html', {'name': 'Mosh', 'products': list(queryset)})
    
    #product = Product.objects.order_by('unit_price')[0]
    # el mas antiguo
    #product = Product.objects.earliest('unit_price')
    # el mas reciente
    #product = Product.objects.latest('unit_price')
    #return render(request, 'hello.html', {'name': 'Mosh', 'products': [product]})

    # 0, 1, 2, 3, 4
    #queryset = Product.objects.all()[:5]
    # 5, 6, 7, 8, 9
    #queryset = Product.objects.all()[5:10]
    # Muestra los productos en forma de diccionario
    #queryset = Product.objects.values('id', 'title', 'collection__title')
    #queryset = Product.objects.values_list('id', 'title', 'collection__title')
    # Obtiene todos los productos que han sido ordenados/vendidos al menos una vez (sin duplicados)
    #queryset = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct())
    # Optimización: Carga solo las columnas 'id' y 'title' para ahorrar memoria (las demás se cargarán solo si se solicitan)
    #queryset = Product.objects.only('id', 'title')
    # Carga todos los campos del producto EXCEPTO 'id' y 'title' (se traerán solo si se leen después)
    #queryset = Product.objects.defer('id', 'title')
    # Optimización (1 a N): Carga los productos junto con su 'collection' en una sola consulta SQL mediante un INNER JOIN
    #queryset = Product.objects.select_related('collection').all()
    # Carga los productos relacionando 'collection' y además el campo/modelo 'someOtherField' dentro de esa colección en una sola consulta
    #queryset = Product.objects.select_related('collection__someOtherField').all()
    # Carga productos y hace ejecuciones SQL separadas para relaciones 'muchos a muchos' (M2M) o inversas en 'collection'
    #queryset = Product.objects.prefetch_related('collection__someOtherField').all()
    # Carga las últimas 5 órdenes optimizando el acceso al cliente (JOIN) y a sus productos comprados (prefetch)
    queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    return render(request, 'hello.html', {'name': 'Mosh', 'products': list(queryset)})