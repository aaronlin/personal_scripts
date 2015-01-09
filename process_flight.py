#!/usr/bin/env python
import subprocess
import os
import argparse
import tempfile


def process_cmd(cmd):
    p = subprocess.Popen(cmd, shell=True)
    p.communicate()


def convert_kml(input_path, output_path):
    tmpfile = tempfile.NamedTemporaryFile()
    cmd = 'gpsbabel -w -r -t -i kml -f %s -o gpx -F %s' % (input_path, tmpfile.name)
    process_cmd(cmd)
    cmd = 'gpsbabel -i gpx -f %s -x interpolate,distance=0.5m -o gpx -F %s' % (tmpfile.name, output_path)
    process_cmd(cmd)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True)
    parser.add_argument('-o', '--output', required = True)

    args = parser.parse_args()
    if not os.path.exists(args.output):
        os.makedirs(args.output)

    for filename in os.listdir(args.input):
        if filename.endswith('kml'):
            input_path = os.path.join(args.input, filename)
            output_path = os.path.join(args.output, '%s.gpx' % filename[:-4])
            convert_kml(input_path, output_path)
