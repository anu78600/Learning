import os ,sys
from os.path import dirname,join,abspath

sys.path.insert(0,abspath(join(dirname(__file__),'..')))

from course import course_details

def payment():
    print('this is my payment details')


course_details.course()


# yha pr jo error aa rha h , vo circular import se aa rha h

# ham yha ke file ko vha , ar vha ke file yha kar rhe h 

# ye error na aaye iss liye , yek time pr yek ko hi import karte h
