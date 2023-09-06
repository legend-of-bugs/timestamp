import time
import hashlib
import argparse
import json
from colorama import Fore,init

init()
parser = argparse.ArgumentParser()
parser.add_argument("-u",help="Enter your username or email", required=True)
parser.add_argument("-s",help="Enter the second you want the timestamp to run", required=True)
arg = parser.parse_args()

def banner():
    print(f"""
  {Fore.RED}$${Fore.WHITE}\     {Fore.RED}$${Fore.WHITE}\                                           {Fore.RED}$${Fore.WHITE}\                                       
  {Fore.RED}$${Fore.WHITE} |    \__|                                          {Fore.RED}$${Fore.WHITE} |                                      
{Fore.RED}$$$$$${Fore.WHITE}\   {Fore.RED}$${Fore.WHITE}\ {Fore.RED}$$$$$${Fore.WHITE}\{Fore.RED}$$$${Fore.WHITE}\   {Fore.RED}$$$$$${Fore.WHITE}\         {Fore.RED}$$$$$$${Fore.WHITE}\ {Fore.RED}$$$$$${Fore.WHITE}\    {Fore.RED}$$$$$${Fore.WHITE}\  {Fore.RED}$$$$$${Fore.WHITE}\{Fore.RED}$$$${Fore.WHITE}\   {Fore.RED}$$$$$${Fore.WHITE}\  
\_{Fore.RED}$${Fore.WHITE}  _|  {Fore.RED}$${Fore.WHITE} |{Fore.RED}$${Fore.WHITE}  _{Fore.RED}$${Fore.WHITE}  _{Fore.RED}$${Fore.WHITE}\ {Fore.RED}$${Fore.WHITE}  __{Fore.RED}$${Fore.WHITE}\       {Fore.RED}$${Fore.WHITE}  _____|\_{Fore.RED}$${Fore.WHITE}  _|   \____{Fore.RED}$${Fore.WHITE}\ {Fore.RED}$${Fore.WHITE}  _{Fore.RED}$${Fore.WHITE}  _{Fore.RED}$${Fore.WHITE}\ {Fore.RED}$${Fore.WHITE}  __{Fore.RED}$${Fore.WHITE}\ 
  {Fore.RED}$${Fore.WHITE} |    {Fore.RED}$${Fore.WHITE} |{Fore.RED}$${Fore.WHITE} / {Fore.RED}$${Fore.WHITE} / {Fore.RED}$${Fore.WHITE} |{Fore.RED}$$$$$$$${Fore.WHITE} |      \{Fore.RED}$$$$$${Fore.WHITE}\    {Fore.RED}$${Fore.WHITE} |     {Fore.RED}$$$$$$${Fore.WHITE} |{Fore.RED}$${Fore.WHITE} / {Fore.RED}$${Fore.WHITE} / {Fore.RED}$${Fore.WHITE} |{Fore.RED}$${Fore.WHITE} /  {Fore.RED}$${Fore.WHITE} |
  {Fore.RED}$${Fore.WHITE} |{Fore.RED}$${Fore.WHITE}\ {Fore.RED}$${Fore.WHITE} |{Fore.RED}$${Fore.WHITE} | {Fore.RED}$${Fore.WHITE} | {Fore.RED}$${Fore.WHITE} |{Fore.RED}$${Fore.WHITE}   ____|       \____{Fore.RED}$${Fore.WHITE}\   {Fore.RED}$${Fore.WHITE} |{Fore.RED}$${Fore.WHITE}\ {Fore.RED}$${Fore.WHITE}  __{Fore.RED}$${Fore.WHITE} |{Fore.RED}$${Fore.WHITE} | {Fore.RED}$${Fore.WHITE} | {Fore.RED}$${Fore.WHITE} |{Fore.RED}$${Fore.WHITE} |  {Fore.RED}$${Fore.WHITE} |
  \{Fore.RED}$$$${Fore.WHITE}  |{Fore.RED}$${Fore.WHITE} |{Fore.RED}$${Fore.WHITE} | {Fore.RED}$${Fore.WHITE} | {Fore.RED}$${Fore.WHITE} |\{Fore.RED}$$$$$$${Fore.WHITE}\       {Fore.RED}$$$$$$${Fore.WHITE}  |  \{Fore.RED}$$$${Fore.WHITE}  |\{Fore.RED}$$$$$$${Fore.WHITE} |{Fore.RED}$${Fore.WHITE} | {Fore.RED}$${Fore.WHITE} | {Fore.RED}$${Fore.WHITE} |{Fore.RED}$$$$$$${Fore.WHITE}  |
   \____/ \__|\__| \__| \__| \_______|      \_______/    \____/  \_______|\__| \__| \__|{Fore.RED}$${Fore.WHITE}  ____/ 
                                                                                        {Fore.RED}$${Fore.WHITE} |      
                                                                                        {Fore.RED}$${Fore.WHITE} |      
                                                                                        \__|      
""")
    print(f"{Fore.CYAN}Twitter : {Fore.WHITE}https://twitter.com/legend_of_bugs\n{Fore.CYAN}Instagram : {Fore.WHITE}https://instagram.com/legend.of.bugs\n{Fore.CYAN}Github : {Fore.WHITE}https://github.com/legend-of-bugs")
    print(f"{Fore.WHITE}==========================================================================================")
    print(f"\n{Fore.WHITE}Username/Email :{Fore.RED} {arg.u}")
    print(f"{Fore.WHITE}For {Fore.RED}{arg.s}{Fore.WHITE} Seconds")
banner()

def string_to_md5(my_string):
    m = hashlib.md5()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()

print(f"\n{Fore.YELLOW}Creating word list ...")
timestamps = []
current_time = time.time()
new_time = current_time + int(arg.s)

while current_time <= new_time:
    current_time = time.time()
    timestamps.append(current_time)
    timestamps.append(str(current_time).split(".")[0])

unique_timestamps = list(set(timestamps))
pattern = json.loads(open("pattern.json","r").read())
file_name = f"{arg.u}-{str(time.time()).split('.')[0]}"
output = open(f"export/{file_name}.txt","a")
count = 0
for timest in unique_timestamps:
    for pat in pattern:
        for username in str(arg.u).split(","):
            count += 1
            rep = str(pat).replace("$USERNAME",str(username)).replace("$TIMESTAMP",str(timest))
            md5 = string_to_md5(rep)
            output.write(md5+"\n")
output.close()
print(f"{Fore.GREEN}\n{str(count)}{Fore.WHITE} Hash was created successfully :)")
print(f"Check {Fore.GREEN}export/{file_name}.txt")
