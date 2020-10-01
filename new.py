# customers template    
from sys import argv
script, customers_name = argv, "james"
customers_address = input('customers_address: ')
customers_email_address = input('customers_email_address: ')
password1 = input('passsword: ')
if password1.isalnum()== True :
    password2 = input('input password again\npasssword: ')
else:
    print('incorrect  password and password should contain number and alphabeth')
if ( password1 == password2) :
    print("password saved\nwelcome " + customers_name.upper())
    print(f'customers template\ncustomers_name: {customers_name}\ncustomers_address: {customers_address}\ncustomers_email_address: {customers_email_address}')  

else:
    print('incorrect  password and password should contain a number')

   



