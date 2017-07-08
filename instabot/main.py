#fetching own information
from self_info import self_info
#fetching our own data
from get_own_post import get_own_post
#fetching user information
from get_user_info import get_user_info
#fetching user post
from get_users_post import get_users_post


def start_bot():
    while True:
        print '\n'
        print 'Hey! Welcome to instaBot!'
        print 'Here are your menu options:'
        print "a.Get your own details\n"
        print "b.Get details of a user by username\n"
        print "c.Get your own recent post\n"
        print "d.Get the recent post of a user by username\n"

        print "j.Exit"

        choice = raw_input("Enter you choice: ")
        if choice == "a":
            self_info()
        elif choice == "b":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_info(insta_username)
        elif choice == "c":
            get_own_post()
        elif choice == "d":
            insta_username = raw_input("Enter the username of the user: ")
            get_users_post(insta_username)

        elif choice == "j":
            exit()
        else:
            print "wrong choice"

start_bot()
