from peewee import *

class Manga(Model):
    id = IntegerField()
    title = CharField(max_length=255)
    title_en = CharField(max_length=255)
    about = TextField()
    cover = CharField(max_length=255)
    link = CharField(max_length=255)
    year = CharField(max_length=255)
    fixed = BooleanField()
    stopped = BooleanField()
    updatable = BooleanField()
    author_id = IntegerField()
    mag_id = IntegerField()
    updated_at = CharField(max_length=255)
    class Meta:
        table_name = 'mangas'
        database = MySQLDatabase("manga",host="localhost",user="manga",password="manga",charset='utf8mb4',use_unicode=True,thread_safe=True)
