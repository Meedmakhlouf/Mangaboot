from peewee import *

class Author(Model):
    id = IntegerField()
    fullname = CharField(max_length=255)
    about = CharField(max_length=255)
    image = CharField(max_length=255)
    link = CharField(max_length=255)
    class Meta:
        table_name = 'authors'
        database = MySQLDatabase("manga",host="localhost",user="manga",password="manga",charset='utf8mb4',use_unicode=True,thread_safe=True)
