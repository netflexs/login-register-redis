import redis

#connect to redis database
r = redis.Redis(
  host='example.redis.host',
  port=13475,
  username='####',
  password='#####')

# choice login or register
choice = input('Do you want to login or register ? ')

# Make Login And Register Session with user input
if choice == 'Login' or choice == 'login':
    username = input('Enter username : ')
    password = input('Enter password : ')
    if r.exists(username) and r.hget(username, 'password') == password:
        print('Welcome ' + username)
    else:
        print('Username and password are incorrect. Please register')
        choice = 'Register'

if choice == 'Register' or choice == 'register':
    username = input('Enter username : ')
    if r.exists(username):
        print('Username already exists. Please login')
        choice = 'Login'
    else:
        password = input('Enter password : ')
        r.hmset(username, {'password': password})
        print('Registration Successful')

# Delete registered User After 1 Day
r.expire(username, 86400)