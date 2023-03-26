import pandas as pd
from getpass import getpass
import re
from netmiko import ConnectHandler
import subprocess


#Gather some inputs from user.
Kind = input("What type of devices? [L3 Switch, Router, Switch]: ")
User = input("Username: ")
Pass = getpass("Password: ")
#Make sure user inputs are filled out. Then parse the excel sheet.
if ((Kind=="") or (User=="") or (Pass=="")):
    print("Make sure you filled the info out")
    exit
else:
    df = pd.read_excel("test.xlsx") #Pull info from excel sheet
    df_abc = df[df["Type"] == Kind]
    for row in df_abc.iterrows():
        pass
string = df_abc.to_string(index=False)
ips = []
regex = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b',string)
if regex is not None:
    for match in regex:
        if match not in ips:
           ips.append(match)
#Convert list to string
switch = ' '.join(str(x) for x in ips)
#########################################################################
#########################################################################
#########################################################################
#Get windows username
def Username():
    Posistion_Counter = 0
    Result = subprocess.getoutput("whoami")
    for words in Result:
        if words == "\\":
            Position = Posistion_Counter
            break
        Posistion_Counter +=1
    return Result[Position + 1: ]
Local_Coumpter_Username = Username()

for switch in ips:
    Network_Device = {
                      "host": switch,
                      "username": User,
                      "password": Pass,
                      "device_type": "cisco_ios",
                     }
    Connect_to_Device = ConnectHandler(**Network_Device)
    Connect_to_Device.enable()
    List_of_Commands = [
                        "sh ver",
                        "sh vlan brief",
                        "sh ip route",
                        "sh environment",
                        "sh cdp neighbors",
                        "sh ip route ospf",
                        ]
    for command in List_of_Commands:
        output = Connect_to_Device.send_command(command)
        
        with open("C:\\Users\\" +Local_Coumpter_Username+ "\\Desktop\\"+switch+".txt", "a")as f:
            f.write("\n")
            f.write(switch + "#" + command)
            f.write("\n")
            f.write(Connect_to_Device.send_command(command))
            f.write("\n")
            f.close()