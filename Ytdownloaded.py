import os
import requests
import time
import json

os.system("clear")
print ("\033[1;32m[+] Downloading && INSTALLING Figlet")
time.sleep(1.05)

os.system("pkg install figlet")

os.system("clear")
print ("\033[1;32m[+] Installed Successfully Figlet")
time.sleep(1.05)
os.system("clear)
print ("\033[1;32m[+] Downloading && INSTALLING Requests")
time.sleep(1.05)
os.system("pip install requests")
print ("\033[1;32m[+] Requests successfully Installed!!")
time.sleep(1.05)
os.system("clear)


from termcolor import colored



os.system("clear")


print(colored("==================================================================" , 'red'))
os.system('figlet Insta-info')
print(colored("==================================================================" , 'red'))

print ( "                        \033[34m COD3D BY R3X1N             ")
print ( "                        \033[  INSTA:-psycho_rexin_ofc_               ")
print(".")
print ( "                        \033[34m CONTACT-ME:-https://t.me/psycho_rexin_ofc             ")



#ask for username
def get_account_data(username):

   response = requests.get(f'https://www.instagram.com/{username}/?__a=1')


   if response.status_code == 200:
   # Parse the JSON data from the response
     data = json.loads(response.text)

     # Showing 
     username = data['graphql']['user']['username']
     full_name = data['graphql']['user']['full_name']
     followers = data['graphql']['user']['edge_followed_by']['count']
     following = data['graphql']['user']['edge_follow']['count']
     profile_picture_url = data['graphql']['user']['profile_pic_url']


     # Return the extracted data as a dictionary
     return {
       'username': username,
       'full_name': full_name,
       'followers': followers,
       'following': following,
       'profile_picture_url': profile_picture_url,
     }
   else:
     #if the request was not successful return to emty directory
     return {}
     
#example
account_data = get_account_data('instagram')
print(account_data)
     