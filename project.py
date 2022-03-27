def menu():
    print("Welcome to MyBookStore")
    print("1. View Customer Account")
    print("2. Books Available")
    print("3. View Pending Orders")
    print("4. Place an Order")
    print("5. Cancel Pending Order")
    print("6. Add an Account")
    print("7. Update an Account")
    print("8. Delete an Account")
    print("9. View an Account")
    print("---------------------")
    print("0. Exit")

def viewd():
    print("View Database")
    from pymongo import MongoClient
    from pprint import pprint

    client = MongoClient(port=27017)
    db = client.test
    collections = db.list_collection_names()

    for a in range(len(collections)):
        testCollection = collections[a]
        pprint(f"Collection name: {testCollection}")
        colldoc = db.get_collection(testCollection)
        for documents in colldoc.find():
            pprint(documents)


def viewc():
    print("View Customer Account")
    from pymongo import MongoClient
    from pprint import pprint

    client = MongoClient(port=27017)
    db = client.test
    collection = db.customers

    customers = collection.find()
    
    for documents in customers:
        print(documents)

def viewp():
    print("View Our Products")
    from pymongo import MongoClient
    from pprint import pprint

    client = MongoClient(port=27017)
    db = client.test
    collection = db.products

    products = collection.find()
    
    for documents in products:
        print(documents)

def ordersp():
    print("Pending Orders")
    from pymongo import MongoClient
    from pprint import pprint

    client = MongoClient(port=27017)
    db = client.test
    collection = db.orders

    products = collection.find()
    
    for documents in products:
        print(documents)

def orders():
    print("Place your order")

    from pymongo import MongoClient
    from pprint import pprint

    client = MongoClient(port=27017)
    db = client.test
    collection = db.orders

    customerid = int(input("Enter your ID: "))
    productid = int(input("Enter the product ID: "))
    qty = int(input("Enter the quantity of books: "))

    neworder = {"_id" : (customerid), "productid": (productid), "quantity": (qty)}
    collection.insert_one(neworder)
    print("Your Order has been Placed!!!")
    print()



def update():
    print("Update a Document")

    from pymongo import MongoClient
    from pprint import pprint

    client = MongoClient(port=27017)
    db = client.test
    collection = db.customers
    
    ids = int(input("Enter the ID that you want to update: "))
    fname = input("Enter your Fullname: ")
    cname = input("Enter your contactname: ")
    address = input("Enter your address: ")
    city = input("Enter your city: ")
    pcode = int(input("Enter your postalcode: "))
    country = input("Enter your country: ")


    collection.update_one({"_id": (ids)}, {"$set": {"CustomerName": (fname), "ContactName": (cname), "Address": (address), "City": (city), "PostalCode": (pcode), "Country": (country)}})
    print("Document updated")
    print()
    

def deleteo():
    print("Cancel a Pending Orders")
    from pymongo import MongoClient
    from pprint import pprint

    client = MongoClient(port=27017)
    db = client.test
    collection = db.orders

    ids = int(input("Enter order ID you want to cancel: "))

    cancel = {"_id" : (ids)}
    collection.delete_one(cancel)
    print("Order Cancelled!!!")
    print()

def deletec():
    print("Delete a Document")
    

    from pymongo import MongoClient
    from pprint import pprint

    client = MongoClient(port=27017)
    db = client.test
    collection = db.customers

    ids = int(input("Enter ID you want deleted: "))

    newdocu = {"_id" : (ids)}
    collection.delete_one(newdocu)
    print("Document deleted")
    print()


def add():
    print("Add a document")
    from pymongo import MongoClient
    from pprint import pprint

    client = MongoClient(port=27017)
    db = client.test
    collection = db.customers

    ids = int(input("Enter your ID: "))
    fname = input("Enter your Fullname: ")
    cname = input("Enter your contactname: ")
    address = input("Enter your address: ")
    city = input("Enter your city: ")
    pcode = int(input("Enter your postalcode: "))
    country = input("Enter your country: ")


    newdocu = {"_id" : (ids), "CustomerName": (fname), "ContactName": (cname), "Address": (address), "City": (city), "PostalCode": (pcode), "Country": (country)}

    collection.insert_one(newdocu)
    print("New document addded")
    print()

    




menu()
choices = int(input("Choose an option: "))

while choices != 0:
    if choices == 1:
        viewc()   
    elif choices == 2:
        viewp()
    elif choices == 3:
        ordersp()
    elif choices == 4:
        orders()
    elif choices == 5:
        deleteo()
    elif choices == 6:
        add()
    elif choices == 7:
        update()
    elif choices == 8:
        deletec()
    elif choices == 9:
        viewc()
    else:
        print()
        print("The number was not on the options. Try again!!!")

    print("________________________________________________________")
    menu()
    choices = int(input("Choose an option: "))

print("Thank you and have a blessed day!")