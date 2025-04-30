import pypjlink

# File Directory
# "D:\Projector\ManyProjectors.py"

# List of projectors with their IPs and passwords (adjust to your projectors' IPs and passwords)
projectors = [
     {'ip': '192.168.1.229', 'password': 'password', 'Name': 'Aiden Projector'},
     #{'ip': '10.10.20.37', 'password': 'password', 'Name': 'Robotics'},
     #{'ip': '192.168.1.240', 'password': 'password', 'Name': 'Jace Projector'}, 
    # {'ip': '10.10.20.40', 'password': 'password'} #Welch Projector
    # {'ip': '10.10.20.59', 'password': 'password'} #Media Center 

    
]

def prompt():

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

    elif x =="4":
        print(f"Adios")
    
    else: 
        prompt()



def power():
    print(f"Projector is:  {pj.get_power()}")
    print(f"1. Turn Off")
    print(f"2. Turn On")
    print(f"3. EXIT")

    x = input()
    if x == "1":
        pj.set_power('off')
        prompt()
        
    elif x == "2":
        pj.set_power('on')
        prompt()

    elif x == "3": 
        prompt()

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
    
    elif x == "2":
        pj.set_mute("all", False)
    
    elif x == "3":
        prompt()

    else:
        mute()

def network():
    print(f"Current Input: {pj.get_input()}")
    print(f"Network Options: {pj.get_inputs()}")
    print(f"1. RGB 1")
    print(f"2. RGB 2")
    print(f"3. Video")
    print(f"4. Digital 1")
    print(f"5. Digital 2")
    print(f"6. Digital 3")
    print(f"7. Storage")
    print(f"8. Network 1")
    print(f"9. Network 2")
    print(f"10. EXIT")

    x = input()
    if x == "1":
        pj.set_input('RGB', 1)
        prompt()
    
    elif x == "2":
        pj.set_input('RGB', 2)
        prompt()

    elif x == "3":
        pj.set_input('VIDEO', 1)
        prompt()
    
    elif x == "4":
        pj.set_input('DIGITAL', 2)
        prompt()
    
    elif x == "5":
        pj.set_input('DIGITAL', 3)
        prompt()

    elif x == "6":
        pj.set_input('DIGITAL', 6)
        prompt()

    elif x =="7":
        pj.set_input('STORAGE', 1)
        prompt()

    elif x == "8":
        pj.set_input('NETWORK', 2)
        prompt()

    elif x == "9":
        pj.set_input('NETWORK', 3)
        prompt()

    elif x == "10":
        prompt()

    else: 
        network()



# Loop through the list of projectors and send commands
for projector in projectors:
    try:
        # Create a Projector instance for each projector
        pj = pypjlink.Projector.from_address(projector['ip'])
        
        # Set password if required
        if projector['password']:
            pj.authenticate(projector['password'])

        #Adds projector name to projectors array
        projector['Name'] = pj.get_name()
        print(f"{projector['Name']}:")
    
        prompt()

      
    
    except Exception as e:
        print(f"Failed to communicate with projector at {projector['ip']}. Error: {str(e)}")