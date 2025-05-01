#!/bin/bash

USER=epsonweb
HOME_DIR="/home/$USER"

echo "Installing pjHack for user: $USER"

# 1. Install wlr-randr
echo "Installing wlr-randr..."
apt update && apt install -y wlr-randr

# 2. Create PiVideoPlay.py
echo "Creating PiVideoPlay.py..."
cat << 'EOF' > "$HOME_DIR/PiVideoPlay.py"
#!/usr/bin/env python3
import os 
import time

video_path = "/home/epsonweb/Videos/Movie.mp4"

# Turn HDMI on
os.system('wlr-randr --output HDMI-A-1 --on')
time.sleep(0.25)  # give display time to settle

# Play video
os.system(f'ffplay -fs -autoexit "{video_path}"')

# Wait and turn HDMI off
time.sleep(0.25)
os.system('wlr-randr --output HDMI-A-1 --off')
EOF

chmod +x "$HOME_DIR/PiVideoPlay.py"
chown $USER:$USER "$HOME_DIR/PiVideoPlay.py"

# 3. Create turn_off_hdmi.py
echo "Creating turn_off_hdmi.py..."
cat << 'EOF' > "$HOME_DIR/turn_off_hdmi.py"
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

chmod +x "$HOME_DIR/turn_off_hdmi.py"
chown $USER:$USER "$HOME_DIR/turn_off_hdmi.py"

# 4. Create turn_on_hdmi.py
echo "Creating turn_on_hdmi.py..."
cat << 'EOF' > "$HOME_DIR/turn_on_hdmi.py"
#!/usr/bin/env python3
import subprocess

def turn_on_hdmi():
    try:
        subprocess.run(['wlr-randr', '--output', 'HDMI-A-1', '--on'], check=True)
    except Exception as e:
        print(f"Failed to turn on HDMI: {e}")

if __name__ == '__main__':
    turn_on_hdmi()
EOF

chmod +x "$HOME_DIR/turn_on_hdmi.py"
chown $USER:$USER "$HOME_DIR/turn_on_hdmi.py"

# 5. Create systemd user service
echo "Creating user systemd service..."
sudo -u $USER mkdir -p "$HOME_DIR/.config/systemd/user"

cat << EOF > "$HOME_DIR/.config/systemd/user/turnoffhdmi.service"
[Unit]
Description=Turn off HDMI after desktop login
After=graphical-session.target

[Service]
Type=oneshot
ExecStart=/usr/bin/python3 $HOME_DIR/turn_off_hdmi.py

[Install]
WantedBy=default.target
EOF

chown $USER:$USER "$HOME_DIR/.config/systemd/user/turnoffhdmi.service"

# 6. Enable linger and auto-enable user service on next login
echo "Preparing to enable user service at next login..."
loginctl enable-linger $USER

cat << 'EOF' >> "$HOME_DIR/.bash_profile"
# Enable HDMI turn-off service on first login
if ! systemctl --user is-enabled turnoffhdmi.service >/dev/null 2>&1; then
  systemctl --user daemon-reexec
  systemctl --user daemon-reload
  systemctl --user enable turnoffhdmi.service
fi
EOF

chown $USER:$USER "$HOME_DIR/.bash_profile"

echo "pjHack installed. Log in once as $USER, then reboot. HDMI will turn off after startup."
