import subprocess
p = subprocess.Popen('ls', stdout=subprocess.PIPE)
print(p.communicate())
