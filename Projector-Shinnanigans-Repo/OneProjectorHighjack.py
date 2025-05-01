import pypjlink
import paramiko
import time

# File Directory
#   "D:\Projector\OneProjectorHighjack.py"

projectors = [
      {'pj-ip': '192.168.1.229', 'pj-password': 'password', 'Name': '', 'Teacher': 'Aiden', 'Power': '', 'pi-username': 'epsonweb', 'pi-password': 'admin', 'pi-ip': 'raspberrypi002.local'},
      #{'pj-ip': '192.168.1.240', 'pj-password': 'password', 'Name': '', 'Teacher': 'Jace', 'Power': '', 'pi-username': 'epsonweb', 'pi-password': 'admin', 'pi-ip': '192.168.1.202'}, 
]

# Create SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#   Creates timer for spacing between commands
def timer(length):

    currentTime = 0
    print(f"Setting {length}sec timer")

    while currentTime < length:

        time.sleep(1)
        currentTime = currentTime + 1
    print(f"Timer Complete")


# Loop through the list of projectors and send commands
for projector in projectors:
    try:
        # Create a Projector instance for each projector
        pj = pypjlink.Projector.from_address(projector['pj-ip'])
        
        # Set password if required
        if projector['pj-password']:
            pj.authenticate(projector['pj-password'])

        #Adds projector name to projectors array
        projector['Name'] = pj.get_name()
        print(f"{projector['Name']}:")
    
        #Turns the projector on and gets power status
        print(pj.get_power())
        pj.set_power('on')
        print(f'Turning on...')
        timer(20)


        #Checks power status until on
        while True:
            try:
                if pj.get_power() == 'on':
                    break
                else:
                    timer(10)
                    print(f"Projector is:  {pj.get_power()}")

            except Exception as e:
                timer(5)
                # print(f"Projector is:  {pj.get_power()}")

        #Gets then sets then changes the input
        print(f"Current Input: {pj.get_input()}")

        if ('DIGITAL', 3) in pj.get_inputs():
            pj.set_input('DIGITAL', 3)
            print("Switched to HDMI 1.")
        else:
            print("HDMI 1 ('digital', 2) not available. Staying on current input.")

        timer(10)
        print(f"Current Input: {pj.get_input()}")

    
        try:
            print("Connecting to Pi...")
            ssh.connect(projector['pi-ip'], username=projector['pi-username'], password=projector['pi-password'])
            print("Running video script...")
            ssh.exec_command("DISPLAY=:0 python3 /home/epsonweb/PiVideoPlay.py")
            print("Video should now be playing on the Pi.")
        finally:
            ssh.close()

      
    
    except Exception as e:
       print(f"Error: {str(e)}")