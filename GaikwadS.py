import string;

#Function to Display database
def displaydb(db): 
    # Print the names of the columns. 
    print ("{:<10} {:<18} {:<12} {:<10}".format('PART NO.','PART NAME','SALE-PRICE','QUANTITY'))
    print("---------------------------------------------------")
    #print each data item along with its key in the database 'db' 
    #'db' is sorted using sorted()
    for k,v in (sorted(db.items())):
        key=int(k)
        partname=str(v[0])
        saleprice=float(v[1])
        quant=int(v[2])
        print("{:<10}".format(k),"{:<18} {:<12} {:<10}".format(partname,saleprice,quant))
            
    
#Function to retrieve an item from database
def retrieve(k,db):
#Check if entered key/part number is in database
    if k in db.keys():
        print("Information requested for part no:",k)
        print("{:<10} {:<18} {:<12} {:<10}".format('PART NO.','PART NAME','SALE-PRICE','QUANTITY'))
        print("{:<10}".format(k),"{:<18} {:<12} {:<10}".format(db[k][0],db[k][1],db[k][2]))
            
    else:
        print("Item not in database !!")
       
#Function to place an order for an item
def order(db):
    part=int(input("Enter the part number:"))
    if part in db.keys():
        price=float(db[part][1])
        qty=int(db[part][2])
        
        print("Information of part#:",part)
        print ("{:<10} {:<18} {:<12} {:<10}".format('PART NO.','PART NAME','SALE-PRICE','QUANTITY'))
        print("{:<10}".format(part),"{:<18} {:<12} {:<10}".format(db[part][0],db[part][1],db[part][2]))
        
        numitems=int(input("Enter number of items to order :"))
        
        #Check if order can be fulfilled ,and display order information
        if numitems<=qty:                             
            db[part][2]=qty-numitems
            tax=0.01
            saleTax=tax*price
            totalCost=(price*numitems)+(saleTax*numitems)
            print("-----------")
            print("Your Order")
            print("-----------")
            print("Part number:",part)
            print("Quantity:",numitems)
            print("Tax:10%")
            print("Total-Cost:$",round(totalCost,2))
        else:
            print("Not enough items!!")
        
    else:
        print("Item not in database") 
        
#Function to restock a part already in database
def restock(db):
    part=int(input("Enter the part number:"))
    if part in db.keys():
        print("Current stock quantity for part:",part,"is:",db[part][2],end="")
        stockQty=int(input("\nEnter the number of items to add to existing stock :"))
        qty=int(db[part][2])
        db[part][2]=qty+stockQty
        print("After restocking the updated information for ",part,"is as :")
        print ("{:<10} {:<18} {:<12} {:<10}".format('PART NO.','PART NAME','SALE-PRICE','QUANTITY'))
        print("{:<10}".format(part),"{:<18} {:<12} {:<10}".format(db[part][0],db[part][1],db[part][2]))
        #print(part,db[part][0],db[part][1],db[part][2],end="")
    else:
        print("Item not in database") 
        
#Function to add a new item/part to the inventory/database
def addNewpart(db):
    values=[]
    part=int(input("Enter part number of item:"))
    #value = [item for item in eval(input("Enter the part-name,price,quantity of item: "))]
    values.append(input("Enter the part-name:"))
    values.append(float(input("Enter the price:")))
    values.append(int(input("Enter the quantity of item: ")))
    db[part]=values
    print("Details of new item added:")
    print ("{:<10} {:<18} {:<12} {:<10}".format('PART NO.','PART NAME','SALE-PRICE','QUANTITY'))
    print("{:<10}".format(part),"{:<18} {:<12} {:<10}".format(db[part][0],db[part][1],db[part][2]))
    
    
    
def writeout(finaldb,of):    # Write output final database to file
    outstring=str("PART").ljust(10) +str("PART-NAME").ljust(18)+str("PRICE").ljust(12) +str("QUANTITY").ljust(10)+"\n"
    of.write(outstring)
    for key,values in sorted(finaldb.items()):
        stringdata=str(key).ljust(10)+str(finaldb[key][0]).ljust(18)+str(finaldb[key][1]).ljust(12)+str(finaldb[key][2]).ljust(10)+"\n"
        of.write(stringdata)
    #of.write(str(finaldb))
    
def main():
    print("CS524- programming Assignment1");
    print("Name: Snehal Gaikwad");
    print("Purpose: To implement in-memory database in python using various in built functions,data types such as lists,dictionary,etc")
    
    #open file pythonIn.txt to read 
    inputfile=open("pythonIn.txt","r")   
    
    #Open file pythonOut.txt to write the output to
    outputfile=open("pythonOut.txt","w")
    
    #Create an empty dictionary to read the file contents into
    inventory={}
    values=[]
    #Skip first line from the pythonIn.txt file
    next(inputfile)
    for line in inputfile:
        items=line.split()                  #split the string into a list of strings
        key,values=int(items[0]),items[1:]
        values[0]=str(items[1])
        values[1]=float(items[2])
        values[2]=int(items[3])
        inventory[key]=values
            
    print("\nPrinting dictionary without formatting:")
    print(inventory)
    
    choice=' '
    
    while(choice!='6'):
         #Display menu
        print("\nMain menu : Enter 1-6 ")
        print(" 1. Display Database")
        print(" 2. Retrieve data item")
        print(" 3. Place Order")
        print(" 4. Restock item")
        print(" 5. Add item")
        print(" 6. Terminate")
        
        #Prompt the user and Implement menu using if-elif-else 
        choice=input("\nEnter your choice :")
        if (choice=='1'):                       #Display database
            displaydb(inventory)
        elif(choice=='2'):                       #Retrieve an item from database
            part=int(input("Enter the part number :"))     #part number is key
            retrieve(part,inventory)
        elif(choice=='3'):
            print("\nPlace an order for a item from database:")
            order(inventory)
        elif(choice=='4'):
            print("\nEnter details for item to be restocked:")
            restock(inventory)
        elif(choice=='5'):
            print("\nEnter details of new item to be added to the inventory:")
            addNewpart(inventory)
        elif(choice=='6'):
            writeout(inventory,outputfile)
            
        else:
            print("Error:Enter correct choice!!")
    #Close the pytonIn.txt and pythonOut.txt files      
    inputfile.close()
    outputfile.close()
main()