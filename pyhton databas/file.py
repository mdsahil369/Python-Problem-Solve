from MySQL_cmd import DBHelper

def main():
    db=DBHelper()
    while True:
        print("*******WELCOME********")
        print("PRESS 1 to insert new user")
        print("PRESS 2 to display all user")
        print("PRESS 3 to delete user")
        print("PRESS 4 to update user")
        print("PRESS 5 to exit program")
        print()
        try:
            choice=int(input())
            if(choice==1):
                #insert user
                pass
            elif choice==2:
                #fetch all
                db.fetch_all()
                pass
            elif choice==3:
                pass
            elif choice==4:
                pass
            elif choice==5:
                break
            else:
                print("INvalid input ! Try again")
        except Exception as e:
            print(e)
            print("Envalid Details ! Try again")

if __name__=="__main__":
    main()