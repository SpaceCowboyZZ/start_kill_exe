import subprocess, time

process = subprocess.Popen(['YOUR_EXE_PATH_HERE'])

time.sleep(3)

process.terminate()

process.wait()