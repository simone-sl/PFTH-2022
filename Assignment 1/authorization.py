def welcome_user():
    while True:
        name = input('Welcome, what is your name?')
        password = input('Welcome, ' + name + ', please enter the password.')
        if password == 'calico':
            print('That is the correct password, welcome ' + name)
            break
        elif password != 'calico':
         print('That is not the correct password, please try again.')
        continue
welcome_user()