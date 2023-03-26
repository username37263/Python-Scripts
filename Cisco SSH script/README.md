This script pulls info from an excel sheet the script is look for test.xlsx if your file has a differnt name you mush edit the script. Line 17
The excel must have Type colum with ip address but it will find them 

How the script works:

Step 1) The user is requested to input:
Kind - the type of device ie L3 switch, router, or switch
User - username for ssh
Pass - password for ssh

Step 2) The script will then search the excel file for all devices that match the Kind and save the row

Step 3) The script pulls the ip address from the saved information from setp 2

Step 4) The script uses the list of ip address to ssh and excute a list of commands. It then save the commands in differnt txt files pre device

See examples folder for examples of my outputs
