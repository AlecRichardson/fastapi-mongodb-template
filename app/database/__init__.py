import motor.motor_asyncio


client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://admin:Passw0rd!@cluster0.aylu4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.primary_db
