from django.db import models

# Create your models here.


# class Member(models.Model):
#     firstname = models.CharField(max_length=50)
#     lastname = models.CharField(max_length=50)
#     address = models.CharField(max_length=50)

#     def __str__(self):
#         return self.firstname + " " + self.lastname

#connect to sqlite in python?
# $ ls *.db
# ls: *.db: No such file or directory

# $ python test.py

# $ ls *.db
# mydatabase.db

# $ sqlite3 mydatabase.db 
# SQLite version 3.7.7 2011-06-25 16:35:41
# Enter ".help" for instructions
# Enter SQL statements terminated with a ";"
# sqlite&gt; select * from sqlite_master;
# table|albums|albums|2|CREATE TABLE albums
#              (title text, artist text, release_date text, 
#               publisher text, media_type text)
# sqlite&gt;
