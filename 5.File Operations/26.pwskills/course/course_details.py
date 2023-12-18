# hmara objective h ki ham course vale file ke andr se payment vale ko access kar paye
# and vise versa

# package means folder(directiory) in general
# module means file where we perform many operations



import os ,sys
from os.path import dirname,join,abspath

sys.path.insert(0,abspath(join(dirname(__file__),'..')))


#from payment import payment_details

def course():
    print('this is my course details')


#payment_details.payment() 

'''
# common error dekhne ko milega (NameError: name 'payment_details' is not defined)

# isko ham kaise thik krenge every condition me 

# ham module import karte h 
'''