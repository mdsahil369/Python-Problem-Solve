# blance_amount = 1000
# admin = 'akter'
user_name_and_password = {'sahil':'1','sayem':'2','sazia':'3','muskan':'4','niloy':'5'}
# user_name = ['sahil','sayem','sazia','muskan','niloy']
# user_password = ['1','2','3','4','5']
bkash_number = [1922035654,1922035655,1922035656,1922035657,1922035658]
user_bkash_blance = [200,100,50,60,30]


user_name_input = input('User Name : ')
user_password_input = input('User Password : ')

for name,password in user_name_and_password.items():
    if user_name_input == name and user_password_input == password:
        user_name_index_list = list(user_name_and_password.keys())
        user_name_index_number = user_name_index_list.index(name)
        print(f'Your blance is {user_bkash_blance[user_name_index_number]}')
        print(f'1. Send Money')
        print(f'2. Add Money')
        user_work_input = int(input('what you want : '))
        if user_work_input == 1:
            send_friend_number = int(input('Where you want to send money type this number : '))
            send_money_amound = int(input('Which amound of money you send : '))
            friend_bkash_number_index = bkash_number.index(send_friend_number)
            user_bkash_blance[user_name_index_number] -= send_money_amound
            user_bkash_blance[friend_bkash_number_index] += send_money_amound
            print(f'your friend name is {user_name_index_list[friend_bkash_number_index]} and send money amound is {send_money_amound}, prossce suscesful')
            print(f'now your blance is {user_bkash_blance[user_name_index_number]} ')
            print(f'/////////////////////////////////friend blance is {user_bkash_blance[friend_bkash_number_index]}')
        if user_work_input == 2:
            add_money_password = int(input('Add Money Password :'))
            if add_money_password == 5577:
                print(f'You have added 200 tk in your blance')
                user_bkash_blance[user_name_index_number]+=200
                print(f'Now, Your Blance Is {user_bkash_blance[user_name_index_number]}')
            else:
                print(f'Sorry ! Your Password Is Worng.')
