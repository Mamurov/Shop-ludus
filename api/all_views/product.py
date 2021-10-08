from rest_framework import status
from api.all_serializers.product import ProductSerializer
from api.all_models.product import Product
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Product
from django.shortcuts import get_object_or_404


sortKeys = ["limit", "offset", "orderby"];
filterKeys = ["catalog", "subcatalog", "category", "min", "max"]
orderByTypes = ["id", "-id", "-price_kg", "price_kg", "price_ru", "-price_ru"]


def outOffset(offset):
    if isinstance(offset, type(1)):
        return offset;
    if isinstance(offset, type("")):
        return int(offset);
def outLimits(querySettings):
    if querySettings["limit"]:
        return outOffset(querySettings["offset"]) + int(querySettings["limit"]);
    return None;
def outOrderBy(orderby):
    for item in orderByTypes:
        if orderby == item:
            return item;
    
    return orderByTypes[0];

class ProductView(APIView):
    def get(self, request):
        params = request.query_params;
        querySettings = {
            'offset': 0,
            'orderby': orderByTypes[0],
            'limit': None
        }
        filter = {}
        currency = params.get('currency', "kg");
        for key in sortKeys:
            if params.get(key, ""):
                querySettings[key] = params.get(key, "");
        for key in filterKeys:
            if params.get(key, ""):
                filter[key] = int(params.get(key, ""));
        if params.get("price_range", ""):
            price_range = params.get("price_range", "").split(",");
            filter["price_"+ currency +"__gte"] = int(price_range[0]);
            filter["price_"+ currency +"__lte"] = int(price_range[1]);
        data = Product.objects.filter(**filter).order_by(outOrderBy(querySettings["orderby"]))[outOffset(querySettings["offset"]):outLimits(querySettings=querySettings)];
        serializer = ProductSerializer(data, many=True, context={'request': request});
        return Response(data=serializer.data);

class ProductCountView(APIView):
    def get(self, request):
        params = request.query_params;
        filter = {}
        currency = params.get('currency', "kg");
        for key in filterKeys:
            if params.get(key, ""):
                filter[key] = int(params.get(key, ""));
        if params.get("price_range", ""):
            price_range = params.get("price_range", "").split(",");
            filter["price_"+ currency +"__gte"] = int(price_range[0]);
            filter["price_"+ currency +"__lte"] = int(price_range[1]);
        count = Product.objects.filter(**filter).count();
        return Response(count);

class ProductSearchView(APIView):
    def get(self, request, query):
        products = list(Product.objects.filter(title__contains=query));
        if not products:
            return Response(status=status.HTTP_404_NOT_FOUND);
        serializer = ProductSerializer(products, many=True, context={'request': request});
        return Response(serializer.data);

class ProductByIdView(APIView):
    def get(self, request, id): 
        data = get_object_or_404(Product, id=id);
        serializer = ProductSerializer(data, context={'request': request});
        return Response(serializer.data);