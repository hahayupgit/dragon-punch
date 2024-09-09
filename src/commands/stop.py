async def default(message, admin, client):
    if str(message.author) in admin:
            await message.channel.send('Goodbye!')
            await client.close()
