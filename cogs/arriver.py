import discord
import asyncio
from discord.ext import commands
from datetime import datetime

class ArriverCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener() #Arriver d'une personne sur le serveur
    async def on_member_join(self, member: discord.Member):
        channel_arriver = self.bot.get_channel(1381208630325547079)

        role = member.guild.get_role(1381203365370925099)

        await channel_arriver.send(f"Bienvenue {member.mention} !!!")
        await member.add_roles(role)

        embed = discord.Embed(
            title= "Bienvenue sur le serveur de la GW Esport.",
            color= discord.Color.from_str("#12ccaa")
        )
        date = datetime.now().strftime("%d/%m/%Y %H:%M")

        embed.set_author(name= "GW Esport", url= "https://cdn.discordapp.com/attachments/1243273974725738629/1486101414475337890/Logo.jpg?ex=6a71a48b&is=6a70530b&hm=920a8e15509140edb1109207e322c0ed4b0f8a2b529419b09676769eeceae295")
        embed.set_image(url="https://cdn.discordapp.com/attachments/1243273974725738629/1533878277780017203/Bonjour_et_Bienvenue.png?ex=6a7216f7&is=6a70c577&hm=aac4cfdd27ab1eeaae3d5f2bd31c9dd02097da42eaf70e8e062813284e5df3e8")
        embed.set_footer(text= f"{date}", icon_url= "https://cdn.discordapp.com/attachments/1243273974725738629/1486101414475337890/Logo.jpg?ex=6a71a48b&is=6a70530b&hm=920a8e15509140edb1109207e322c0ed4b0f8a2b529419b09676769eeceae295")

        await channel_arriver.send(embed= embed)
        await asyncio.sleep(3)

        try:

            embed1 = discord.Embed(
                title= "Bienvenue sur le serveur de **SnoopMarc**.",
                description= "Mais avant d'accéder aux serveurs de SnoopMarc. Il va falloir que tu **acceptes le règlement**.",
                color= discord.Color.dark_blue()
            )
            date = datetime.now().strftime("%d/%m/%Y %H:%M")

            embed1.set_author(name= "Snoop Bot", url= "https://cdn.discordapp.com/attachments/1243273974725738629/1486101414475337890/Logo.jpg?ex=6a71a48b&is=6a70530b&hm=920a8e15509140edb1109207e322c0ed4b0f8a2b529419b09676769eeceae295")
            embed1.add_field(name= "Pour accepter le règlement du serveur, il faut :", value= "👇", inline= False)
            embed1.add_field(name= "1️⃣", value= "Aller dans le salon, règlement.", inline= False)
            embed1.add_field(name= "2️⃣", value= "Lire le règlement", inline= False)
            embed1.add_field(name= "3️⃣", value= "Acceptez le règlement en cliquant sur le bouton en bas du règlement", inline= False)
            embed1.add_field(name= "Profite bien de ton aventure parmi nous.", value="Merci à toi de nous avoir rejoint.", inline= False)
            embed1.set_footer(text= f"{date}", icon_url= "https://cdn.discordapp.com/attachments/1243273974725738629/1486101414475337890/Logo.jpg?ex=6a71a48b&is=6a70530b&hm=920a8e15509140edb1109207e322c0ed4b0f8a2b529419b09676769eeceae295")


            await member.send(embed= embed1)

        except discord.Forbidden:
            await print("")

async def setup(bot):
    await bot.add_cog(ArriverCog(bot))  