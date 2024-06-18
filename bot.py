import os
import discord
from discord.ext import tasks
from socket import timeout
import a2s
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

# EXAMPLE: CHANNEL_ID = 36746374674

CHANNEL_ID = "Replace with channel id"
IP = os.getenv("SERVER_IP")
PORT = os.getenv("SERVER_PORT")
SERVER_ADDRESS = (IP, int(PORT))

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    update_player_count.start()

@tasks.loop(minutes=5)
async def update_player_count():
    channel = client.get_channel(CHANNEL_ID)
    if channel is not None:
        # Fetch the last message sent by the bot and delete it
        async for message in channel.history(limit=1):  # You can adjust the limit based on typical traffic
            if message.author == client.user:
                await message.delete()
                break  # Stop after finding and deleting the first bot message

        # Now send the new message
        embed = discord.Embed(title="DayZ Server Status", color=0x00ff00)
        server_info = get_player_count(SERVER_ADDRESS)
        embed.add_field(name="Server Info", value=server_info, inline=False)
        await channel.send(embed=embed)


def get_player_count(server_address):
    try:
        info = a2s.info(server_address, timeout=5.0)
        return f"**Server name:** {info.server_name}\n**Current players:** {info.player_count}/{info.max_players}"
    except timeout:
        return "Query timed out. The server might be offline or the IP/port is incorrect."
    except Exception as e:
        return f"An error occurred: {e}"

client.run(TOKEN)
