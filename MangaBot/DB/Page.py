from peewee import *

class Page(Model):
    id = IntegerField()
    image = CharField(max_length=255)
    page_number = DoubleField()
    chapter_id = IntegerField()
    class Meta:
        table_name = 'pages'
        database = MySQLDatabase("manga",host="localhost",user="manga",password="manga",charset='utf8mb4',use_unicode=True,thread_safe=True)
