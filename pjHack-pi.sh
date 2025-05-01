#!/bin/bash

USER=epsonweb
HOME_DIR="/home/$USER"

echo "Installing pjHack for user: $USER"

# Step 1: Install wlr-randr
echo "Installing wlr-randr..."
apt update && apt install -y wlr-randr

# Step 2: Create PiVideoPlay.py
echo "Creating PiVideoPlay.py..."
cat << 'EOF' > $HOME_DIR/PiVideoPlay.py
#!/usr/bin/env python3
import os
video_path = "/home/epsonweb/Videos/Movie.mp4"
os.system(f'ffplay -fs "{video_path}"')
EOF

chmod +x $HOME_DIR/PiVideoPlay.py
chown $USER:$USER $HOME_DIR/PiVideoPlay.py

# Step 3: Create turn_off_hdmi.py
echo "Creating turn_off_hdmi.py..."
cat << 'EOF' > $HOME_DIR/turn_off_hdmi.py
#!/usr/bin/env python3
import subprocess
import time

time.sleep(5)

def turn_off_hdmi():
    try:
        subprocess.run(['wlr-randr', '--output', 'HDMI-A-1', '--off'], check=True)
    except Exception as e:
        print(f"Failed to turn off HDMI: {e}")

if __name__ == '__main__':
    turn_off_hdmi()
EOF

chmod +x $HOME_DIR/turn_off_hdmi.py
chown $USER:$USER $HOME_DIR/turn_off_hdmi.py

# Step 4: Create systemd service
echo "Creating systemd service..."
cat << EOF > /etc/systemd/system/turnoffhdmi.service
[Unit]
Description=Turn off HDMI using wlr-randr
After=multi-user.target

[Service]
Type=oneshot
ExecStart=/usr/bin/python3 $HOME_DIR/turn_off_hdmi.py
RemainAfterExit=true

[Install]
WantedBy=multi-user.target
EOF

# Step 5: Enable service
systemctl daemon-reexec
systemctl daemon-reload
systemctl enable turnoffhdmi.service

echo "pjHack install complete. Reboot to test HDMI auto-off."
