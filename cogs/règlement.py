import discord
from discord.ext import commands
from datetime import datetime

class ReglementCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command() #règlement
    async def reglement_activate(self, intéraction: discord.Integration, code: int):
        channel_règlement = self.bot.get_channel(1381203366121705526)

        await channel_règlement.send("https://cdn.discordapp.com/attachments/1243273974725738629/1534525657675989093/RULE-removebg-preview_1.png?ex=6a7471e2&is=6a732062&hm=8ca1c7d5caaca30a5a9c7c8c072b4f6d0b3cbb9ee3d58a89bfe2bc1c97b9f564")

        if code == 9866403785:
            embed = discord.Embed(
                title= "Bienvenue sur le serveur de GW Esport",
                description= "## Voici quelques règles importantes à suivre pour garantir une expérience agréable pour tous :",
                color= discord.Color.from_str("#12ccaa")
            )
            date = datetime.now().strftime("%d/%m/%Y %H:%M")

            embed.set_author(name= "GW Esport", url= "https://cdn.discordapp.com/attachments/1243273974725738629/1486101414475337890/Logo.jpg?ex=6a71a48b&is=6a70530b&hm=920a8e15509140edb1109207e322c0ed4b0f8a2b529419b09676769eeceae295")
            embed.add_field(name= "🤝 Respect des Membres", value= "- Respectez toujours les autres membres du serveur. \n - Pas de harcèlement, de discours haineux, ou de comportement offensant.", inline= True)
            embed.add_field(name= "🔞 Contenu approprié", value= "- Pas de contenu inapproprié, adulte, ou offensant. \n - Évitez les discussions politiques ou religieuses sensibles.", inline= True)
            embed.add_field(name= "", value= "", inline= False)
            embed.add_field(name= "🚫 Spam et Publicité", value= "- Pas de spam, de flood, ou de messages répétitifs. \n - Pas de publicité non autorisée par les admins.", inline= True)
            embed.add_field(name= "📌 Canaux Appropriés", value= "- Utilisez les canaux de manière appropriée selon leur thème. \n - Évitez le hors-sujet dans les discussions.", inline= True)
            embed.add_field(name= "", value= "", inline= False)
            embed.add_field(name= "💬 Langage et Ton", value= "- Utilisez un langage respectueux et courtois. \n - Évitez les majuscules excessives ou le langage vulgaire. \n -Merci de ne pas mettre son message en avant avec les balises heading (#) de Discord ou par une autre manière.", inline= True)
            embed.add_field(name= "⚠️ Respect des Modérateurs", value= "- Suivez les instructions des modérateurs. \n - Respectez leur décision. \n - Interdiction de MP et de demander en ami les staffs sauf si celui-ci vous le demande. Si besoin d'aide : <#1383725351439700008>", inline= True)
            embed.add_field(name= "", value= "", inline= False)
            embed.add_field(name= "🚨 Mentions abusives", value= "- Interdiction formelle de ping les <@&1381203365395955788> \n - Le ping du staff est autorisé mais limité. Merci de ne pas en abuser.", inline= True)
            embed.add_field(name= "🔒 Protection des Données et DOX", value= "- Ne partagez pas d'informations personnelles. Qu'elles soient à vous ou quelqu'un d'autre. \n - Respectez la vie privée des autres membres.", inline= True)
            embed.add_field(name= "", value= "**En rejoignant ce serveur, vous acceptez de respecter ces règles. En cas de non-respect, des mesures pourront être prises par l'équipe de modération.** \n **Ce règlement est sujet à modification. Veuillez le consulter régulièrement pour rester à jour.**", inline= False)
            embed.set_footer(text= f"{date}", icon_url= "https://cdn.discordapp.com/attachments/1243273974725738629/1486101414475337890/Logo.jpg?ex=6a71a48b&is=6a70530b&hm=920a8e15509140edb1109207e322c0ed4b0f8a2b529419b09676769eeceae295")

            message = await channel_règlement.send(embed= embed)
            await message.add_reaction("✅")

        else:
            print("")

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        guild = await self.bot.fetch_guild(payload.guild_id)
        member = await guild.fetch_member(payload.user_id)
        role_add = guild.get_role(1381203365370925100)
        role_remove = guild.get_role(1381203365370925099)
        
        if payload.message_id == 1534528031727816766 and payload.emoji.name == "✅":
            await member.add_roles(role_add)
            await member.remove_roles(role_remove)

async def setup(bot):
    await bot.add_cog(ReglementCog(bot))