import subprocess
import os

def convert(in_file, out_file):
	cmd = "ffmpeg -i " + in_file +" " + out_file
	subprocess.run(cmd)

in_file = input("Введи файл: ")
base, ext = os.path.splitext(in_file)

if ext == "":
	ext=".webm"
	in_file=base+ext

out_file = base + '.mp4'
convert(in_file, out_file)

input()