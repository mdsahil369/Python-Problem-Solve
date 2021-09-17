import mysql.connector as connector

class DBHelper:
    def __init__(self):
        self.con=connector.connect(host="localhost",
                                    user="root",
                                    password="",
                                    database="school")
        query = 'create table if not exists user(userId int primary key,userName varchar(200), phone varchar(12))'
        cur = self.con.cursor()
        cur.execute(query)
        print("Created")
    
    #Insert
    def insert_user(self,userid,username,phone):
        query ="insert into user(userId,userName,phone)values({},'{}','{}')".format(userid,username,phone)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user data inserted")

    #Fech All
    def fetch_all(self):
        query="select * from user"
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("UserId : ",row[0])
            print("User Name : ",row[1])
            print("Phone : ",row[2])
            print()
            print()

    #Fech One
    def fetch_one(self,id):
        query="select * from user where userId = {}".format(id)
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print(row)

    #Delete user
    def delete_user(self, userId):
        query="delete from user where userId = {}".format(userId)
        print(query)
        cur= self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('deleted')
    
    #Update
    def update_user(self,userId,newName,newPhone):
        query="update user set userName='{}',phone='{}' where userId={}".format(newName,newPhone,userId)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")



    
helper = DBHelper()
for n in range(1,11):
    helper.insert_user(n,f"Sahil{n}",f"0199{n}")
# # helper.fetch_all()
# # helper.fetch_one(1463)
# # helper.delete_user(1463)
# helper.update_user(1462,'Sahil','0199')
# helper.fetch_all()



