import redis

#connect to redis database
r = redis.Redis(
  host='example.com',
  port=13475,
  username='####',
  password='####')

# choice login or register
while True:
    print("1. Login \n2. Register")
    choice = input("Enter your choice (1 for Login, 2 for Register):  ")

    if choice == "1":
        username = input("Enter username:  ")
        password = input("Enter password:  ")
        if r.exists(username):
            if r.get(username).decode("utf-8") == password:
                print("Login successful")
                r.expire(username, 86400)
                break
            else:
                print("Wrong username or password")
        else:
            print("Username not found")
    elif choice == "2":
        username = input("Enter username:  ")
        password = input("Enter password:  ")
        #Delete User After 1day
        r.expire(username, 86400)
        r.set(username, password)
        print("Registration successful")
        
        break
    else:
        print("Please enter a valid choice")
        r.expire(username, 86400)