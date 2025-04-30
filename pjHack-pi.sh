#!/bin/bash

USER=orangepi
HOME_DIR="/home/$USER"

# Step 1: Save HDMI off script
cat << 'EOF' > $HOME_DIR/turn_off_hdmi.py
#!/usr/bin/env python3
import subprocess
import os
import time

# Set display for xrandr
os.environ["DISPLAY"] = ":0"
time.sleep(10)

def turn_off_hdmi():
    try:
        output = subprocess.check_output(['xrandr']).decode()
        for line in output.splitlines():
            if ' connected' in line and 'HDMI' in line:
                display_name = line.split()[0]
                print(f"Turning off display: {display_name}")
                subprocess.run(['xrandr', '--output', display_name, '--off'], check=True)
                print("HDMI output turned off.")
                return
        print("No HDMI display found.")
    except subprocess.CalledProcessError as e:
        print("xrandr command failed:", e)
    except FileNotFoundError:
        print("xrandr not installed or not in PATH.")

if __name__ == '__main__':
    turn_off_hdmi()
EOF

# Step 2: Save PiVideoPlay.py
cat << 'EOF' > $HOME_DIR/PiVideoPlay.py
#!/usr/bin/env python3
import os
video_path = "/home/epsonweb/Videos/Movie.mp4"
os.system(f'ffplay -fs "{video_path}"')
EOF

# Step 3: Make both scripts executable
chmod +x $HOME_DIR/turn_off_hdmi.py
chmod +x $HOME_DIR/PiVideoPlay.py

# Step 4: Create autostart directory
mkdir -p $HOME_DIR/.config/autostart

# Step 5: Create .desktop entry for HDMI-off script
cat << EOF > $HOME_DIR/.config/autostart/turn_off_hdmi.desktop
[Desktop Entry]
Type=Application
Name=Turn Off HDMI
Exec=python3 $HOME_DIR/turn_off_hdmi.py
X-GNOME-Autostart-enabled=true
EOF

# Step 6: Set correct ownership
chown $USER:$USER $HOME_DIR/turn_off_hdmi.py
chown $USER:$USER $HOME_DIR/PiVideoPlay.py
chown $USER:$USER $HOME_DIR/.config/autostart/turn_off_hdmi.desktop

echo "✅ Setup complete:"
echo "  • turn_off_hdmi.py will run at desktop login"
echo "  • PiVideoPlay.py is ready in $HOME_DIR"
