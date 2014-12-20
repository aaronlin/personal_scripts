import subprocess
import os
import argparse


def get_cmd(functionality, input_path, output_path):
    if functionality == 'convert_kml':
        cmd = 'gpsbabel -w -r -t -i kml -f %s -o gpx -F %s' % (input_path, output_path)
    elif functionality == 'interpolate_gps':
        cmd = 'gpsbabel -i gpx -f %s -x interpolate,distance=0.5m -o gpx -F %s' % (input_path, output_path)
    else:
        assert 0
    return cmd


def check_filetype(functionality, filename):
    result = False
    if functionality == 'convert_kml' and filename.endswith('kml'):
        result = True
    if functionality == 'interpolate_gps' and filename.endswith('gps'):
        result = True
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True)
    parser.add_argument('-o', '--output', required = True)
    parser.add_argument('-f', '--functionality', required = True)

    args = parser.parse_args()
    if not os.path.exists(args.output):
        os.makedirs(args.output)

    for filename in os.listdir(args.input):
        if check_filetype(args.functionality, filename):
            input_path = os.path.join(args.input, filename)
            output_path = os.path.join(args.output, filename)
            cmd = get_cmd(args.functionality, input_path, output_path)
            subprocess.Popen(cmd, shell=True)
