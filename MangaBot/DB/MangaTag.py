from peewee import *

class MangaTag(Model):
    id = IntegerField()
    tag_id = IntegerField()
    manga_id = IntegerField()

    class Meta:
        table_name = 'tag_manga'
        database = MySQLDatabase("manga",host="localhost",user="manga",password="manga",charset='utf8mb4',use_unicode=True,thread_safe=True)
