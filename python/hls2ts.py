#!/usr/bin/python2.7
#
# Copyright 2019 Eyevinn Technology. All rights reserved
# Use of this source code is governed by a MIT License
# that can be found in the LICENSE file.
# Author: Jonas Rydholm Birme (Eyevinn Technology)
#
# Pull live HLS and output to multicast TS
#
import argparse
import subprocess
from os.path import basename
import re
import glob

parser = argparse.ArgumentParser(description='Pull live HLS and output to multicast TS')
parser.add_argument('hlsurl')
parser.add_argument('outputaddress')
parser.add_argument('--srt', action='store_true', help='use SRT as transport protocol')
parser.add_argument('--with-debug', dest='debug', action='store_true')
args = parser.parse_args()

outputcoding = '-acodec copy -vcodec copy'

protocol = 'udp'
if args.srt:
  protocol = 'srt'

ffmpeg = "ffmpeg -fflags +genpts -re -i %s -strict -2 -y -f mpegts %s://%s?pkt_size=1316" % (args.hlsurl, protocol, args.outputaddress)

if args.debug:
  print "%s" % ffmpeg
  print ffmpeg.split()

p1 = subprocess.Popen(ffmpeg.split())
output,err = p1.communicate()