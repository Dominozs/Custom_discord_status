from pypresence import Presence
import time, os, sys, random, json
with open('Info.json', 'r') as f:
  data = f.read()

parsed_data = json.loads(data)

client_id = parsed_data['client_id']
if client_id == 'YourClientId':
    print('Please check your config.json file!')
    print('Client ID must be filled')
    time.sleep(3)
    exit()

RPC = Presence(client_id)
print('Connecting..')
RPC.connect()
os.system('cls')
print("    ____  _                          __")
print("   / __ \(_)_____________  _________/ /          ")
print("  / / / / / ___/ ___/ __ \/ ___/ __  /           ")
print(" / /_/ / (__  ) /__/ /_/ / /  / /_/ /            ")
print("/_____/_/____/\___/\____/_/ __\__,_/             ")
print("          / ____/_  _______/ /_____  ____ ___    By : Domino")
print("         / /   / / / / ___/ __/ __ \/ __ `__ \   Discord : Domino#6136")
print("        / /___/ /_/ (__  ) /_/ /_/ / / / / / /   ")
print("        \____/\__,_/____/\__/\____/_/ /_/ /_/    ")
print("                  / ___// /_____ _/ /___  _______")
print("                  \__ \/ __/ __ `/ __/ / / / ___/")
print("                 ___/ / /_/ /_/ / /_/ /_/ (__  ) ")
print("                /____/\__/\__,_/\__/\__,_/____/  ")
print('Connected')
print('User ID: ', client_id)
an2 = input('State(Down text) : ')
an1 = input('Details(Up text) : ')
an3 = input('With time? [Y/N]: ')

if an3 == 'Y' or an3 == 'Y' or an3 == '':
        RPC.update( 
    state=an1,
    details=an2,
    large_image='large',
    start=int(time.time())
    )
else:
        RPC.update( 
    state=an1,
    details=an2,
    large_image='large'
    )

while True:
    time.sleep(15)