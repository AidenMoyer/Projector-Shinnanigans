import pypjlink
import paramiko
import time

# File Directory
# "D:\Projector\HighjackAll.py"

# List of projectors with their IPs and passwords (adjust to projectors' IPs and passwords)
projectors = [
    {'pj-ip': '192.168.1.229', 'pj-password': 'password', 'Name': '', 'Teacher': 'Aiden', 'Power': '', 'pi-username': 'epsonweb', 'pi-password': 'admin', 'pi-hostname': 'raspberrypi001.local'},
    {'pj-ip': '192.168.1.240', 'pj-password': 'password', 'Name': '', 'Teacher': 'Jace', 'Power': '', 'pi-username': 'epsonweb', 'pi-password': 'admin', 'pi-hostname': '192.168.1.202'}, 
     #{'pj-ip': '10.10.20.37', 'pj-password': 'password', 'Name': '', 'Teacher': 'Robotics', 'Power': '', 'pi-username': 'epsonweb', 'pi-password': 'admin', 'pi-hostname': ''},
    #  {'pj-ip': '10.10.20.40', 'pj-password': 'password', 'Name': '', 'Teacher': 'Welch', 'Power': '', 'pi-username': 'epsonweb', 'pi-password': 'admin', 'pi-hostname': ''},
    #  {'pj-ip': '10.10.20.59', 'pj-password': 'password', 'Name': '', 'Teacher': 'Media Center', 'Power': '', 'pi-username': 'epsonweb', 'pi-password': 'admin', 'pi-hostname': ''}, #Left Wall
    #  {'pj-ip': '10.10.20.20', 'pj-password': 'password', 'Name': '', 'Teacher': 'Shizler', 'Power': '', 'pi-username': 'epsonweb', 'pi-password': 'admin', 'pi-hostname': ''}, 
    #  {'pj-ip': '10.10.20.21', 'pj-password': 'password', 'Name': '', 'Teacher': 'Sensory Room', 'Power': '', 'pi-username': 'epsonweb', 'pi-password': 'admin', 'pi-hostname': ''}, 
    #  {'pj-ip': '10.10.20.22', 'pj-password': 'password', 'Name': '', 'Teacher': 'Green', 'Power': '', 'pi-username': 'epsonweb', 'pi-password': 'admin', 'pi-hostname': ''},
    #  {'pj-ip': '10.10.20.23', 'pj-password': 'password', 'Name': '', 'Teacher': 'Neimith', 'Power': '', 'pi-username': 'epsonweb', 'pi-password': 'admin', 'pi-hostname': ''},
    #  {'pj-ip': '10.10.20.24', 'pj-password': 'password', 'Name': '', 'Teacher': 'Brown', 'Power': '', 'pi-username': 'epsonweb', 'pi-password': 'admin', 'pi-hostname': ''},
    #  {'pj-ip': '10.10.20.25', 'pj-password': 'password', 'Name': '', 'Teacher': 'Stanbaugh', 'Power': '', 'pi-username': 'epsonweb', 'pi-password': 'admin', 'pi-hostname': ''},
    #  {'pj-ip': '10.10.20.28', 'pj-password': 'password', 'Name': '', 'Teacher': '', 'Power': '', 'pi-username': 'epsonweb', 'pi-password': 'admin', 'pi-hostname': ''},
    #  {'pj-ip': '10.10.20.29', 'pj-password': 'password', 'Name': '', 'Teacher': '', 'Power': '', 'pi-username': 'epsonweb', 'pi-password': 'admin', 'pi-hostname': ''},
    #  {'pj-ip': '10.10.20.30', 'pj-password': 'password', 'Name': '', 'Teacher': '', 'Power': '', 'pi-username': 'epsonweb', 'pi-password': 'admin', 'pi-hostname': ''},
    #  {'pj-ip': '10.10.20.31', 'pj-password': 'password', 'Name': '', 'Teacher': '', 'Power': '', 'pi-username': 'epsonweb', 'pi-password': 'admin', 'pi-hostname': ''},
    #  {'pj-ip': '10.10.20.32', 'pj-password': 'password', 'Name': '', 'Teacher': 'Nugent', 'Power': '', 'pi-username': 'epsonweb', 'pi-password': 'admin', 'pi-hostname': ''},
    #  {'pj-ip': '10.10.20.33', 'pj-password': 'password', 'Name': '', 'Teacher': '', 'Power': '', 'pi-username': 'epsonweb', 'pi-password': 'admin', 'pi-hostname': ''},
]

#   Creates timer for spacing between commands
def timer(length):

    currentTime = 0
    print(f"Setting {length}sec timer")

    while currentTime < length:

        time.sleep(1)
        currentTime = currentTime + 1
    print(f"Timer Complete")

