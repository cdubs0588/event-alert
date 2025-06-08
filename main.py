import discord
from discord.ext import commands

# Define intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.messages = True

# Set up bot
bot = commands.Bot(command_prefix="!", intents=intents)

# === SETTINGS ===
TRIGGER_STRINGS = ["Boss Battle", "Dank Scrambled Eggs"]
ALERT_CHANNEL_ID = 1381406773340278804  # Alert channel in home server
ALERT_ROLE_ID = 951560990586208317     # Replace this with the role ID to tag

@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content.lower()
    if any(trigger.lower() in content for trigger in TRIGGER_STRINGS):
        # Build alert message
        alert_msg = (
            f"<@&{ALERT_ROLE_ID}> Keyword detected!\n"
            f"**Server:** {message.guild.name if message.guild else 'DM'}\n"
            f"**Channel:** <#{message.channel.id}>\n"
            f"**User:** {message.author.mention}\n"
            f"**Message:** {message.content}\n"
            f"**Link:** [Jump to message]({message.jump_url})"
        )

        alert_channel = bot.get_channel(ALERT_CHANNEL_ID)
        if alert_channel:
            await alert_channel.send(alert_msg)
        else:
            print("❗ Could not find the alert channel.")

    await bot.process_commands(message)

# Run the bot (replace with your token)
bot.run("1381395904279609354")
