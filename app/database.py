from typing import Optional
import motor.motor_asyncio

# DEPRECATED
client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://admin:Passw0rd!@cluster0.aylu4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

# https://motor.readthedocs.io/en/stable/api-asyncio/asyncio_motor_client.html?highlight=AsyncIOMotorClient
class Database:
    db = None
    database_name = None

    def __init__(self, database_name: Optional[str]):
        print('\n init\n')
        self.database_name = database_name
        self.connect()

    def __enter__(self):
        return self.db
    
    def __exit__(self, *args, **kwargs):
        client.close()

    def connect(self):
        self.db = client[self.database_name]

    def reset(self):
        client = None
        self.db = None
        self.database_name = None

database = Database


async def get_db(database_name: Optional[str] = 'primary_db'):
    with Database(database_name) as db:
        yield db


