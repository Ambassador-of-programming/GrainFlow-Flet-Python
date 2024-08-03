import aiosqlite
import asyncio

class DatabaseManager():
    def __init__(self):
        self.db_name = 'database/db_file.db'
        
    # подключение к базе данных
    async def connect(self):
        self.connection = await aiosqlite.connect(self.db_name)
        return self.connection
    
    # закрытие подключения к базе данных
    async def close(self):
        if self.connection:
            return await self.connection.close()
    
    # выполнение запроса
    async def execute_query(self, query, *args):
        async with self.connection.execute(query, args) as cursor:
            return await cursor.fetchall()
     
    # выполнение записи в базу данных
    async def execute_write_query(self, query, *args):
        async with self.connection.execute(query, args) as cursor:
            await self.connection.commit()

class Auth(DatabaseManager):
    def __init__(self):
        super().__init__()
    
    # создание базы данных
    async def create_db(self):
        await self.connect()
        await self.execute_write_query(
            '''CREATE TABLE IF NOT EXISTS auth 
            (id INTEGER PRIMARY KEY, username TEXT, password TEXT)'''
        )
        await self.close()
    
    # добавление пользователя в базу данных
    async def add_user(self, username, password):
        await self.connect()
        await self.execute_write_query(
            '''INSERT INTO auth (username, password) VALUES (?,?)''',
            username, password
        )
        await self.close()
    
    # проверка есть ли пользователь в базе данных
    async def check_user(self, username: str, password: str) -> bool:
        await self.connect()
        result = await self.execute_query(
            '''SELECT * FROM auth WHERE username =? AND password =?''',
            username, password
        )
        await self.close()
        if result:
            return True
        else:
            return False

# async def test():
#     auth = Auth()
#     print(await auth.check_user('admin', 'admin1'))

# if __name__ == '__main__':
#     asyncio.run(test())