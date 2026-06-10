import pymysql as p
import getpass
import bcrypt
from datetime import datetime
admin_pwd=b"admin123"
developer_pwd=b"dev123"
dev_hash=bcrypt.hashpw(developer_pwd,bcrypt.gensalt())
admin_hash=bcrypt.hashpw(admin_pwd,bcrypt.gensalt())
user_db={"Admin":admin_hash,"Pranav":dev_hash}
def CreateDB(cur,conn,dbname):
    try:
        cur.execute(f"create database {dbname}")
        conn.commit()
    except Exception:
        pass
def Createtable(cur,conn):
    try:
        tables=['academic','co_curricular','sports_pe','health_wellness','admin_support']
        for t in tables:
            cur.execute(f"create table if not exists {t} (asset_id int primary key,asset_name varchar(50),asset_description varchar(200),conditions varchar(50),mfg_date date,exp_date date,pr_u float,nu int,total_cost float)")
            conn.commit()
    except Exception as e:
        print("Error during table creation:",e)
def CreateUsers(cur,conn):
    try:
        cur.execute(f"create table if not exists users (username varchar(20) primary key, password_hash varchar(255))")
        conn.commit()
    except Exception as e:
        print("Error creating users table:",e)
def add_user(cur,conn):
    while True:
        try:
            new_user=input("Enter new username: ").strip()
            if new_user=="":
                print("Username cannot be empty.")
                continue
            cur.execute(f"select username from users where username='{new_user}'")
            if cur.fetchone():
                print("User already exists.")
                continue
            while True:
                try:
                    new_pass=getpass.getpass("Enter password for new user: ")
                    if new_pass=="":
                        print("Password cannot be empty.")
                        continue
                    confirm_pass=getpass.getpass("Confirm password: ")
                    if new_pass!=confirm_pass:
                        print("Passwords do not match.")
                        continue
                    break
                except Exception:
                    print("Error entering password. Try again.")
            hashed=bcrypt.hashpw(new_pass.encode(),bcrypt.gensalt())
            cur.execute(f"insert into users(username,password_hash) values('{new_user}','{hashed.decode()}')")
            conn.commit()
            print(f"User '{new_user}' added successfully.")
            break
        except Exception as e:
            print("Error adding user:",e)
def view_users(cur):
    try:
        cur.execute("select username from users")
        users=cur.fetchall()
        print("\nRegistered Admin Users:")
        if not users:
            print("No users found.")
        else:
            for u in users:
                print("-",u[0])
    except Exception as e:
        print("Error retrieving users:",e)
def dept():
    departments=['academic','co_curricular','sports_pe','health_wellness','admin_support']
    print("\nSelect Department:")
    for i,d in enumerate(departments,1):
        print(f"{i}. {d}")
    while True:
        ch=input("Enter department number (1-5): ")
        if ch in "12345":
            return departments[int(ch)-1]
        else:
                print("Invalid input. Please choose between 1-5.")
def Mdate():
            while 1:
                date_str=input(f"Enter Manufacturing Date (YYYY-MM-DD): ").strip()
                date_obj=datetime.strptime(date_str,"%Y-%m-%d").date()
                Y=date_obj.year
                if not(Y>=datetime.now().year-100 and Y<=datetime.now().year):
                    print("Invalid Year..")
                    continue
                M=date_obj.month
                if not (1<=M<=12):
                    print("Invalid Month..")
                    continue
                D=date_obj.day
                if M==2:
                    if (Y%4==0 and Y%100!=0) or (Y%400==0):
                        if not(1<=D<=29):
                            print("Invalid day ")
                            continue
                    elif not (1<=D<=28):
                            print("Invalid Day..")
                            continue
                elif M in [4,6,9,11]:
                    if not(1<=D<=30):
                        print("Invalid day!")
                        continue
                else:
                    if not(1<=D<=31):
                        print("Invalid day!")
                        continue
                break
            return date_obj
def Edate():
            while 1:
                date_str=input(f"Enter Expiry Date (YYYY-MM-DD): ").strip()
                date_obj=datetime.strptime(date_str,"%Y-%m-%d").date()
                Y=date_obj.year
                if not(Y>=datetime.now().year and Y<=datetime.now().year+200):
                    print("Invalid Year..")
                    continue
                M=date_obj.month
                if not (1<=M<=12):
                    print("Invalid Month..")
                    continue
                D=date_obj.day
                if M==2:
                    if (Y%4==0 and Y%100!=0) or (Y%400==0):
                        if not(1<=D<=29):
                            print("Invalid day ")
                            continue
                    elif not (1<=D<=28):
                            print("Invalid Day..")
                            continue
                elif M in [4,6,9,11]:
                    if not(1<=D<=30):
                        print("Invalid day!")
                        continue
                else:
                    if not(1<=D<=31):
                        print("Invalid day!")
                        continue
                break
            return date_obj
def Add(cur,conn):
    try:
        print("\n----- ADD ASSET -----")
        table=dept()
        tables=['academic','co_curricular','sports_pe','health_wellness','admin_support']
        asset_id=0
        for i in tables:
            cur.execute(f"select max(asset_id) from {i}")
            result=cur.fetchone()
            if result[0] is not None and result[0]>asset_id:
                asset_id=result[0]
        asset_id+=1
        print(f"\nGenerated Asset ID: {asset_id}")
        while True:
            asset_name=input("Enter Asset Name: ").strip()
            if not asset_name:
                print("Asset Name cannot be empty.")
                continue
            if len(asset_name)>50:
                print("Asset Name too long. Max 50 characters.")
                continue
            invalid=False
            for word in asset_name.split():
                if not word.isalpha():
                    invalid=True
                    break
            if invalid:
                print("Asset Name must contain only alphabetic characters and spaces.")
                continue
            break
        while True:
            asset_description=input("Enter Asset Description: ").strip().replace("'","''")
            if not asset_description:
                print("Asset Description cannot be empty.")
                continue
            if len(asset_description)>100:
                print("Asset Description too long. Max 100 characters.")
                continue
            invalid=False
            for c in asset_description:
                if not(c.isalnum() or c.isspace() or c in ".,'-"):
                    invalid=True
                    break
            if invalid:
                print("Asset Description contains invalid characters.")
                continue
            break
        while True:
            while True:
                print("\nAsset Condition Options:\n1. New\n2. Used\n3. Needs Repair")
                condition=input("Enter Condition (1/2/3): ").strip()
                if condition=="1":
                    condition="New"
                    break
                elif condition=="2":
                    condition="Used"
                    break
                elif condition=="3":
                    condition="Needs Repair"
                    break
                else:
                    print("Invalid input. Please enter 1, 2, or 3.")
            if condition in["New","Used","Needs Repair"]:
                break
        while 1:
            mfg_date=Mdate()
            break
        while 1:
            exp_date=Edate()
            break
        while True:
            price_input=input("Enter Price per Unit: ").strip()
            if not price_input.replace('.','',1).isdigit():
                print("Invalid input. Enter a valid number.")
                continue
            pr_u=float(price_input)
            if pr_u<0:
                print("Price per unit cannot be negative.")
                continue
            break
        while True:
            num_input=input("Enter Number of Units: ").strip()
            if not num_input.isdigit():
                print("Invalid input. Enter a valid integer.")
                continue
            nu=int(num_input)
            if nu<0:
                print("Number of units cannot be negative.")
                continue
            break
        total_cost=pr_u*nu
        cur.execute(f"insert into {table}(asset_id,asset_name,asset_description,conditions,mfg_date,exp_date,pr_u,nu,total_cost) values({asset_id},'{asset_name}','{asset_description}','{condition}','{mfg_date}','{exp_date}',{pr_u},{nu},{total_cost})")
        conn.commit()
        print("\nAsset added successfully!")
    except Exception as e:
        print("Error adding asset:",e)
def Update(cur,conn):
    try:
        print("\n----- UPDATE ASSET -----")
        table=dept()
        while True:
            while True:
                asset_id=input("Enter Asset ID to update: ").strip()
                if not asset_id.isdigit():
                    print("Invalid input. Asset ID must be an integer.")
                    continue
                asset_id=int(asset_id)
                if len(str(asset_id))==0:
                    print("Asset ID cannot be empty.")
                    continue
                if len(str(asset_id))>4:
                    print("Asset ID too long. Max 4 digits.")
                    continue
                break
            cur.execute(f"select * from {table} where asset_id={asset_id}")
            record=cur.fetchone()
            if not record:
                print("Asset not found with given ID.")
                continue
            break
        print("\nExisting Record Details:")
        print(record)
        print("\nSelect field to update:\n1. Asset Name\n2. Asset Description\n3. Condition\n4. Manufacturing Date\n5. Expiry Date\n6. Price per Unit\n7. Number of Units")
        while True:
            choice=input("Enter your choice (1-7): ").strip()
            if not choice.isdigit() or int(choice)<1 or int(choice)>7:
                print("Invalid choice.")
                continue
            choice=int(choice)
            break
        if choice==1:
            while True:
                new_val=input("Enter new Asset Name: ").strip()
                if len(new_val)==0:
                    print("Asset Name cannot be empty.")
                    continue
                if len(new_val)>50:
                    print("Asset Name too long. Max 50 characters.")
                    continue
                invalid=False
                for word in new_val.split():
                    if not word.isalpha():
                        invalid=True
                        break
                if invalid:
                    print("Asset Name must contain only alphabetic characters and spaces.")
                    continue
                break
            cur.execute(f"update {table} set asset_name='{new_val}' where asset_id={asset_id}")
        elif choice==2:
            while True:
                new_val=input("Enter new Asset Description: ").strip()
                if len(new_val)==0:
                    print("Asset Description cannot be empty.")
                    continue
                if len(new_val)>100:
                    print("Asset Description too long. Max 100 characters.")
                    continue
                invalid=False
                for c in new_val:
                    if not(c.isalnum()or c.isspace()or c in ".,'-"):
                        invalid=True
                        break
                if invalid:
                    print("Asset Description contains invalid characters.")
                    continue
                break
            cur.execute(f"update {table} set asset_description='{new_val}' where asset_id={asset_id}")
        elif choice==3:
            while True:
                while True:
                    print("\nAsset Conditions Options:\n1. New\n2. Used\n3. Needs Repair")
                    new_val=input("Enter new Condition (1/2/3): ").strip()
                    if new_val=="1":
                        new_val="New"
                        break
                    elif new_val=="2":
                        new_val="Used"
                        break
                    elif new_val=="3":
                        new_val="Needs Repair"
                        break
                    else:
                        print("Invalid condition. Please enter 1, 2, or 3.")
                if new_val in["New","Used","Needs Repair"]:
                    break
            cur.execute(f"update {table} set conditions='{new_val}' where asset_id={asset_id}")
        elif choice==4:
            while 1:
                ch=input("Do you wish to update the manufacturing date? (Y/N): ").upper()
                if ch not in ["Y","N"]:
                    print("Invalid input! Please re-enter.")
                    continue
                if ch=="N":
                    new_val=None
                else:
                    new_val=Mdate()
                break
            if new_val is None:
                new_val=None
            cur.execute(f"update {table} set mfg_date='{new_val}' where asset_id={asset_id}")
        elif choice==5:
            while 1:
                ch=input("Do you wish to update the expiry date? (Y/N): ").upper()
                if ch not in ["Y","N"]:
                    print("Invalid input! Please re-enter.")
                    continue
                if ch=="N":
                    new_val=None
                else:
                    new_val=Edate()
                break
            if new_val is None:
                new_val=None
            cur.execute(f"update {table} set exp_date='{new_val}' where asset_id={asset_id}")
        elif choice==6:
            while True:
                price=input("Enter new Price per Unit: ").strip()
                if not price.replace('.','',1).isdigit():
                    print("Invalid input. Enter a valid number.")
                    continue
                pr_u=float(price)
                if pr_u<0:
                    print("Invalid price. Try again.")
                    continue
                cur.execute(f"update {table} set pr_u={pr_u} where asset_id={asset_id}")
                break
        elif choice==7:
            while True:
                num=input("Enter new Number of Units: ").strip()
                if not num.isdigit():
                    print("Invalid input. Enter a valid integer.")
                    continue
                nu=int(num)
                if nu<0:
                    print("Invalid number. Try again.")
                    continue
                cur.execute(f"update {table} set nu={nu} where asset_id={asset_id}")
                break
        cur.execute(f"update {table} set total_cost=pr_u*nu where asset_id={asset_id}")
        conn.commit()
        print("\nAsset updated successfully!")
    except Exception as e:
        print("Error updating asset:",e)
def Delete(cur,conn):
    try:
        print("\n----- DELETE ASSET -----")
        table=dept()
        while True:
            while True:
                asset_id=input("Enter Asset ID to delete: ").strip()
                if not asset_id.isdigit():
                    print("Invalid input. Asset ID must be an integer.")
                    continue
                asset_id=int(asset_id)
                if asset_id<0:
                    print("Asset ID cannot be negative.")
                    continue
                break
            cur.execute(f"select * from {table} where asset_id={asset_id}")
            record=cur.fetchone()
            if not record:
                print("No asset found with that ID.")
                continue
            print(record)
            break
        while True:
            confirm=input(f"Are you sure you want to delete Asset ID {asset_id}? (Y/N): ").strip().upper()
            if confirm not in ["Y","N"]:
                print("Invalid input. Enter Y or N.")
                continue
            if confirm=="Y":
                cur.execute(f"delete from {table} where asset_id={asset_id}")
                conn.commit();print(f"Asset ID {asset_id} deleted successfully.")
                break
            else:
                print("Deletion cancelled.")
                break
    except Exception as e:
        print("Error deleting asset:",e)
def Display(cur):
    try:
        print("\n----- DISPLAY ASSETS -----")
        table=dept()
        cur.execute(f"select asset_id,asset_name,conditions,mfg_date,exp_date,pr_u,nu,total_cost from {table}")
        rows=cur.fetchall()
        if not rows:
            print("\nNo assets found in this department.")
        else:
            print("\n===================================================================================================================================================================")
            print(f"{'ID':<6} | {'NAME':<50} | {'CONDITION':<18} | {'MFG DATE':<10} | {'EXP DATE':<10} | {'PRICE/U':<25} | {'UNITS':<25} | {'TOTAL COST':<25}")
            print("=====================================================================================================================================================================")
            for row in rows:
                print(f"{row[0]:<6} | {row[1]:<50} | {row[2]:<18} | {str(row[3]):<10} | {str(row[4]):<10} | {row[5]:<25.2f} | {row[6]:<25} | {row[7]:<25.2f}")
            print("=====================================================================================================================================================================")
            while 1:
                A=input("Do you wish to view asset description (Y/N): ").upper()
                if A not in ["Y","N"]:
                    print("Invalid input! Please re-enter.")
                    continue
                elif A=="Y":
                    cur.execute(f"select asset_description from {table}")
                    row=cur.fetchall()
                    for i in row:
                        print("\nAsset Description:")
                        print(i[0])
                else:
                    break
    except Exception as e:
        print("Error displaying assets:",e)
def admin_menu(cur,conn):
    while True:
        try:
            print("Welcome to the Admin Menu, Aaditya!")
            print("Please select an option from the menu below to proceed further:")
            print("\n==================== ADMIN MENU ====================")
            print("1. Add Asset\n2. Update Asset\n3. Delete Asset\n4. Display Assets\n5. Add User\n6. View Users\n7. Logout\n8. Exit All")
            choice=int(input("Enter your choice (1-8): "))
            if choice==1:
                Add(cur,conn)
            elif choice==2:
                Update(cur,conn)
            elif choice==3:
                Delete(cur,conn)
            elif choice==4:
                Display(cur)
            elif choice==5:
                add_user(cur,conn)
            elif choice==6:
                view_users(cur)
            elif choice==7:
                print("\nLogging out from admin account...")
                login_menu(cur,conn)
            elif choice==8:
                print("\nExiting program completely...")
                conn.close()
                exit()
            else:
                print("Invalid choice. Please enter between 1-8.")
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt detected. Returning to Admin Menu...")
            continue
        except Exception:
            print("Invalid input. Please try again.")
def developer_menu(cur,conn):
    while True:
        try:
            print("Welcome to the Developer Menu, Developer Pranav!")
            print("Please select an option from the menu below to proceed further:")
            print("\n==================== DEVELOPER MENU ====================")
            print("1. Add Asset\n2. Update Asset\n3. Delete Asset\n4. Display Assets\n5. View Users\n6. Logout\n7. Exit All")
            choice=int(input("Enter your choice (1-7): "))
            if choice==1:
                Add(cur,conn)
            elif choice==2:
                Update(cur,conn)
            elif choice==3:
                Delete(cur,conn)
            elif choice==4:
                Display(cur)
            elif choice==5:
                view_users(cur)
            elif choice==6:
                print("\nLogging out from developer account...")
                login_menu(cur,conn)
            elif choice==7:
                print("\nExiting program completely...")
                conn.close()
                exit()
            else:
                print("Invalid choice. Please enter between 1-7.")
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt detected. Returning to Developer Menu...")
            continue
        except Exception:
            print("Invalid input. Please try again.")
def user_menu(cur,conn,user_name):
    while True:
        try:
            print(f"Welcome, {user_name}!")
            print("Please select an option from the menu below to proceed further:")
            print("\n==================== USER MENU ====================")
            print("1. Add Asset\n2. Update Asset\n3. Delete Asset\n4. Display Assets\n5. Exit")
            print("===================================================")
            print("Disclaimer: As a user, you have limited access rights. You can add,\nupdate, delete, and display assets, but you cannot manage users or \naccess admin/developer functionalities.")
            choice=int(input("Enter your choice (1-5): "))
            if choice==1:
                Add(cur,conn)
            elif choice==2:
                Update(cur,conn)
            elif choice==3:
                Delete(cur,conn)
            elif choice==4:
                Display(cur)
            elif choice==5:
                print("\nExiting user operations...")
                login_menu(cur,conn)
            else:
                print("Invalid choice. Please enter between 1-5.")
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt detected. Returning to User Menu...")
            continue
        except Exception:
            print("Invalid input. Please try again.")
def login_menu(cur,conn):
    while True:
        try:
            print("Welcome to the Login Menu!")
            print("Please select an option from the menu below to proceed further:")
            print("\n==================== LOGIN MENU ====================")
            print("1. Admin Login\n2. User (Auto-Login)\n3. Developer Login\n4. Exit")
            ch=int(input("Enter your choice (1-4): "))
            if ch==1:
                username=input("Enter admin username: ").strip()
                password=getpass.getpass("Enter admin password: ")
                if username=="Admin" and bcrypt.checkpw(password.encode(),user_db["Admin"]):
                    print("\nAdmin login successful!")
                    admin_menu(cur,conn)
                elif username=="Admin" and not(bcrypt.checkpw(password.encode(),user_db["Admin"])):
                    print("Incorrect Password. Please try again.")
                else:
                    print("Invalid credentials. Please try again.")
            elif ch==2:
                print("\nAuto-login as user successful!")
                while 1:
                    user_name = input("Please enter your name: ").strip()
                    if user_name=="":
                        print("Name cannot be empty. Please enter a valid name.")
                        continue
                    invalid=False
                    for word in user_name.split():
                        if not word.isalnum() and not word.isspace():
                            invalid=True
                            break
                    if invalid:
                        print("Name must contain valid characters and no spaces. Please try again.")
                        print("Note: Special characters, numbers and spaces are not allowed.")
                        continue
                    break
                if user_name=="Aaditya":
                    print("Are you admin?")
                    while 1:
                        ch=input("Enter Y for Yes and N for No: ").upper()
                        if ch=="Y":
                            pwd=getpass.getpass("Enter admin password: ")
                            if bcrypt.checkpw(pwd.encode(),user_db["Admin"]):
                                print("\nAdmin login successful!")
                                admin_menu(cur,conn)
                            else:
                                print("Authentication failed. Returning to login menu...")
                                login_menu(cur,conn)
                        elif ch=="N":
                            break
                        else:
                            print("Invalid input! Please re-enter.")
                            continue
                elif user_name=="Pranav":
                    print("Are you developer?")
                    while 1:
                        ch=input("Enter Y for Yes and N for No: ").upper()
                        if ch=="Y":
                            pwd=getpass.getpass("Enter developer password: ")
                            if bcrypt.checkpw(pwd.encode(),user_db["Pranav"]):
                                print("\nDeveloper login successful!")
                                developer_menu(cur,conn)
                            else:
                                print("Authentication failed. Returning to login menu...")
                                login_menu(cur,conn)
                        elif ch=="N":
                            break
                        else:
                            print("Invalid input! Please re-enter.")
                            continue
                else:
                    ch1=input("Do you wish to continue as a normal user? (Y/N): ").upper()
                    if ch1=="Y":
                        user_menu(cur,conn,user_name)
                    elif ch1=="N":
                        print("Exiting program...")
                        conn.close()
                        exit()
                    else:
                        print("Invalid input! Please re-enter.")
                        continue
            elif ch==3:
                username=input("Enter developer username: ").strip()
                password=getpass.getpass("Enter developer password: ")
                if username=="Pranav" and bcrypt.checkpw(password.encode(),user_db["Pranav"]):
                    print("\nDeveloper login successful!")
                    developer_menu(cur,conn)
                elif username=="Pranav" and not(bcrypt.checkpw(password.encode(),user_db["Pranav"])):
                    print("Incorrect Password. Please try again.")
                else:
                    print("Invalid credentials. Please try again.")
            elif ch==4:
                print("\nExiting program...")
                conn.close()
                exit()
            else:
                print("Invalid choice. Please enter between 1-3.")
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt detected. Returning to Login Menu...")
            continue
        except Exception:
            print("Invalid input. Try again.")
def main():
    while True:
        try:
            print("\n===================================================")
            print("Welcome to the Asset Management System (MySQL 8.0)")
            print("===================================================")
            P=getpass.getpass("Enter MySQL Root Password: ")
            temp_conn=p.connect(host="localhost",user="root",password=P)
            temp_cur=temp_conn.cursor()
            CreateDB(temp_cur,temp_conn,"asset_management")
            temp_cur.close()
            temp_conn.close()
            conn=p.connect(host="localhost",user="root",password=P,database="asset_management")
            cur=conn.cursor()
            Createtable(cur,conn)
            CreateUsers(cur,conn)
            print("\n==================== EXISTING USERS ====================")
            view_users(cur)
            print("========================================================")
            login_menu(cur,conn)
            break
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt detected. Restarting main program...")
            continue
        except Exception as e:
            print("Database connection failed:",e)
            print("Try again.\n")
main()
