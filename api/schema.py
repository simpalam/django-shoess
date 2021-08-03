
import graphene
from .models import *
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene import relay ,ObjectType

class ColorNode(DjangoObjectType):
    class Meta:
        model=Color
        fields='__all__'
        filter_fields=[]
        interfaces=(relay.Node,)


class SizeNode(DjangoObjectType):
    class Meta:
        model=Size
        fields='__all__'
        filter_fields=[]
        interfaces=(relay.Node,)


class GalleryNode(DjangoObjectType):
    class Meta:
        model=Gallery
        fields='__all__'
        filter_fields=[]
        interfaces=(relay.Node,)

class ProductNode(DjangoObjectType):
    class Meta:
        model=Product
        fields='__all__'
        filter_fields={
            'name':['icontains','istartswith','exact'],
            'slug':['icontains','istartswith','exact'],
            'type':['exact','icontains'],
            'salePrice':['lt','gt'],
            'discountInPercent':['lt','gt']
        }
        interfaces=(relay.Node,)

class ChildrenNode(DjangoObjectType):
    class Meta:
        model=Children
        fields='__all__'
        filter_fields={
            'title':['icontains','istartswith','exact'],
             'slug':['icontains','istartswith','exact'],
            'type':['exact','icontains']
        }
        interfaces=(relay.Node,)

class CategoryNode(DjangoObjectType):
    class Meta:
        model=Category
        fields='__all__'
        filter_fields={
            'title':['exact','icontains','istartswith'],
             'slug':['icontains','istartswith','exact'],
            'type':['exact','icontains']
        }
        interfaces=(relay.Node,)


class OrderNode(DjangoObjectType):
    class Meta:
        model=Order
        fields='__all__'
        filter_fields={
            'user_id':['exact','icontains','istartswith'],
             'name':['icontains','istartswith','exact'],
            'status':['exact','icontains']
        }
        interfaces=(relay.Node,)

class Query(graphene.ObjectType):
    size=relay.Node.Field(SizeNode)
    all_sizes=DjangoFilterConnectionField(SizeNode)


    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    product = relay.Node.Field(ProductNode)
    all_products = DjangoFilterConnectionField(ProductNode)

    children = relay.Node.Field(ChildrenNode)
    all_children = DjangoFilterConnectionField(ChildrenNode)

    order=relay.Node.Field(OrderNode)
    all_ordeers=DjangoFilterConnectionField(OrderNode)

 

