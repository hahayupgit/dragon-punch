async def default(message, admin, client):
    if str(message.author.global_name) in admin:
            await message.channel.send('Goodbye!')
            await client.close()
