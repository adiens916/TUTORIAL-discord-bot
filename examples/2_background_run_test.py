from time import sleep

import discord

from settings import TOKEN, CHANNEL_ID


class MyClient(discord.Client):
    async def on_ready(self):
        channel = self.get_channel(int(CHANNEL_ID))  # 특정 채널 가져오기

        count = 1
        while True:
            await channel.send(str(count))  # 해당 채널에 메시지 보내기
            count += 1
            sleep(1)  # 1초 대기

            if count == 100:
                break


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)
