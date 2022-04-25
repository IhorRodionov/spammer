from telethon import TelegramClient
import asyncio
import os
import mysql.connector as con

server = 'server'
database = ''
username = ''
password = ''
connection = con.connect(host=server,
                         database=database,
                         user=username,
                         password=password)

cursor = connection.cursor()
cursor.execute("select name from attacklist;")
spam_list = list(map(lambda x: str(x[0]), cursor.fetchall()))
cursor.close()

fds = os.listdir("photo")
list_name = list(map(lambda x: "photo/"+x, fds))


async def spam(client:TelegramClient):
    for bot in spam_list:
        await client.send_message(bot, "/start")
        for img in list_name:
            await client.send_file(bot, img)

async def user(name, api_id, api_hash):
    async with TelegramClient(name, api_id, api_hash) as client:
        await spam(client)


async def main():
    while True:
        cursor = connection.cursor()
        cursor.execute("select name, api_id, api_hash from people;")
        tasks=[]
        rows = cursor.fetchall()
        for row in rows:
            tasks.append(asyncio.get_event_loop().create_task(user(str(row[0]),
                                                               int(row[1]),
                                                               str(row[2])
                                                               )))
        await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())


