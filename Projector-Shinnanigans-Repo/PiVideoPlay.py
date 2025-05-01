import os
import time

video_path = "/home/epsonweb/Videos/Movie.mp4"

# Turn HDMI on
os.system('wlr-randr --output HDMI-A-1 --on')
time.sleep(.25)  # give display time to settle

# Play video
os.system(f'ffplay -fs -autoexit "{video_path}"')

# Wait and turn HDMI off
time.sleep(.25)
os.system('wlr-randr --output HDMI-A-1 --off')
