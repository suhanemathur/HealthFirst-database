import mysql.connector as sqlcon

mycon=sqlcon.connect(host='127.0.0.1', user='root', passwd='mysqlM#4374', database='healthfirst')

if mycon.is_connected():
    print("succesfully connected")

cur=mycon.cursor()



while True:
    print("Welcome to Heathfirst Database :)) ")
    print(" Enter 1 for signing in as registered customer to view and update your cart(db transaction used)")
    print(" Enter 2 for registering as a new customer (db transaction used)")
    print(" Enter 3 to sign up as a new supplier (db transaction used)")
    print(" Enter 4 to sign in as a supplier to add a product (db transaction used)")
    print(" Enter 5 to log in as supplier to update the price of a product (db transaction used)")
    

    print()
    x=int(input("Enter your choice: "))

    if x==1:
        user=input("Enter your username:")
        password=input(("Enter your password:"))
        customer_id=input(("Enter your customer_ID:"))
        print()

        print("Welcome to Healthfirst, following is your information:")
        query1=('select f_name, l_name, dob from customer where customer_Id=%s;')
        cur.execute(query1,(customer_id,))

        print("(First name, Last name, DOB)")
        info=cur.fetchall()
        print(info)

        print()
        print("you have these items in your cart presently:")
        print()
        # query2=("""select product_ID,product_name,product_price, product_manufacture,product_expiry
        #              from product join added where customer_ID=%s;""")

        query2=("""SELECT DISTINCT product.product_Id, product.product_name, product.product_price,added.customer_ID
                    FROM added
                    INNER JOIN product ON added.product_Id = product.product_Id
                    WHERE added.customer_ID=%s;""")
        cur.execute(query2,(customer_id,))
        print("(product ID, product name, price, manufacturing date, expiry date)")
        cart=cur.fetchall()
        for i in cart:
            print(i)

        # TO ADD IN CART

        print()
        print("Do you want to add products in your cart?")
        choice=input(("Enter Y/N:"))
        if choice=="y":
            print()
            print("Following is the list of products we have:")
            print()

            query6=("""select product_ID,product_name, product_price, product_manufacture,product_expiry from product;""")
            cur.execute(query6)
            products=cur.fetchall()
            print("(product_ID,product_name, product_price, product_manufacture,product_expiry)")
            for i in products:
                print(i)

            print()
            new_cart_product=input(("Enter the product_ID of the product you want to add to your cart:"))
            query7=("""start transaction;
                        insert into added(admin_ID,customer_ID,product_ID) values (1,%s,%s);
                        update cart_product set cart_size=cart_size+1 where customer_ID=%s;
                        update product set product_availability=product_availability-1;
                        commit;""")
            cur.execute(query7, (customer_id, new_cart_product,customer_id,))

            print("Sign in again to get your updated cart!")
        
        elif choice=="n":
            checkout=input("Do you want to proceed to checkout? (y/n):")
            
            if checkout=="y":
                print()
                print()
                print("Your final bill details are as follows:")
        # query3=("""select product_ID,product_name,product_price, product_manufacture,product_expiry
        #              from product where customer_ID=%s;""")
        

                query3=("""SELECT DISTINCT product.product_Id, product.product_name, product.product_price,added.customer_ID
                        FROM added
                        INNER JOIN product ON added.product_Id = product.product_Id
                        WHERE added.customer_ID=%s;""")
                cur.execute(query3,(customer_id,))
                final=cur.fetchall()
                print()
                print("(product_ID, Product name, price, manufacturing date, expiry date)")
                for i in final:
                    print(i)


                query4=("""select product_price from added
                        INNER JOIN product ON added.product_Id = product.product_Id
                        WHERE added.customer_ID=%s;""")
        
        
        
        
                cur.execute(query4, (customer_id,))
                final_bill=cur.fetchall()
                bill_sum=0
                for i in final_bill:
                    bill_sum+=float(i[0])
                print()
                print("Your total is off:",bill_sum)


                print("You get a discount of:")
                query5=("""select payment_discount from payment_dicount where payment_ID=%s;""")
                cur.execute(query5,(customer_id,))
                discount=cur.fetchone()[0]
                print(discount)

                print("Your final bill is off:")
                print(bill_sum-int(discount))
        


                print("Your payment transaction was a success!")
                print()

                print("Your tracking ID and designated delivery partner is:")
                query6=("""select * from tracking_order where tracking_ID=%s;""")
                cur.execute(query6,(customer_id,))
                dispatch_info=cur.fetchall()
                print("(Tracking_ID, delivery partner name)")
                print(dispatch_info)
                print()

                print("Thank you for choosing us! ")
                print()

            else:
                print("Thank you!")









        # CLI HAS TO RUN THE PROGRAM AGAIN TO SHOW UPDATED RESULTS
        # print()
        # print("Your final bill details are as follows:")
        # # query3=("""select product_ID,product_name,product_price, product_manufacture,product_expiry
        # #              from product where customer_ID=%s;""")
        

        # query3=("""SELECT DISTINCT product.product_Id, product.product_name, product.product_price,added.customer_ID
        #             FROM added
        #             INNER JOIN product ON added.product_Id = product.product_Id
        #             WHERE added.customer_ID=%s;""")
        # cur.execute(query3,(customer_id,))
        # final=cur.fetchall()
        # print()
        # print("(product_ID, Product name, price, manufacturing date, expiry date)")
        # for i in final:
        #     print(i)


        # query4=("""select product_price from added
        #             INNER JOIN product ON added.product_Id = product.product_Id
        #             WHERE added.customer_ID=%s;""")
        
        
        
        
        # cur.execute(query4, (customer_id,))
        # final_bill=cur.fetchall()
        # bill_sum=0
        # for i in final_bill:
        #     bill_sum+=float(i[0])
        # print()
        # print("Your total is off:",bill_sum)


        # print("You get a discount of:")
        # query5=("""select payment_discount from payment_dicount where payment_ID=%s;""")
        # cur.execute(query5,(customer_id,))
        # discount=cur.fetchone()[0]
        # print(discount)

        # print("Your final bill is off:")
        # print(bill_sum-int(discount))
        


        # print("Your payment transaction was a success!")
        # print()

        # print("Your tracking ID and designated delivery partner is:")
        # query6=("""select * from tracking_order where tracking_ID=%s;""")
        # cur.execute(query6,(customer_id,))
        # dispatch_info=cur.fetchall()
        # print("(Tracking_ID, delivery partner name)")
        # print(dispatch_info)
        # print()

        # print("Thank you for choosing us! ")
        # print()


    
    elif x==2:
        print("THANK YOU FOR JOINING US!")
        print("We'll take a few of your details and get you registered right away")
        print()

        new_f_name=input(("Enter your first name:"))
        new_l_name=input(("Enter your last name:"))
        new_dob=input("Enter you dob in (1996-01-13) format, () included:")
        new_add=input(("Enter address:"))
        new_num=input(("Enter phone number:"))

        dbquery1=("""START TRANSACTION;
                    INSERT INTO customer (f_name, l_name, dob) VALUES (%s, %s, %s);
                    SET @customer_id = LAST_INSERT_ID();
                    INSERT INTO address (customer_ID, address) VALUES (@customer_id, %s);
                    INSERT INTO phone_number (customer_ID, phone_number) VALUES (@customer_id, %s);
                    COMMIT;""")
        
        cur.execute(dbquery1, (new_f_name, new_l_name, new_dob,new_add,new_num) )
        print("(In this process we have executed a db transaction of adding a new customer that makes a new customer row in all related tables)")
        print()
        print("YOU HAVE BEEN REGISTERED! lOG IN AS REGISTSERED CUSTOMER")
        print()

    
    elif x==3:
        print("Welcom to Healthfirst!")
        print("We will take a few details and get your company registered as our new supplier!")
        print()
        
        new_sup_name=input(("Enter your company's name:"))
        new_sup_address=input(("Enter your company's address:"))

        dbquery2=("""start transaction;
                    insert into supplier(supplier_name) values(%s);
                    set @supplier_ID=LAST_INSERT_ID();
                    insert into supplier_address(supplier_ID,supplier_address) values(@supplier_ID,%s);
                    commit;""")
        cur.execute(dbquery2, (new_sup_name, new_sup_address,))
        print()

        print("(In this process we have executed a db transaction of adding a new supplier that makes a new supplier row in all related tables)")
        print()
        print("YOU HAVE BEEN REGISTERED! lOG IN AS REGISTSERED SUPPLIER")
        print()


    elif x==4:
        print("Welcome to Healthfirst!")
        user=input(("Enter username:"))
        pass1=input(("Enter your password:"))

        sup_id=input(("Enter your supplier_ID:"))
        new_prod_name=input(("Enter the name of your new product:"))
        new_prod_avail=input(("Enter the quantity you will provide us:"))
        new_prod_price=input(("Enter the price of the new poduct:"))
        new_prod_expiry=input(("Enter the expiry date in 1996-01-13 format:"))
        new_prod_manufacture=input(("Enter the manufacturing date in 1996-01-13 format:"))
        new_prod_customer=20
        new_prod_category=input(("Enter the category_ID in which the product belongs:"))

                              

        dbquery3=("""start transaction;
                    insert into product(product_name, product_availability,product_price, product_expiry, 
                    product_manufacture,customer_ID, category_ID) 
                    values(%s,%s,%s,%s,%s,%s,%s);
                    set @product_ID=LAST_INSERT_ID();
                    insert into manufactures values(@product_ID,%s);
                    commit;""")
        cur.execute(dbquery3, (new_prod_name, new_prod_avail, new_prod_price,new_prod_expiry,new_prod_manufacture,new_prod_customer,new_prod_category,sup_id))

        print("(In this process we have executed a db transaction of adding a new product that makes a new product row in all related tables)")
        print()
        print("YOUR NEW PRODUCT HAS BEEN ADDED!")
        print()

    elif x==5:
        print("Welcome! We'll take some details and update the price right away!")
        print()
        user1=input(("Enter your username:"))
        pass2=input(("Enter your password:"))

        sup=input(("Enter your supplier_ID:"))
        prod_id=input("Enter the product_ID:")
        updated_price=float(input("Enter the updated price of your product:"))

        dbquery4=("""start transaction;
                    UPDATE product
                    JOIN manufactures ON product.product_ID = manufactures.product_ID
                    SET product.product_price = %s
                    WHERE manufactures.supplier_ID = %s;
                    commit;""")
        cur.execute(dbquery4,(updated_price, sup,))
        print()

        print("The price of your product has been updated!")
        print("In this process we have used dn transaction to make the necessary changes in all related tables")
        print()

        print("Thank you for using Healthfirst!")


      
    


mycon.close()
