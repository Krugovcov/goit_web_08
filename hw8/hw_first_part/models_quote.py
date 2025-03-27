from mongoengine import Document, ReferenceField, ListField, StringField, CASCADE


class Author(Document):
    fullname = StringField(max_length=100, required=True, unique=True)
    born_date = StringField(max_length=50)
    born_location = StringField()
    description = StringField()




class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    quote = StringField(required=True)

