from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=50,default='')
    desc = models.CharField(max_length=200,default='')

    def __str__(self):
        return str(self.id)+':'+self.name+':'+self.desc

class Product(models.Model):
    pid = models.CharField(max_length=13,primary_key=True,default='')
    name = models.CharField(max_length=50,default='')
    brand = models.CharField(max_length=30,default='')
    price = models.FloatField (default=0.00)
    net = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.pid + ':'+self.name+':'+self.brand+':'+str(self.price)+':'+str(self.net)+':'+self.category.name
import datetime
class Employee(models.Model):
    eid = models.CharField(max_length=5, default='')
    name = models.CharField(max_length=35,default='')
    surname = models.CharField(max_length=35,default='')
    address = models.CharField(max_length=200,default='')
    gender = models.BooleanField(default=True)
    birthday = models.CharField(max_length=20, default="")
    salary = models.FloatField(default=0.00)



class product11():
    def __init__(self,pid,brand, ptype, size, price, amount, member,):
        self.__pid = pid
        self.__brand = brand
        self.__ptype = ptype
        self.__size = size
        self.__price = price
        self.__amount = amount
        self.__member = member
        self.__setDiscount()
        self.__setSum()
        self.__setNet()





    def __setDiscount(self):
        if self.__member == "y":
            self.__discount = self.__price * 0.5
        else:
            self.__discount = 0

    def __setSum(self):
        self.__sum = self.__price - self.__discount

    def __setNet(self):
        self.__net = self.__sum * self.__amount

    # def __setTotal(self):
    #     self.__setTotal =
    def getId(self):
        return self.__pid
    def getBrand(self):
        return self.__brand
    def getType(self):
        return self.__ptype
    def getSize(self):
        return self.__size
    def getPrice(self):
        return self.__price
    def getAmount(self):
        return self.__amount
    def getMember(self):
        return self.__member

    def getDiscount(self):
        return self.__discount
    def getNet(self):
        return self.__net



