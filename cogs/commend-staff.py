import discord
import re
from discord.ext import commands

class CommandStaffCog(commands.Cog):
    def __init__(self, bot):
            self.bot = bot
    
    MESSAGE_LINK_REGEX = re.compile(r"https://(?:ptb\.|canary\.)?discord(?:app)?\.com/channels/(\d+)/(\d+)/(\d+)")

    @discord.app_commands.command()
    async def mp(self, interaction: discord.Interaction, cible: discord.Member | discord.Role, lien_message: str):
        await interaction.response.defer(ephemeral=True)

        guild_id, channel_id, message_id = map(int, self.MESSAGE_LINK_REGEX.match(lien_message).groups())

        channel = interaction.guild.get_channel(channel_id) or await interaction.guild.fetch_channel(channel_id)
        message = await channel.fetch_message(message_id)

        destinataires = cible.members if isinstance(cible, discord.Role) else [cible]

        for membre in destinataires:
            await membre.send(f"{message.content}\n{lien_message}")

        await interaction.followup.send(f"Envoyé à {len(destinataires)} personne(s).", ephemeral=True)

async def setup(bot):
    await bot.add_cog(CommandStaffCog(bot))