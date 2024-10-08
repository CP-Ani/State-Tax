### S14_PyMT_StarterFile.py  v1b
#  K.Schmitz (c) 2022
#  Starter File for CIS2010 Session 14, Structured Query Language
##################Initialization information, do not modify ################
from cis2010utils import StartHere, EndHere 
from colorama import Fore
import pandas as pd
import sqlite3
############################################################################
# Open up the database  ########## Do not modify these instructions#########
db_name =  "irs18.db"
db_conn = sqlite3.connect(db_name)
sqltxt = "SELECT COUNT(zipcode) FROM irsz" ; zz = pd.read_sql(sqltxt, db_conn) ; print("\nnumber of zipcodes\n", zz)
sqltxt = "pragma table_info('irsz')" ; t1 = pd.read_sql(sqltxt, db_conn) ; print("irsz table\n", t1)
sqltxt = "pragma table_info('zco')" ; t2 = pd.read_sql(sqltxt, db_conn) ; print("zco table\n", t2)
############################################################################
#
# Task 2a
StartHere( "Chike Ani", "S14", "Workshop")
#
# Task w2b
sqlw2b = """
SELECT state, zipcode, n1
FROM irsz
"""
try :
    w2b = pd.read_sql(sqlw2b, db_conn); print( "w2b contains\n", w2b)
except :
    if len(sqlw2b.lstrip()) :
        print(Fore.RED + "\nYour SQL statement has an error that must be fixed" + Fore.BLUE )
        print( sqlw2b )
        print(Fore.BLACK + "Start by checking the spelling of each field in the list" )
        print("Also consider spelling of your table name, and SQL statements\n" )

# Task w2c
sqlw2c = """
SELECT state, zipcode, n1, n2, numdep, a00100*1000, schf
FROM irsz
"""
try :
    w2c = pd.read_sql(sqlw2c, db_conn); print( "w2c contains\n", w2c)
except :
    if len(sqlw2c.lstrip()) :
        print(Fore.RED + "\nYour SQL statement has an error that must be fixed" + Fore.BLUE )
        print( sqlw2c )
        print(Fore.BLACK + "Start by checking the spelling of each field in the list" )
        print("Also consider spelling of your table name, and SQL statements\n" )

# Task w2d
sqlw2d = """
SELECT state, zipcode, n1, n2, numdep, a00100*1000,
schf, a06500*1000, a19700*1000
FROM irsz
"""
try :
    w2d = pd.read_sql(sqlw2d, db_conn); print( "w2d contains\n", w2d)
except :
    if len(sqlw2d.lstrip()) :
        print(Fore.RED + "\nYour SQL statement has an error that must be fixed" + Fore.BLUE )
        print( sqlw2d )
        print(Fore.BLACK + "Start by checking the spelling of each field in the list" )
        print("Also consider spelling of your table name, and SQL statements\n" )

#Task w3a
w2d.to_csv( 'x2d.csv', sep=',')

# Workshop END
#
###########################################################
# Collaboration Challenge
#
# S14ccq Q4
StartHere( "Chike Ani", "S14", "CC")

# S14ccq Q5
sqlcc5 = """
SELECT state, zipcode, n1, n2, numdep, a00100*1000,
schf, a06500*1000, a19700*1000
FROM irsz
WHERE zipcode > 1000 and zipcode < 99999
"""
try :
    cc5 = pd.read_sql(sqlcc5, db_conn); print( "cc5 contains\n", cc5)
except :
    if len(sqlcc5.lstrip()) :
        print(Fore.RED + "\nYour SQL statement has an error that must be fixed" + Fore.BLUE )
        print( sqlcc5 )
        print(Fore.BLACK + "Start by checking the spelling of each field in the list" )
        print("Also consider spelling of your table name, and SQL statements\n" )


# S14ccq Q6
sqlcc6 = """
SELECT state, zipcode, n1, n2, numdep, a00100*1000,
schf, a06500*1000, a19700*1000
FROM irsz
WHERE zipcode BETWEEN 1000 AND 99999
AND state = 'GA'


"""
try :
    cc6 = pd.read_sql(sqlcc6, db_conn); print( "cc6 contains\n", cc6)
except :
    if len(sqlcc6.lstrip()) :
        print(Fore.RED + "\nYour SQL statement has an error that must be fixed" + Fore.BLUE )
        print( sqlcc6 )
        print(Fore.BLACK + "Start by checking the spelling of each field in the list" )
        print("Also consider spelling of your table name, and SQL statements\n" )

# S14ccq Q7
sqlcc7 = """
SELECT state, elderly, zipcode, n1, n2, numdep, a00100*1000,
schf, a06500*1000, a19700*1000
FROM irsz
WHERE zipcode BETWEEN 1000 AND 99999
AND state = 'GA'
"""
try :
    cc7 = pd.read_sql(sqlcc7, db_conn); print( "cc7 contains\n", cc7)
except :
    if len(sqlcc7.lstrip()) :
        print(Fore.RED + "\nYour SQL statement has an error that must be fixed" + Fore.BLUE )
        print( sqlcc7 )
        print(Fore.BLACK + "Start by checking the spelling of each field in the list" )
        print("Also consider spelling of your table name, and SQL statements\n" )
finally :
    db_conn.close()
    
cc7.to_csv( 'cc7.csv', sep=',')

#Collaboration Challenge: Cleanup, Save and End
EndHere( globals())
#db_conn.close(); exit()
###########################################################