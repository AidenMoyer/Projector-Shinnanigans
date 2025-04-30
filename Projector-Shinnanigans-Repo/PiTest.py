import paramiko

# File Directory
#   "D:\Projector\PiTest.py"

# Connection details
pi_ip = "192.168.1.202"
pi_user = "epsonweb"
pi_password = "admin"
remote_command = "DISPLAY=:0 python3 /home/epsonweb/PiVideoPlay.py"

# Create SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    print("Connecting to Pi...")
    ssh.connect(pi_ip, username=pi_user, password=pi_password)
    print("Running video script...")
    ssh.exec_command(remote_command)
    print("Video should now be playing on the Pi.")
finally:
    ssh.close()
