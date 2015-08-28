import subprocess


p = subprocess.call("gpsbabel -t -i m241 -f /dev/tty.HOLUX_M-241-SPPSlave -o gpx -F dump.gpx")
p.communicate()
