import mysql.connector as sqlcon

mycon=sqlcon.connect(host='127.0.0.1', user='root', passwd='mysqlM#4374', database='healthfirst')

if mycon.is_connected():
    print("succesfully connected")

cur=mycon.cursor()



while True:
    print("Welcome to Heathfirst Database :)) ")
    print(" Enter 1 for embedded queries")
    print(" Enter 2 for OLAP queries")
    print(" Enter 3 to see working of triggers")
    print(" Enter 4 to exit Heathfirst database")

    x=int(input("Enter your choice: "))

    if x==1:
        print(" 1- List of customers who have their orders below 200")
        print(" 2- Filter list of customers from illness ID 10")
        y=int(input("Enter your choice: "))
        if y==1:
            cur.execute('SELECT * FROM product INNER JOIN customer ON product.customer_ID = customer.customer_ID where product_price<200; ')
            customers=cur.fetchall()
            print("Product name, Product_ID,Product availability,price,expiry,manufacturing,customer_ID,category_ID,f_name,l_name,DOB")
            for i in customers:
                print(i)

        elif y==2:
            cur.execute('select customer_Id,f_name,l_name from recommends natural join customer where illness_ID=10;')
            customer1=cur.fetchall()
            print("Customer_ID,First name, Last name")
            for i in customer1:
                print(i) 

    elif x==2:
        print("1- Give the total stock in each category of each supplier")
        print("2- Show all transactions sanctioned by both both the Admins and their success status total")
        print("3- Show the total number of products recommended to each customer_id for a disease from each category and then total")
        print("4- Give the total count of medicines expiring in each category on a specific date")
        y=int(input("Enter your choice:"))
    
        if y==1:
            query="""
               SELECT product.category_ID,manufactures.supplier_ID, SUM(product.product_availability * product.product_price) AS 'Total Price'
                FROM product
                JOIN manufactures on  product.product_ID = manufactures.product_ID
                GROUP BY manufactures.supplier_ID,product.category_ID WITH ROLLUP;"""
            cur.execute(query)
            product_table=cur.fetchall()
            print("(Category_ID, Supplier_ID, Total Stock value)")
            for i in product_table:
                print(i)


        elif y==2:
            query = """
                select access.admin_ID,order_dispatch.transaction_success,count(access.customer_ID)
                from access
                join order_dispatch on
                access.customer_ID=order_dispatch.customer_ID 
                group by access.admin_ID,order_dispatch.transaction_success with rollup;
                """
            cur.execute(query)
            stock=cur.fetchall()
            print("(Admin_ID, transaction success(0/1/" " " "), Total)")
            for i in stock:
                print(i)

        elif y==3:

            query="""
            select recommends.customer_ID,recommends.category_ID,count(recommends.product_ID) 
            from recommends 
            group by customer_ID,category_ID with rollup;

            update recommends set customer_ID=3 where product_id=1
            """
            cur.execute(query)
            print("Customer_ID, category_ID, count of recommended products")
            product=cur.fetchall()
            for i in product:
                print(i)


        elif y==4:
            query="""
            select YEAR(product_expiry) as year,MONTH(product_expiry) AS month ,category_ID,count(product_id) from product 
            where product_availability>100
            group by YEAR,MONTH,category_ID with rollup;"""
            cur.execute(query)
            category_totals=cur.fetchall()
            print("year, month, category_ID, count of products")
            for i in category_totals:
                print(i)

    elif x==3:
        print(" Enter 1- to see the timestamp of customer updation table incase of updation")
        print(" Enter2- to see the successful order updation in successful order table with timestamp")

        a=int(input("Enter your choice:"))

        if a==1:
            query1="""
            Update Customer Set f_name = 'khwaish' Where customer_ID = 1;"""
            cur.execute(query1)
            mycon.commit()
            query2="""
                select * from customer_log"""
            cur.execute(query2)
            print("Log_ID, CUSTOMER_id, First name, last name, DOB,action, timestamp of updation")
            customer_logs=cur.fetchall()
            for i in customer_logs:
                print(i)

        if a==2:
            query1="""
                UPDATE order_dispatch SET transaction_success ='1' WHERE tracking_ID = 22;"""
            cur.execute(query1)
            mycon.commit()
            query2="""
            select * from successful_ders"""
            cur.execute(query2)
            successfull_orders=cur.fetchall()
            print("Log_ID, Tracking_ID, Customer_ID, Payment_ID, Transaction success, action, Timestamp")
            for i in successfull_orders:
                print(i)
    
    elif x==4:
        print(" Thank you! :)")
        break
        
        

    



# print("Welcome to Heathfirst Database :)) ")
# print(" Enter 1 for embedded queries")
# print(" Enter 2 for OLAP queries")
# print(" Enter 3 to see working of triggers")

# x=int(input("Enter your choice: "))

# if x==1:
#     print(" 1- List of customers who have their orders below 200")
#     print(" 2- Filter list of customers from illness ID 10")
#     y=int(input("Enter your choice: "))
#     if y==1:
#         cur.execute('SELECT * FROM product INNER JOIN customer ON product.customer_ID = customer.customer_ID where product_price<200; ')
#         customers=cur.fetchall()
#         for i in customers:
#             print(i)

#     elif y==2:
#         cur.execute('select customer_Id from recommends where illness_ID=10;')
#         customer1=cur.fetchall()
#         for i in customer1:
#             print(i) 

# elif x==2:
#     print("1- Give the total stock in each category of each supplier")
#     print("2- Show all transactions sanctioned by both both the Admins and their success status total")
#     print("3- Give the product with the least duration of time between manufacturing and expiry")
#     print("4- Give the total number of products in each product category")
#     y=int(input("Enter your choice:"))
    
#     if y==1:
#         query="""
#                SELECT product.category_ID,manufactures.supplier_ID, SUM(product.product_availability * product.product_price) AS 'Total Price'
#                 FROM product
#                 JOIN manufactures on  product.product_ID = manufactures.product_ID
#                 GROUP BY manufactures.supplier_ID,product.category_ID WITH ROLLUP;"""
#         cur.execute(query)
#         product_table=cur.fetchall()
#         print("(Category_ID, Supplier_ID, Total Stock value)")
#         for i in product_table:
#             print(i)


#     elif y==2:
#         query = """
#                 select access.admin_ID,order_dispatch.transaction_success,count(access.customer_ID)
#                 from access
#                 join order_dispatch on
#                 access.customer_ID=order_dispatch.customer_ID 
#                 group by access.admin_ID,order_dispatch.transaction_success with rollup;
#                 """
#         cur.execute(query)
#         stock=cur.fetchall()
#         print("(Admin_ID, transaction success(0/1/""), Total)")
#         for i in stock:
#             print(i)

#     elif y==3:

#         query="""
#             SELECT product_name,
#                 product_expiry,
#                 Product_id,
#                 product_manufacture
#             FROM 
#                 Product
#             WHERE 
#                 product_expiry = (SELECT MIN(product_expiry)
#             FROM 
#                 Product);
#             """
#         cur.execute(query)
#         product=cur.fetchall()
#         print(product)


#     elif y==4:
#         query="""
#             SELECT category_ID, COUNT(product_ID) 
#             FROM product
#             GROUP BY category_ID WITH ROLLUP"""
#         cur.execute(query)
#         category_totals=cur.fetchall()
#         for i in category_totals:
#             print(i)

# elif x==3:
#     print(" Enter 1- to see the timestamp of customer updation table incase of updation")
#     print(" Enter2- to see the successful order updation in successful order table with timestamp")

#     a=int(input("Enter your choice:"))

#     if a==1:
#         query1="""
#             Update Customer Set f_name = 'khwaish' Where customer_ID = 1;"""
#         cur.execute(query1)
#         mycon.commit()
#         query2="""
#             select * from customer_log"""
#         cur.execute(query2)
#         customer_logs=cur.fetchall()
#         for i in customer_logs:
#             print(i)

#     if a==2:
#         query1="""
#             UPDATE order_dispatch SET transaction_success ='1' WHERE tracking_ID = 22;"""
#         cur.execute(query1)
#         mycon.commit()
#         query2="""
#             select * from successful_ders"""
#         cur.execute(query2)
#         successfull_orders=cur.fetchall()
#         for i in successfull_orders:
#             print(i)
    
   

mycon.close()
