# Lists and dictionaries   create a list of your favorite books, including
# book titles, and authors  Use list slicing to print the first 3 books in the
# lsit. Create a dictionary that representsa basic student database, including
# student names, and student ID's
import pytest

book_list = ['To Kill a Mockingbird','Harper Lee','The Great Gatsby', 
            'F Scott Fitzgerald', 'Pride and Prejudice', 'Jane Austin',
            'Gone with the Wind', 'Margaret Mitchell']
        
print(book_list)
print(book_list[0], book_list[2], book_list[4])
#==============================================================================
print()
#==============================================================================
student_database = { 
    'a':{'student_name':'George Smith',      'student_ID':   45461},
    'b':{ 'student_name':'Alice JOnes',       'student_Id':   45871},
    'c':{ 'student_name':'Henry Black',       'student_ID':   44451},
    'd':{ 'student_name':'Christi McNamara',  'student_id':   456871} }

print(student_database)
#==============================================================================
def test_book_list():
    assert book_list == book_list

def test_student_database():
    expected_dict = {'student_name':'George Smith',      'student_ID':   45461} 
    actual_dic = {'student_name':'George Smith',      'student_ID':   45461}
    assert actual_dic == expected_dict


