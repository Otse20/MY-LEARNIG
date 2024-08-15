
# open_buffet calculator software
payment = 20
Age = float (input ("please enter your age here: "))
if Age <=12:
    print("you dont have to pay")
elif Age >12 and Age <= 16:
    print ("your payment is: ", float(payment- (payment*0.2)) ,"$")
elif Age > 16:
    print("your payment is: ", payment,"$")
    