import subprocess
import settings
def makeMidi():
   scriptName = 'makeMidi.m';
   cmd = ['matlab', '-nodesktop', '-nosplash', '-nodisplay', '-r' , '"run ./{scriptName}; quit;"'.format(scriptName = scriptName)];
   if settings.DEBUG: print(cmd)
   p = subprocess.Popen(cmd);



