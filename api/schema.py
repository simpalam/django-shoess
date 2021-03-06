
import graphene
from .models import *
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene import relay ,ObjectType
from graphql_relay.node.node import from_global_id

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
              'email':['icontains','istartswith','exact'],
            'status':['exact','icontains']
        }
        interfaces=(relay.Node,)


class CartProductNode(DjangoObjectType):
    class Meta:
        model=CartProduct
        fields='__all__'
        filter_fields={
            'user_id':['exact','icontains','istartswith'],
             'name':['icontains','istartswith','exact'],
              'productid':['icontains','istartswith','exact'],
            'status':['exact','icontains']
        }
        interfaces=(relay.Node,)

# class BookInput(graphene.InputObjectType):
#     id = graphene.ID()
#     title = graphene.String()
#     author = graphene.String()
#     year_published = graphene.String()
#     review = graphene.Int() 

class CartProductInput(graphene.InputObjectType):
    id=graphene.ID()
    user_id=graphene.String()
    productid=graphene.String()
    name=graphene.String()
    price=graphene.String()
    salePrice=graphene.String()
    image=graphene.String()
    status=graphene.String()
    color=graphene.String()

class OrderInput(graphene.InputObjectType):
    id=graphene.ID()
    user_id=graphene.String()
    productName=graphene.String()
    color=graphene.String()
    size=graphene.Int()
    price=graphene.String()
    image=graphene.String()
    deliverycharge=graphene.String()
    status=graphene.String()
    name=graphene.String()
    phone=graphene.String()
    email=graphene.String()
    address=graphene.String()

class CreateCartProduct(graphene.Mutation):
    class Arguments:
        cart_data=CartProductInput(required=True)
    cartproduct=graphene.Field(CartProductNode)

    @staticmethod
    def mutate(root,info,cart_data):
        cartproduct_instance = CartProduct(
            user_id=cart_data.user_id,
            productid=cart_data.productid,
            name=cart_data.name,
            image=cart_data.image,
            color=cart_data.color,
            price=cart_data.price,
            salePrice=cart_data.salePrice,
            status=cart_data.status
        )
        cartproduct_instance.save()
        return CreateCartProduct(cartproduct=cartproduct_instance)

class UpdateCartProduct(graphene.Mutation):
    class Arguments:
        cart_data=CartProductInput(required=True)
    cartproduct=graphene.Field(CartProductNode)
    @staticmethod
    def mutate(root,info,cart_data=None):
        cartproduct_instance=CartProduct.objects.get(pk=from_global_id(cart_data.id)[1])

        if cartproduct_instance:
            cartproduct_instance.user_id=cart_data.user_id
            cartproduct_instance.productid=cart_data.productid
            cartproduct_instance.name=cart_data.name
            cartproduct_instance.image=cart_data.image
            cartproduct_instance.color=cart_data.color
            cartproduct_instance.price=cart_data.price
            cartproduct_instance.salePrice=cart_data.salePrice
            cartproduct_instance.status=cart_data.status

            cartproduct_instance.save()
            return UpdateCartProduct(cartproduct=cartproduct_instance)
        return UpdateCartProduct(cartproduct=None)

class DeleteCartProduct(graphene.Mutation):
    class Arguments:
        id=graphene.ID()
    cartproduct=graphene.Field(CartProductNode)
    @staticmethod
    def mutate(root,info,id):
        cartproduct_instance=CartProduct.objects.get(pk=from_global_id(id)[1])
        cartproduct_instance.delete()
        return None

class CreateOrder(graphene.Mutation):
    class Arguments:
        order_data=OrderInput(required=True)
    
    order=graphene.Field(OrderNode)
    @staticmethod
    def mutate(root,info,order_data):
        order_instance = Order(
            user_id=order_data.user_id,
            productName=order_data.productName,
            color=order_data.color,
            size=order_data.size,
            price=order_data.price,
            image=order_data.image,
            deliverycharge=order_data.deliverycharge,
            status=order_data.status,
            name=order_data.name,
            phone=order_data.phone,
            email=order_data.email,
            address=order_data.address
        )
        order_instance.save()
        return CreateOrder(order=order_instance)

class UpdateOrder(graphene.Mutation):
    class Arguments:
        order_data=OrderInput(required=True)
    order=graphene.Field(OrderNode)
    @staticmethod
    def mutate(root,info,order_data=None):
        order_instance=Order.objects.get(pk=from_global_id(order_data.id)[1])

        if order_instance:
            order_instance.user_id=order_data.user_id
            order_instance.productName=order_data.productName
            order_instance.color=order_data.color
            order_instance.size=order_data.size
            order_instance.price=order_data.price
            order_instance.image=order_data.image
            order_instance.deliverycharge=order_data.deliverycharge
            order_instance.status=order_data.status
            order_instance.name=order_data.name
            order_instance.phone=order_data.phone
            order_instance.email=order_data.email
            order_instance.address=order_data.address
            order_instance.save()

            return UpdateOrder(order=order_instance)
        return UpdateOrder(order=None)
        
class DeleteOrder(graphene.Mutation):
    class Arguments:
        id=graphene.ID()
    order=graphene.Field(CartProductNode)
    @staticmethod
    def mutate(root,info,id):
        order_instance=Order.objects.get(pk=from_global_id(id)[1])
        order_instance.delete()
        return None

class Mutation(graphene.ObjectType):
    create_order=CreateOrder.Field()
    update_order=UpdateOrder.Field()
    delete_order=DeleteOrder.Field()

    create_cartproduct=CreateCartProduct.Field()
    update_cartproduct=UpdateCartProduct.Field()
    delete_cartproduct=DeleteCartProduct.Field()

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

    cartproduct=relay.Node.Field(CartProductNode)
    all_cartpeoducts=DjangoFilterConnectionField(CartProductNode)

 

