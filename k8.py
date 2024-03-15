from telethon.sync import TelegramClient, events
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
import asyncio  # Import asyncio module for sleep function

api_id = 28176665  # Your API ID
api_hash = '79dc0205b83535cbf99c62961bdd30f0'  # Your API hash
phone_number = '+918179842316'
chat_id = 'HeXamonbot'
your_name = "empty"
your_id = "5575157427"
sec_id = 'citx_8543'

start_message = "Haai"
stop_message = "Aaah"

continue_loop = None
repeat = False
ball = 'Ultra'
client = TelegramClient(phone_number, api_id, api_hash)
client.start()

ready = 0
am = False
sm = False
rm = False
chal = False
atk_clm = 0
atk_row = 0

switch = 1

legendary_pokemon = {'Articuno', 'Zapdos', 'Moltres', 'Mewtwo', 'Mew', 'Raikou', 'Entei', 'Suicune', 'Lugia', 'Ho-Oh', 'Celebi', 'Regirock', 'Regice', 'Registeel', 'Latias', 'Latios', 'Kyogre', 'Groudon', 'Rayquaza', 'Jirachi', 'Deoxys', 'Uxie', 'Mesprit', 'Azelf', 'Dialga', 'Palkia', 'Heatran', 'Regigigas', 'Giratina', 'Cresselia', 'Phione', 'Manaphy', 'Darkrai', 'Shaymin', 'Arceus', 'Victini', 'Cobalion', 'Terrakion', 'Virizion', 'Tornadus', 'Thundurus', 'Reshiram', 'Zekrom', 'Landorus', 'Kyurem', 'Keldeo', 'Meloetta', 'Genesect', 'Xerneas', 'Yveltal', 'Zygarde', 'Diancie', 'Hoopa', 'Volcanion', 'Tapu Koko', 'Tapu Lele', 'Tapu Bulu', 'Tapu Fini', 'Cosmog', 'Cosmoem', 'Solgaleo', 'Lunala', 'Necrozma', 'Magearna', 'Marshadow', 'Zeraora', 'Meltan', 'Melmetal', 'Zacian', 'Zamazenta', 'Eternatus', 'Kubfu', 'Urshifu', 'Zarude', 'Regieleki', 'Regidrago', 'Glastrier', 'Spectrier', 'Calyrex'}

async def get_own_name():
    global your_name
    me = await client.get_me()
    your_name = me.first_name if me.first_name else me.username
    print(f"Your name: {your_name}")

async def click_atk(event, atk_clm):
    global am
    print(f"Inside click_button event.")
    am = True
    if event.reply_markup:
        button = event.reply_markup.rows[atk_row].buttons[atk_clm]
        await asyncio.sleep(2)
        while am:
            await client(GetBotCallbackAnswerRequest(
                event.chat_id,
                event.message.id,
                data=button.data
            ))
            print(f"Clicked attack button in attack event.")
            await asyncio.sleep(5)
    else:
        print(f"Message does not contain inline keyboard buttons for button {atk_clm}.")
        return
        

async def click_switch(event, switch):
    global sm
    print(f"Inside switch event clicking button to switch.")
    sm = True
    if event.reply_markup:
        for row in event.reply_markup.rows:
            for button in row.buttons:
                if button.text == str(switch):
                    await asyncio.sleep(2)
                    while sm:
                        await client(GetBotCallbackAnswerRequest(
                            event.chat_id,
                            event.message.id,
                            data=button.data
                        ))
                        print(f"Clicked button: {switch}")
                        await asyncio.sleep(5)
                    pass
    else:
      print(f"No button with number {switch} found in the reply markup.")
      return


async def click_ready(event, ready):
    global rm
    print(f"Inside click_button ready event.")
    rm = True
    if event.reply_markup:
        button = event.reply_markup.rows[0].buttons[ready]
        await asyncio.sleep(1)
        while rm:
            await client(GetBotCallbackAnswerRequest(
                event.chat_id,
                event.message.id,
                data=button.data
            ))
            print(f"Clicked ready button in ready event.")
            await asyncio.sleep(5)
        else:
            print(f"Message does not contain inline keyboard buttons for button ready.")
            pass
    else:
      return
          
async def click_catch(event,):

    global cm

    print(f"Inside click_button catch event.")
    cm = True
    if event.reply_markup:
        button = event.reply_markup.rows[2].buttons[0]
        await asyncio.sleep(1)
        while cm:
            await client(GetBotCallbackAnswerRequest(
                event.chat_id,
                event.message.id,
                data=button.data
            ))
            print(f"Clicked catch button in ready event.")
            await asyncio.sleep(5)
        else:
            print(f"Message does not contain inline keyboard buttons for button catch.")
            pass
    else:
      return
          
async def click_ball(event, ball):

    global bm

    print(f"Inside ball event clicking button to switch.")
    bm = True
    if event.reply_markup:
        for row in event.reply_markup.rows:
            for button in row.buttons:
                if button.text == ball:
                    await asyncio.sleep(2)
                    while bm:
                        print(f"Throwing {ball} ball")
                        await client(GetBotCallbackAnswerRequest(
                            event.chat_id,
                            event.message.id,
                            data=button.data
                        ))
                        print(f"Clicked button: {ball}")
                        await asyncio.sleep(5)
                    pass
    else:
      print(f"No button with number {ball} found in the reply markup.")
      return
        

async def send_challenge_message(event):
    global ball
    ball = 'Ultra'
    await asyncio.sleep(2)
    print("inside hunt loop")
    while chal:
      await client.send_message(chat_id, '/hunt')
      await asyncio.sleep(4)

async def stop_msg(event):
    global continue_loop, chal
    continue_loop = False
    chal = False
    print("Battle stopped.")

@client.on(events.NewMessage(chats=chat_id))
async def handle_new_message(event):
    global start_message_id
    global continue_loop
    global switch, continue_loop, am, sm, chal, bm, cm, ball
    sm = False
    am = False
    bm = False
    cm = False
    rm = False
    print(f"New message from {event.sender_id}: {event.text}")
    if 'a wild' in event.message.text.lower():
        chal = False
        switch = 1
        if '✨' in event.message.text:
          await client.send_message(sec_id, 'A shiny has appeared ✨')
          return
        elif '✨' not in event.message.text:
          legend = False
          for pokemon in legendary_pokemon:
            if f'{pokemon}' in event.message.text:
              if '☆' in event.message.text:
                ball = 'Repeat'
              await client.send_message(sec_id, f'A legendary pokemon {pokemon} was found')
              await click_ready(event, ready)
              legend = True
              break
          if not legend:
            await click_ready(event, ready)
    elif f'Current turn: [{your_name}](tg://user?id={your_id})' in event.message.text:

        if 'fainted' in event.message.text.lower():
            switch = (switch % 6) + 1
            await click_switch(event, switch)
        elif 'fainted' not in event.message.text.lower():
            legend = False
            for pokemon in legendary_pokemon:
              if 'Wild' and f'{pokemon}' in event.message.text:
                await client.send_message(sec_id, f"Catching {pokemon}")
                await click_catch(event)
                legend = True
                break
            if not legend:
              await click_atk(event, atk_clm)
    else:
        pass

@client.on(events.MessageEdited(chats=chat_id))
async def handle_message_edit(event):
    print("Message edited event started.")
    global switch, continue_loop, am, sm, rm, chal, repeat, cm, bm
    sm = False
    am = False
    rm = False
    cm = False
    bm = False
    print(f"Message edited by {event.sender_id}: {event.text}")
    if f'Current turn: [{your_name}](tg://user?id={your_id})' in event.message.text:
        if 'fainted' in event.message.text.lower():
            switch = (switch % 6) + 1
            await click_switch(event, switch)
        elif 'fainted' not in event.message.text.lower():
            legen = False
            pow = False
            if 'Power' not in event.message.text:
              await click_ball(event, ball)
              pow = True
            if not pow:
             for pokemon in legendary_pokemon:
                if 'Wild' and f'{pokemon}' in event.message.text:
                  await click_catch(event)
                  legen = True
                  break
            if not (legen and pow):
              await click_atk(event, atk_clm)         
    elif 'the wild' in event.message.text.lower():
        print(f"Opponent 'defeated'. Button name set to 1")
        if continue_loop == True:
            print("Starting hunt again")
            chal = True
            await send_challenge_message(event)
        elif continue_loop == False:
            print ("Send start msg again to start auto battle.")
    elif 'caught' in event.message.text.lower():
        print(f"Pokemon caught. Button name set to 1")
        await client.send_message(sec_id,f'{event.message.text}')
        if continue_loop == True:
            print("Starting challenge again")
            chal = True
            await send_challenge_message(event)
        elif continue_loop == False:
            print ("Send start msg again to start auto battle.")
    else:
        pass

@client.on(events.NewMessage(chats=sec_id))
async def handle_change_attack(event):
    global atk_clm, atk_row, chal, continue_loop
    print(f"Message sent by {event.sender_id}: {event.text}")
    if event.text.startswith('/bh'):
            _, new_atk_row, new_atk_clm = event.text.split()
            atk_row = int(new_atk_row)
            atk_clm = int(new_atk_clm)
            print(f"Updated atk_row: {atk_row}, atk_clm: {atk_clm}")
            await event.respond(f"Values updated: atk_row={atk_row}, atk_clm={atk_clm}")
    elif event.text.lower() == start_message.lower():
            continue_loop = True
            print("Sending /hunt message to the user...")
            chal = True
            await event.respond("Starting Hunt again")
            await send_challenge_message(event)
    elif event.text.lower() == stop_message.lower():
        await event.respond("Stopping Hunt")
        await stop_msg(event)
    elif event.raw_text.startswith('/new '):
        pokemon = event.raw_text.split('/new ')[1]
        legendary_pokemon.add(pokemon)
        print(f"'{pokemon}' added to the list of legendary Pokemon.")
        await event.respond(f"✨ '{pokemon}' added to the list of legendary Pokemon! Keep exploring! 🌟")
    elif event.raw_text.startswith('/old '):
        pokemon = event.raw_text.split('/old ')[1]
        if pokemon in legendary_pokemon:
            legendary_pokemon.remove(pokemon)
            print(f"'{pokemon}' removed from the list of legendary Pokemon.")
            await event.respond(f"❌ '{pokemon}' removed from the list of legendary Pokemon! Keep hunting! 🌟")
        else:
            print(f"'{pokemon}' is not in the list of legendary Pokemon.")
            await event.respond(f"❓ '{pokemon}' is not in the list of legendary Pokemon! Keep exploring! 🌟")
    elif event.raw_text == '/name':
        pokemon_list = '\n'.join([f"- {pokemon}" for pokemon in legendary_pokemon])
        print("Sending the list of legendary Pokemon...")
        await event.respond(f"📜 List of Legendary Pokemon: \n{pokemon_list} 🌟")
    else:
        pass
with client:
    client.loop.run_until_complete(get_own_name())
    client.run_until_disconnected()
