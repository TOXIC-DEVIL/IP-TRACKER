#!/usr/bin/python

# WhatsApp  : https://tinyurl.com/WHATSAPP-TOXIC-DEVIL
# Instagram : https://tinyurl.com/INSTAGRAM-TOXIC-DEVIL
# Github    : https://tinyurl.com/GITHUB-TOXIC-DEVIL
# YouTube   : https://tinyurl.com/YOUTUBE-TOXIC-DEVIL

import os
import urllib2
import json
import colorama
colorama.init(autoreset=True)

os.system("clear");
print(colorama.Fore.CYAN + """

▀█▀ ░█▀▀█ 
░█─ ░█▄▄█ 
▄█▄ ░█─── 

▀▀█▀▀ ░█▀▀█ ─█▀▀█ ░█▀▀█ ░█─▄▀ ░█▀▀▀ ░█▀▀█ 
─░█── ░█▄▄▀ ░█▄▄█ ░█─── ░█▀▄─ ░█▀▀▀ ░█▄▄▀ 
─░█── ░█─░█ ░█─░█ ░█▄▄█ ░█─░█ ░█▄▄▄ ░█─░█

╭━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━╮
╰━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━╯

░█▀▄▀█ ─█▀▀█ ░█▀▀▄ ░█▀▀▀ 　 ░█▀▀█ ░█──░█ 
░█░█░█ ░█▄▄█ ░█─░█ ░█▀▀▀ 　 ░█▀▀▄ ░█▄▄▄█ 
░█──░█ ░█─░█ ░█▄▄▀ ░█▄▄▄ 　 ░█▄▄█ ──░█── 

▀▀█▀▀ ░█▀▀▀█ ▀▄░▄▀ ▀█▀ ░█▀▀█ 
─░█── ░█──░█ ─░█── ░█─ ░█─── 
─░█── ░█▄▄▄█ ▄▀░▀▄ ▄█▄ ░█▄▄█ 

░█▀▀▄ ░█▀▀▀ ░█──░█ ▀█▀ ░█─── 
░█─░█ ░█▀▀▀ ─░█░█─ ░█─ ░█─── 
░█▄▄▀ ░█▄▄▄ ──▀▄▀─ ▄█▄ ░█▄▄█
"""
print "\r"
while True:
		ip = raw_input("Enter Your Target IP : ")
		url = """https://api.ipdata.co/"""
		response = urllib2.urlopen(url + ip)
		data = response.read()
		values = json.loads(data)

		print("------------------------------------")
		print "\r"
		print(" IP           :  " + values['ip'])
		print(" City         :  " + values['city'])
		print(" Region       :  " + values['region'])
		print(" Country      :  " + values['country_name'])
		print(" Continent    :  " + values['continent_name'])
		print(" Time Zone    :  " + values['time_zone'])
		print(" Currency     :  " + values['currency'])
		print(" Calling Code :  " + "+" + values['calling_code'])
		print(" Organisation :  " + values['organisation'])
		print(" ASN          :  " + values['asn'])
		print "\r"
		break
