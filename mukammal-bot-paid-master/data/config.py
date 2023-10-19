from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("IP")

CHANNELS = [
    {'name': "Test 1", "url": "https://t.me/+Jv-udSqYUF0xYTZi", "id": -1001925422629},
    {'name': "Test 2", "url": "https://t.me/+jsrUNDsNxIIxOTUy", "id": -1001908165511}
]
