l=[]
class Product:
    def __init__(self,id,name,price,qty):
        self.id = id
        self.name = name
        self.price = price
        self.qty = qty
    def __str__(self) -> str:
        return f'prodcut[{self.id,self.name,self.price,self.qty}]'
class Stationary:
    def __init__(self):
        l.append(Product(1,'pen',10,30))
        l.append(Product(2,'pencil',4,50))
    
    def addstock(self):
        id = int(input('Enter product Id: '))
        filterlist = list(filter(lambda pro:pro.id==id,l))
        if len(filterlist)>0:
            print("id alreday exist...")
            return 
        
        name = input('Enter product name: ')
        price = float(input('Enter product Price: '))
        qty= int(input('Enter product Qty: '))
        product = Product(id,name,price,qty)
        l.append(product)
        print("Product added successfully...")
    def addqty(self):
        take_id=int(input("Enter product id: "))
        filterlist = list(filter(lambda pro:pro.id==take_id,l))
        if len(filterlist)==0:
            print("id does not exist...")
            return
        else:
            for i in l:
                if take_id==i.id:
                    add=int(input("Qty to be added: "))
                    i.qty=i.qty+add
                    print("Quantity added successfully")
    def removeqty(self):
        take_id=int(input("Enter product id: "))
        filterlist = list(filter(lambda pro:pro.id==take_id,l))
        if len(filterlist)==0:
            print("id does not exist...")
            return
        else:
            for i in l:
                if take_id==i.id:
                    remove=int(input("Qty to be removed: "))
                    if i.qty>=remove:
                        i.qty=int(i.qty)-remove
                        print("Quantity removed successfully")
                    else:
                        print("Insufficent qty in inventory")
    def showstock(self):
        print("-----Product List----")
        print("\tid  Name  price  qty")
        for product in l:
            print(product)
            print('-'*30)
    def delpro(self):
        take_id=int(input("Enter product id: "))
        filterlist = list(filter(lambda pro:pro.id==take_id,l))
        if len(filterlist)==0:
            print("id does not exist...")
            return
        else:
            for i in l:
                if take_id==i.id:
                    l.remove(i)
                    print("Data deleted succussfully")
def Inventory():
    s=Stationary()
    sel=0
    while sel!=6:
        try:
            print("")
            print("(1) Add stock in inventory")
            print("(2) Add new product in inventory")
            print("(3) Remove stock from inventory")
            print("(4) Delete product from inventory")
            print("(5) Show all stock")
            print("(6) Exit from Inventory")
            print("")
            sel=int(input("Enter your choice: "))
        except:
            print("Invalid Choice")
        if sel==1:
            s.addqty()
        elif sel==2:
            s.addstock()
        elif sel==3:
            s.removeqty()
        elif sel==4:
            s.delpro()
        elif sel==5:
            s.showstock()
        elif sel==6:
            print("Inventory Closed")
            break
Inventory()
