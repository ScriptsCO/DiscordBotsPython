from imports import  *


class var():
    """
    a class of varables 
    """ 
    bot = discord.Client(intents=discord.Intents.all())
    tree = app_commands.CommandTree(bot)
    CustomColor = discord.Color.from_rgb
    """
    just use rgb to get colors or 
    CustomColor(r,g,b)
    """
    
class functions_events(): 
    """
    This is a class fuctions for events and other shit 
    
    
    contains
    onready 
    sync 
    onjoin coming soon
    onleave coming soon
    botstart
    
    """
    async def sync():
        """
        syncs the tree to discord never call this as it is in the onready function! 
        """
        try:
            await var.tree.sync
            print('synced to discord')
        except Exception as e:
            print({e})
    async def onready():
        """
        this is just onready all you have to do is
        
        
        @var.bot.event
        async def on_ready()
            await functions_events.onready()
        """
        print(f"loged in to {var.bot.user.name}")
        await sync()
    
        