from string import ascii_letters, digits
from random import choices
import pymysql


def make_activation_code():
    """
    ascii_letters = 'abcdefghijklmnopqrstuvwxyz' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    digits = '0123456789',
    'k' is the length for code
    """
    code = ''.join(choices(ascii_letters+digits, k=15))
    return code


# all codes
result_list = [make_activation_code() for i in range(200)]

db = pymysql.connect('localhost', 'root', '123456', 'TestDB')
cursor = db.cursor()

# create table
cursor.execute("CREATE TABLE Q_002("
               "id SMALLINT ,"
               "code VARCHAR(100),"
               "PRIMARY KEY (id))"
               )
for i in range(200):
    cursor.execute("INSERT INTO Q_002 "
                   "VALUES({0}, '{1}')".format(i, result_list[i]))
db.commit()
db.close()
