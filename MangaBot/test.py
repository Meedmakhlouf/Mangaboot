from models.Tag import Tag
try:
    tag = Tag.select(Tag.id).where(Tag.name == "أكdsdsشن").get()
except:
    print("Nothing")
