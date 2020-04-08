from peewee import *

class Chapter(Model):
    id = IntegerField()
    edition_number = DoubleField()
    manga_id = IntegerField()
    views = IntegerField()
    class Meta:
        table_name = 'chapters'
        database = MySQLDatabase("manga",host="localhost",user="manga",password="manga",charset='utf8mb4',use_unicode=True,thread_safe=True)
