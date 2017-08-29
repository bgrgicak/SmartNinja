import hmac
password = "4441f63125284a43de6e113a7e39bd35"
while True:
    user_input = raw_input("Password: ")
    my_hash = hmac.new(user_input).hexdigest()
    if my_hash == password:
        print "Tocno"
        break