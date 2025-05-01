import pypjlink
import paramiko
import time

# File Directory
# "D:\Projector\HighjackAll.py"

# Create SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# List of projectors with their IPs and passwords (adjust to projectors' IPs and passwords)
projectors = [
    {'Teacher': 'Aiden', 'Name': '', 'pj_ip': '192.168.1.229', 'pi_hostname': 'raspberrypi001.local'},
    #{'Teacher': 'Jace', 'Name': '', 'pj_ip': '192.168.1.240', 'pi_hostname': 'abbys-iphone.local'},

    # {'Teacher': 'Robotics', 'Name': '', 'pj_ip': '10.10.20.37', 'pi_hostname': ''},

    # {'Teacher': 'Shizler', 'Name': '', 'pj_ip': '10.10.20.20', 'pi_hostname': ''},
    # {'Teacher': 'Green', 'Name': '', 'pj_ip': '10.10.20.22', 'pi_hostname': ''},
    # {'Teacher': 'Neimith', 'Name': '', 'pj_ip': '10.10.20.23', 'pi_hostname': ''},
    # {'Teacher': 'Brown', 'Name': '', 'pj_ip': '10.10.20.24', 'pi_hostname': ''},
    # {'Teacher': 'Stanbaugh', 'Name': '', 'pj_ip': '10.10.20.25', 'pi_hostname': ''},
    # {'Teacher': 'Davids', 'Name': '', 'pj_ip': '10.10.20.28', 'pi_hostname': ''},
    # {'Teacher': 'Fuller', 'Name': '', 'pj_ip': '10.10.20.30', 'pi_hostname': ''},
    # {'Teacher': 'Honz', 'Name': '', 'pj_ip': '10.10.20.31', 'pi_hostname': ''},
    # {'Teacher': 'Nugent', 'Name': '', 'pj_ip': '10.10.20.32', 'pi_hostname': ''},
    # {'Teacher': 'Polasek', 'Name': '', 'pj_ip': '10.10.20.33', 'pi_hostname': ''},
    # {'Teacher': 'Gorzen', 'Name': '', 'pj_ip': '10.10.20.35', 'pi_hostname': ''},
    # {'Teacher': 'DeGroot', 'Name': '', 'pj_ip': '10.10.20.36', 'pi_hostname': ''},
    # {'Teacher': 'Band', 'Name': '', 'pj_ip': '10.10.20.38', 'pi_hostname': ''},
    # {'Teacher': 'Lowe', 'Name': '', 'pj_ip': '10.10.20.39', 'pi_hostname': ''},
    # {'Teacher': 'Welch', 'Name': '', 'pj_ip': '10.10.20.40', 'pi_hostname': ''},
    # {'Teacher': 'Porchic', 'Name': '', 'pj_ip': '10.10.20.41', 'pi_hostname': ''},
    # {'Teacher': 'Davlin', 'Name': '', 'pj_ip': '10.10.20.42', 'pi_hostname': ''},
    # {'Teacher': 'Novara', 'Name': '', 'pj_ip': '10.10.20.43', 'pi_hostname': ''},
    # {'Teacher': 'Brookes', 'Name': '', 'pj_ip': '10.10.20.44', 'pi_hostname': ''},
    # {'Teacher': 'Thorp', 'Name': '', 'pj_ip': '10.10.20.45', 'pi_hostname': ''},
    # {'Teacher': 'Simions', 'Name': '', 'pj_ip': '10.10.20.46', 'pi_hostname': ''},
    # {'Teacher': 'Rockey', 'Name': '', 'pj_ip': '10.10.20.51', 'pi_hostname': ''},
    # {'Teacher': 'Pulling', 'Name': '', 'pj_ip': '10.10.20.52', 'pi_hostname': ''},
    # {'Teacher': 'Bolthouse', 'Name': '', 'pj_ip': '10.10.20.53', 'pi_hostname': ''},
    # {'Teacher': 'McNammera', 'Name': '', 'pj_ip': '10.10.20.54', 'pi_hostname': ''},
    # {'Teacher': 'Kimmil', 'Name': '', 'pj_ip': '10.10.20.55', 'pi_hostname': ''},
    # {'Teacher': 'Pohl', 'Name': '', 'pj_ip': '10.10.20.56', 'pi_hostname': ''},
    # {'Teacher': 'Media Center', 'Name': '', 'pj_ip': '10.10.20.59', 'pi_hostname': ''},

 ]

pj_password = 'password'
pi_username = 'epsonweb'
pi_password = 'admin'

# 2. Loop through each dictionary to:
#    - create the PJLink object
#    - authenticate
#    - attach the PJLink object back into the dictionary
for proj in projectors:
    try:
        pj = pypjlink.Projector.from_address(proj['pj_ip'])  # create PJLink instance
        pj.authenticate(pj_password)              # authenticate password

        proj['pj'] = pj  # store the PJLink object in the dictionary
        proj['Name'] = pj.get_name()
        proj['productName'] = pj.get_product_name()

        print(f"{proj['Name']} Power: {pj.get_power()}")

    except Exception as e:
        projectors.remove(proj)


#   Creates timer for spacing between commands
def timer(length):

    currentTime = 0
    print(f"Setting {length}sec timer")

    while currentTime < length:

        time.sleep(1)
        currentTime = currentTime + 1
    print(f"Timer Complete")

startTime = time.time()
duration = 60 * 60      # Seconds * Minutes = total seconds


# Runs for decided amount of time
while time.time() - startTime <= duration:

    for proj in projectors:
        try:
            if proj['pj'].get_power() == 'on':
                print(proj['Name'])
                print(proj['pj'].get_power())
                

                try:
                    ssh.connect(proj['pi_hostname'], username = pi_username, password = pi_password)
                    print(f'Connected to pi')

                    stdin, stdout, stderr = ssh.exec_command("ps aux | grep ffplay | grep -v grep")
                    output = stdout.read().decode().strip()

                    if output:
                        print("Movie is playing!")
                        
                        # If statment to see what type of projector to determin what source to set
                        if proj['productName'] == 'EPSON 595':

                            proj['pj'].set_input('DIGITAL', 3)

                        elif proj['productName'] == 'EB/PL-475Wi/475WT/CU600Wi':

                            proj['pj'].set_input('DIGITAL', 2)
                        
                    else:
                       
                        print("Starting Video")
                        ssh.exec_command("DISPLAY=:0 python3 /home/epsonweb/PiVideoPlay.py")

                finally:
                    ssh.close()

            else:
                print(proj['pj'].get_power())
                proj['pj'].set_power('on')

        
        except Exception as e:
            print(proj['Name'])
            print(e)

        print(f" ")

    timer(20)          