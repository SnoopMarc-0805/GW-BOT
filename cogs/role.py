import discord
from discord.ext import commands

class RoleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command() #règlement
    async def role_activate(self, intéraction: discord.Integration, code: int):
        channel_role = self.bot.get_channel(1381210037480853646)
    
        if code == 7789256256:
            await channel_role.send("https://cdn.discordapp.com/attachments/1243273974725738629/1538922950135250964/1-removebg-preview.png?ex=6a84712f&is=6a831faf&hm=aeed17cfc41cf0fcb9773d17491e3cd6cf583de28cb85a5dc85af49dc86c02ab&")
            embed1 = discord.Embed(
                title= "STAFF",
                description= "Vous pourrez retrouver ici l'intégralité des rôles du staff de la GW Esport.",
                color= discord.Color.from_str("#12ccaa")
            )

            embed1.add_field(name="", value= "<@1533863299219980460> \n <@&1381203365395955788> \n <@&1381203365395955787> \n <@&1381203365395955786> \n <@&1464675814871142715>")
            await channel_role.send(embed= embed1)

            await channel_role.send("https://cdn.discordapp.com/attachments/1243273974725738629/1538922949774544956/2-removebg-preview.png?ex=6a84712f&is=6a831faf&hm=f2077c529be9f4c62579dceeea8368bf57813aa43df5c6d17d1100eec29d4772&")
            embed2 = discord.Embed(
                title= "ESPORT",
                description= "Vous pourrez retrouver ici l'intégralité des rôles des membres de la GW Esport.",
                color= discord.Color.from_str("#12ccaa")
            )

            embed2.add_field(name="", value= "<@&1457323429865721978> \n <@&1484268431061811371>")
            await channel_role.send(embed= embed2)

            await channel_role.send("https://cdn.discordapp.com/attachments/1243273974725738629/1538922950424793178/3-removebg-preview_1.png?ex=6a84712f&is=6a831faf&hm=cbc7a52341da7a95112eda516627448198f59abaec80eb7c2f64cc4656ed83d2&")
            embed3 = discord.Embed(
                title= "SPECIALS",
                description= "Vous pourrez retrouver ici l'intégralité des rôles spéciaux de la GW Esport.",
                color= discord.Color.from_str("#12ccaa")
            )

            embed3.add_field(name="", value= "<@&1381203365383376984> \n <@&1457327057515188390>")
            await channel_role.send(embed= embed3)

            await channel_role.send("https://cdn.discordapp.com/attachments/1243273974725738629/1538923282286248047/4-removebg-preview.png?ex=6a84717e&is=6a831ffe&hm=22d3483417175ce9a84bacb19d0edec7ca84def6da7007a5bbf5a5efcb69e2aa&")
            embed4 = discord.Embed(
                title= "DON",
                description= "Vous pourrez retrouver ici l'intégralité des rôles donateurs de la GW Esport.",
                color= discord.Color.from_str("#12ccaa")
            )

            embed4.add_field(name="", value= "<@&1533543959937290270> \n <@&1533543866161168416> \n <@&1480220310874751159> \n <@&1533545025500086332> \n <@&1480219970297397258>")
            await channel_role.send(embed= embed4)

            await channel_role.send("https://cdn.discordapp.com/attachments/1243273974725738629/1538923282626248886/5-removebg-preview_1.png?ex=6a84717e&is=6a831ffe&hm=11907de18a74dab2ac3a2908706da279e602f154fa984792fe3eb9291aaa1122&")
            embed5 = discord.Embed(
                title= "BADGE",
                description= "Vous pourrez retrouver ici l'intégralité des rôles badges de la GW Esport.",
                color= discord.Color.from_str("#12ccaa")
            )

            embed5.add_field(name="", value= "<@&1457329670239555712> \n <@&1485303677135749260>")
            await channel_role.send(embed= embed5)

            await channel_role.send("https://cdn.discordapp.com/attachments/1243273974725738629/1538923497814753310/6-removebg-preview_1.png?ex=6a8471b1&is=6a832031&hm=eaa38280c2dc6deebadca4aa3386ffcb127e8776c90cde44414ce3cbbca9bf10&")
            embed6 = discord.Embed(
                title= "NOTIFICATION",
                description= "Vous pourrez retrouver ici l'intégralité des rôles notifications de la GW Esport.",
                color= discord.Color.from_str("#12ccaa")
            )

            embed6.add_field(name="", value= "<@&1381203365370925105> \n <@&1381203365370925104> \n <@&1496161249258639501> \n <@&1520543788219498606>")
            await channel_role.send(embed= embed6)

            await channel_role.send("https://cdn.discordapp.com/attachments/1243273974725738629/1538923498146242670/7-removebg-preview_1.png?ex=6a8471b1&is=6a832031&hm=96f6d2c0df72e80681a3e667475af66177c1304668c1aa2cb6d756fdde78f9fe&")
            embed7 = discord.Embed(
                title= "MEMBER",
                description= "Vous pourrez retrouver ici l'intégralité des rôles membres de la GW Esport.",
                color= discord.Color.from_str("#12ccaa")
            )

            embed7.add_field(name="", value= "<@&1455703037342515302> \n <@&1381203365370925100> \n <@&1381203365370925099>")
            await channel_role.send(embed= embed7)
        
async def setup(bot):
    await bot.add_cog(RoleCog(bot))