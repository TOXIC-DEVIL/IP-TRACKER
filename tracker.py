#!/usr/bin/python

# WhatsApp  : https://tinyurl.com/WHATSAPP-TOXIC-DEVIL
# Instagram : https://tinyurl.com/INSTAGRAM-TOXIC-DEVIL
# TELEGRAM  : Coming Soon...
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
		url = """https://ipapi.co/""" + ip + """/json/"""
		response = urllib2.urlopen(url)
		data = response.read()
		values = json.loads(data)

		print("------------------------------------")
		print "\r"
		print(" IP               :  " + values['ip'])
		print(" City             :  " + values['city'])
		print(" Region           :  " + values['region'])
                print(" Region Code      :  " + values['region_code'])
		print(" Country          :  " + values['country_name'])
		print(" Languages        :  " + values['languages'])
		print(" Country Area     :  " + values['country_area'])
                print(" Country Code     :  " + values['country'])
		print(" Country Capital  :  " + values['country_capital'])
		print(" Postal           :  " + values['postal'])
		print(" Latitude         :  " + values['latitude'])
		print(" Longitude        :  " + values['longitude'])
		print(" Time Zone        :  " + values['timezone'])
		print(" Currency Name    :  " + values['currency_name'])
		print(" Currency         :  " + values['currency'])
		print(" Calling Code     :  " + "+" + values['country_calling_code'])
		print(" Organisation     :  " + values['org'])
		print(" ASN              :  " + values['asn'])
		print "\r"
		break
