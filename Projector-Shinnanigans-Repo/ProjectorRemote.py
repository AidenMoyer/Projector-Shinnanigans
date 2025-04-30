import pypjlink
import time
import pypjlink.projector

pypjlink.projector.SOURCE_TYPES['digital'] = '3'
pypjlink.projector.SOURCE_TYPES_REV['3'] = 'digital'

# File Directory
# "D:\Projector\ProjectorRemote.py"

# List of projectors with their IPs and passwords (adjust to your projectors' IPs and passwords)
projectors = [
      {'ip': '192.168.1.229', 'password': 'password', 'Name': '', 'Teacher': 'Aiden', 'Power': ''},
     #{'ip': '10.10.20.37', 'password': 'password', 'Name': '', 'Teacher': 'Robotics', 'Power': ''},
      {'ip': '192.168.1.240', 'password': 'password', 'Name': '', 'Teacher': 'Jace', 'Power': ''}, 
    #  {'ip': '10.10.20.40', 'password': 'password', 'Name': '', 'Teacher': 'Welch', 'Power': ''},
    #  {'ip': '10.10.20.59', 'password': 'password', 'Name': '', 'Teacher': 'Media Center', 'Power': ''}, #Left Wall
    #  {'ip': '10.10.20.20', 'password': 'password', 'Name': '', 'Teacher': 'Shizler', 'Power': ''}, 
    #  {'ip': '10.10.20.21', 'password': 'password', 'Name': '', 'Teacher': 'Sensory Room', 'Power': ''}, 
    #  {'ip': '10.10.20.22', 'password': 'password', 'Name': '', 'Teacher': 'Green', 'Power': ''},
    #  {'ip': '10.10.20.23', 'password': 'password', 'Name': '', 'Teacher': 'Neimith', 'Power': ''},
    #  {'ip': '10.10.20.24', 'password': 'password', 'Name': '', 'Teacher': 'Brown', 'Power': ''},
    #  {'ip': '10.10.20.25', 'password': 'password', 'Name': '', 'Teacher': 'Stanbaugh', 'Power': ''},
    #  {'ip': '10.10.20.28', 'password': 'password', 'Name': '', 'Teacher': '', 'Power': ''},
    #  {'ip': '10.10.20.29', 'password': 'password', 'Name': '', 'Teacher': '', 'Power': ''},
    #  {'ip': '10.10.20.30', 'password': 'password', 'Name': '', 'Teacher': '', 'Power': ''},
    #  {'ip': '10.10.20.31', 'password': 'password', 'Name': '', 'Teacher': '', 'Power': ''},
    #  {'ip': '10.10.20.32', 'password': 'password', 'Name': '', 'Teacher': 'Nugent', 'Power': ''},
    #  {'ip': '10.10.20.33', 'password': 'password', 'Name': '', 'Teacher': '', 'Power': ''},
]

#   Creates timer for spacing between commands
def timer(length):

    currentTime = 0
    print(f"Setting {length}sec timer")

    while currentTime < length:

        time.sleep(1)
        currentTime = currentTime + 1
    print(f"Timer Complete")


def remote():

    # Check power status
    status = pj.get_power()
    print(f"Power: {'ON' if status == 'on' else 'OFF'}")

    print(f"What would you like to edit: ")
    print(f"1. Power")
    print(f"2. Mute")
    print(f"3. Input")
    print(f"4. EXIT")

    x = input()
    if x == "1":
        power()

    elif x == "2":
        mute()

    elif x == "3":
        network()

    elif x == "4":
        print(f"Adios")
    
    else: 
        remote()



def power():
    print(f"Projector is:  {pj.get_power()}")
    print(f"1. Turn Off")
    print(f"2. Turn On")
    print(f"3. EXIT")

    x = input()
    if x == "1":
        pj.set_power('off')
        remote()
        
    elif x == "2":
        pj.set_power('on')

    elif x == "3": 
        remote()

    else:
        power()

def mute():
    print(f"Projector is: {pj.get_mute()}")
    print(f"1. Mute")
    print(f"2. Unmute")
    print(f"3. EXIT")

    x = input()
    if x == "1":
        pj.set_mute("all", True)
        timer(5)
        remote()
    
    elif x == "2":
        pj.set_mute("all", False)
        timer(5)
        remote()
    
    elif x == "3":
        remote()

    else:
        mute()

def network():
    #print(pj.get_inputs())
    print(f"Current Input: {pj.get_input()}")
    print(f"1. RGB 1")
    print(f"2. RGB 2")
    print(f"3. Video")
    print(f"4. Digital 1")
    print(f"5. Digital 2")
    print(f"6. Digital 3 DON'T USE")
    print(f"7. Storage")
    print(f"8. Network 1")
    print(f"9. Network 2")
    print(f"10. EXIT")

    x = input()
    if x == "1":
        pj.set_input('RGB', 1)
        timer(5)
        remote()
    
    elif x == "2":
        pj.set_input('RGB', 2)
        timer(5)
        remote()

    elif x == "3":
        pj.set_input('VIDEO', 1)
        timer(5)
        remote()
    
    elif x == "4":
        pj.set_input('digital', 2)
        timer(5)
        remote()
    
    elif x == "5":
        pj.set_input('digital', 3)
        timer(5)
        remote()

    elif x == "6":
        pj.set_input('digital', 3)
        timer(5)
        remote()

    elif x =="7":
        pj.set_input('STORAGE', 1)
        timer(5)
        remote()

    elif x == "8":
        pj.set_input('NETWORK', 2)
        timer(5)
        remote()

    elif x == "9":
        pj.set_input('NETWORK', 3)
        timer(5)
        remote()

    elif x == "10":
        remote()

    else: 
        network()



# Prompt what projector to control
print(f"What Projector would you like to control: ")
projectorInLoop = 0

# Loop through the list of projectors
while projectorInLoop < len(projectors):
    try:
          # Create a Projector instance for given projector
        pj = pypjlink.Projector.from_address(projectors[projectorInLoop]['ip'])
        pj.authenticate(projectors[projectorInLoop]['password'])

        # Sets name and power to projector
        projectors[projectorInLoop]['Name'] = pj.get_name()
        projectors[projectorInLoop]['Power'] = pj.get_power()

        print(f"{projectorInLoop + 1}. {projectors[projectorInLoop]}")


        projectorInLoop += 1
    
    except Exception as e: 
        print(f"{projectorInLoop + 1}. {projectors[projectorInLoop]} MISSING")
        projectorInLoop += 1

print(f"{len(projectors) + 1}. EXIT")
inputedProjector = input()
inputedProjector = int(inputedProjector)
inputedProjector = inputedProjector - 1


# Checks to see if you want to EXIT
if inputedProjector == (len(projectors)):
    print("Adios")

else: 
     # Create a Projector instance for given projector
    pj = pypjlink.Projector.from_address(projectors[inputedProjector]['ip'])

    # Set password if required
    pj.authenticate(projectors[inputedProjector]['password'])

    print(projectors[inputedProjector])

    remote()