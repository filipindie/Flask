# from app import pg_db
from peewee import *
db = PostgresqlDatabase('flaski', user='postgres', password='m249sopmod', host='localhost', port=5432) #cria as tables no db
class BaseModel(Model):
    class Meta:
        database = db

class Users(BaseModel):
    id = PrimaryKeyField()
    username = CharField(unique=True)
    name = CharField()
    password = CharField()
    email = CharField()
    
    @property
    def is_autheticated(self):
        return True
    
    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)


class Post(BaseModel):
    id = PrimaryKeyField()
    content = TextField()
    users_id = ForeignKeyField(Users)
    follower_id = ForeignKeyField(Users)


class Follow(BaseModel):
    id = PrimaryKeyField()
    id_user = ForeignKeyField(Users)   





#Conectando ao DB
def initialize_pg_db():
    db.connect()
    db.create_tables([Users, Post, Follow])
    db.close()
    