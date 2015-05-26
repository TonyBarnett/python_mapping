from mongoengine import connect, Document, StringField, ListField, QuerySet
from pymongo import read_preferences

con = connect('Temp',
              host='10.10.20.37',
              port=27017,
              # alias="reuters_single_class",
              alias="ReutersDataPaul",
              read_preference=read_preferences.ReadPreference.PRIMARY
              )


class ReutersSingleClass(Document):
    document_id = StringField(required=True, unique=True)
    target = ListField(StringField(required=True))
    description = StringField(required=True)
    data_type_lewis = StringField()
    data_Type_cgi = StringField()


thing = ReutersSingleClass()

x = QuerySet(ReutersSingleClass, con)
for doc in thing.objects:
    print(doc.target)