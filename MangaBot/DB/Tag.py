from peewee import *

class Tag(Model):
    id = IntegerField()
    name = CharField(max_length=255)
    description = CharField(max_length=255)
    class Meta:
        table_name = 'tags'
        database = MySQLDatabase("manga",host="localhost",user="manga",password="manga",charset='utf8mb4',use_unicode=True,thread_safe=True)
