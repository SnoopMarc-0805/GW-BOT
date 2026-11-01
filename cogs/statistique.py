import discord
from discord.ext import commands
from discord.ext import tasks

class StatistiqueCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.update_stats.start()

    @tasks.loop(minutes= 6)
    async def update_stats(self):
        guild = self.bot.get_guild(1381203365370925096)

        if guild is None:
            return

        online = sum(
            1
            for member in guild.members
            if member.status != discord.Status.offline
        )

        channel_membres = guild.get_channel(1485310142819074161)
        channel_online = guild.get_channel(1485310626099105794)

        if channel_membres:
            await channel_membres.edit(name=f"Membre: {guild.member_count}")
        if channel_online:
            await channel_online.edit(name=f"En ligne: {online}")

    @update_stats.before_loop
    async def before_update_stats(self):
        await self.bot.wait_until_ready()

async def setup(bot):
    await bot.add_cog(StatistiqueCog(bot))