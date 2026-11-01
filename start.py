import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from keep_alive import keep_alive

load_dotenv()

class MonBot(commands.Bot):
    async def setup_hook(self):
        for extension in ['arriver', 'règlement', 'statistique', 'role', 'commend-staff']:
            await self.load_extension(f"cogs.{extension}")

bot = MonBot(command_prefix= "!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("✅ Bot started")
    try:
        sync = await bot.tree.sync()
        print(f"✅ Synchronize command: {len(sync)}")
    except Exception as e:
        print(f"⚠️  {e}")

keep_alive()
bot.run(token= os.getenv('TOKEN'))