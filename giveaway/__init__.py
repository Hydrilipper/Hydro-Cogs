from .giveaway import giveaway


def setup(bot):
    bot.add_cog(giveaway(bot))