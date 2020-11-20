import sys, os, json

commands = {
  "pwd": {
    "windows": "cd",
    "posix": "pwd"
   },
   "/": {
    "windows": "\\",
    "posix": "/"
   }
}

class CrossSys:
  def __init__(self):
    #Get System Version (windows/posix)
    if 'win' in sys.platform:
      self.OSver = 'windows'
    else: 
      self.OSver = 'posix'
      
  #Function to Get stdout
  def command(self, command, *vartuple):
    if vartuple != "":
      commandLine = " ";
      commandLine.join(vartuple)
      result = os.popen(commands[command][self.OSver] + " " + commandLine)
    else:
      result = os.popen(commands[command][self.OSver])
    return result.read()
    
  def getFileLocation(self, pwd, filename):
    if self.OSver == "windows":
      return pwd + commands["/"]["windows"] + filename
    else: 
      return pwd + commands["/"]["posix"] + filename
      
  #Read and load JSON
  def readJSON(self, file):
    context = file.readlines()
    jsonStr = "";
    for i in context:
      jsonStr += i;
    contextStr = json.loads(jsonStr)
    file.close()
    return contextStr
   
#Class for getchar() 
class Getch:
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class __GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class __GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()