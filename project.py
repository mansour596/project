def menu():
    print("________________________________________________________")
    print("Welcome MyBookStore")
    print("1. Books Available")
    print("2. View Customer Account")
    print("3. Add an Account")
    print("4. Update an Account")
    print("5. Delete an Account")
    print("6. Place an Order")
    print("7. View Pending Orders")
    print("8. Cancel Pending Order")
    print("9. Get the latest books")
    print("______________________________")
    print("0. Exit")


def getbooks():
        import json
        from pymongo import MongoClient
        client = MongoClient(port=27017)
        db = client.test
        collection = db.products

        with open("boo.json") as b:
            data = json.load(b)
            collection.insert_many(data)  
            print("New Documents has been uploaded to Database!")

def viewc():
    try:
        print("View Customer Account")
        from pymongo import MongoClient
        from tabulate import tabulate
        
        
    
        client = MongoClient(port=27017)
        db = client.test
        collection = db.customers

        customer = []

        for view in collection.find():
            customer.append(view)
        
    
        print(tabulate(customer, headers="keys"))

    except Exception:
        print("Enter a number! Try again from the start!")
        viewc()
       
def viewp():
    try:
        print("View Our Products")
        from pymongo import MongoClient
        from tabulate import tabulate
        

        client = MongoClient(port=27017)
        db = client.test
        collection = db.products

        products = []
        for view in collection.find():
            products.append(view)

        print(tabulate(products, headers="keys"))

    except Exception:
        print("Enter a number! Try again from the start!")
        viewp()


def ordersp():
    try:
        print("Pending Orders")
        print("Processing your order")
        from pymongo import MongoClient
        from tabulate import tabulate
        

        client = MongoClient(port=27017)
        db = client.test
        collection = db.orders

        orders = []
        for view in collection.find({}, {"_id": False}):          
            orders.append(view)

        print(tabulate(orders, headers="keys"))


    except Exception:
        print("Enter a number! Try again from the start!")
        ordersp()


def orders():
    try:
        print("Place your order")

        from pymongo import MongoClient
        

        client = MongoClient(port=27017)
        db = client.test
        collection = db.orders

        customername = (input("Enter Customer Name: "))
        productid = float(input("Enter the product ID of the book that you want to order: "))
        qty = float(input("Enter the quantity of books: "))
        

        neworder = {"CustomerName" : (customername), "productid": (productid), "Quantity of Books": (qty)}
        collection.insert_one(neworder)
        print("Your Order has been Placed!!!")
        print()
    
    except Exception:
        print("Enter a number! Try again from the start!")
        orders()


def update():
    try:
        print("Update a Document")

        from pymongo import MongoClient
        

        client = MongoClient(port=27017)
        db = client.test
        collection = db.customers
        
        ids = float(input("Enter the ID that you want to update: "))
        fname = input("Enter your Fullname: ")
        cname = input("Enter your contactname: ")
        address = input("Enter your address: ")
        city = input("Enter your city: ")
        pcode = float(input("Enter your postalcode: "))
        country = input("Enter your country: ")


        collection.update_one({"_id": (ids)}, {"$set": {"CustomerName": (fname), "ContactName": (cname), "Address": (address), "City": (city), "PostalCode": (pcode), "Country": (country)}})
        print("Document updated")
        print()
    except Exception:
        print("Enter a number! Try again from the start!")
        update()


def deleteo():
    try:
        print("Cancel a Pending Orders")
        from pymongo import MongoClient
        

        client = MongoClient(port=27017)
        db = client.test
        collection = db.orders

        ids = input("Enter Customer Name: ")
        pids = float(input("Enter product ID: "))
        qty = float(input("Enter the Quantity: "))


        collection.delete_one({"CustomerName" : (ids), "productid": (pids), "Quantity of Books": (qty)})
        print("Order Cancelled!!!")
        print()
    except Exception:
        print("Enter a number! Try again from the start!")
        deleteo()

def deletec():
    try:
        print("Delete a Document")
    

        from pymongo import MongoClient
        

        client = MongoClient(port=27017)
        db = client.test
        collection = db.customers

        ids = float(input("Enter account ID you want to delete: "))

        newdocu = {"_id" : (ids)}
        collection.delete_one(newdocu)
        print("Document deleted")
        print()
    except Exception:
        print("Something went wrong!(Put a number on ID")
        deletec()


def add():
    try:
        print("Add a document")
        print("Remember your Unique ID!")
        from pymongo import MongoClient
        

        client = MongoClient(port=27017)
        db = client.test
        collection = db.customers

        ids = float(input("Enter your ID: "))
        fname = input("Enter your Fullname: ")
        cname = input("Enter your contactname: ")
        address = input("Enter your address: ")
        city = input("Enter your city: ")
        pcode = float(input("Enter your postalcode: "))
        country = input("Enter your country: ")


        newdocu = {"_id" : (ids), "CustomerName": (fname), "ContactName": (cname), "Address": (address), "City": (city), "PostalCode": (pcode), "Country": (country)}

        collection.insert_one(newdocu)
        print("New document addded")
        print()
    except Exception:
        print("Something went wrong!(ID already existed or Put numbers on ID and Postal Code)")
        add()

    




menu()
choices = int(input("Choose an option: "))

while choices != 0:
    if choices == 1:
        viewp()   
    elif choices == 2:
        viewc()
    elif choices == 3:
        add()
    elif choices == 4:
        update()
    elif choices == 5:
        deletec()
    elif choices == 6:
        orders()
    elif choices == 7:
        ordersp()
    elif choices == 8:
        deleteo()
    elif choices == 9:
        getbooks()
    else:
        print()
        print("The number was not on the options. Try again!!!")

    print("________________________________________________________")
    menu()
    choices = int(input("Choose an option: "))

print("Thank you and have a blessed day!")
