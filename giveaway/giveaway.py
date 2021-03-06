from redbot.core import commands
from redbot.core import Embed
import datetime
import time
import asyncio
import random


class giveaway(commands.Cog):
    """Giveaway Cog for GGCGBot"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def giveaway(self, ctx, time: int, *, prize):
        """The Act of the Giveaway"""
        giveawayembed = discord.Embed(
            title="ðLook a Giveaway!ð",
            colour=discord.Color.purple()
        )

        giveawayembed.add_field(name="Prize", value="{}".format(prize), inline=False)
        giveawayembed.add_field(name="Hosted by", value=f"{ctx.author.mention}", inline=False)
        giveawayembed.add_field(name="Ends in", value="{}s".format(time))
        
        msg = await ctx.send(embed=giveawayembed)

        await msg.add_reaction("ð")
        await asyncio.sleep(time)
        msg = await msg.channel.fetch_message(msg.id)
        winner = None
        
        """For loop for actual giveaway generation"""
        for reaction in msg.reactions:
            if reaction.emoji == "ð":
                users = await reaction.users().flatten()
                users.remove(self.client.user)
                winner = random.choice(users)

        if winner is not None:
            endembed = discord.Embed(
                title="Giveaway ended!",
                description="Prize: {}\nWinner: {}".format(prize, winner))

            await msg.edit(embed=endembed)

    @giveaway.error
    async def giveaway_error(self, ctx, error):
        await ctx.send(error)
        print(error)
        raise error

def setup(client):
    client.add_cog(Giveaway(client))
