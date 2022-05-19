import os
import scratchattach as scratch3
import Keep_alive
from replit import db

session = scratch3.login("Orago_Server", os.environ['PASSWORD'])
conn = session.connect_cloud(project_id=691182767)

client = scratch3.CloudRequests(conn, ignore_exceptions=True)


@client.request
def add_dat(argument1, agrument2):
    print(agrument2)
    db[argument1] = agrument2
    return "success"


@client.request
def ping():
    print("Ping request received")
    return "I'm alive program ready"


@client.request
def get_dat(argument1):
    return db[argument1]


@client.request
def admin_list():
    return db.keys()


@client.request
def admin_get(argument1):
    return db[argument1]


@client.request
def admin_del(argument1):
    del db[argument1]
    return "success"


@client.event
def on_ready():
    print("Request handler is ready")


Keep_alive.keep_alive()
client.run()  #Make sure this is ALWAYS at the bottom of your Python file!
