import sys, os, json

commands = {
  "pwd": {
    "windows": "cd",
    "posix": "pwd"
  },
  "/": {
    "windows": "\\",
    "posix": "/"
  },
  "runJava": {
    "windows": "java.exe -jar",
    "posix": "java -jar"
  },
  "cd": {
    "windows": "cd",
    "posix": "cd"
  },
  "seperator": {
    "windows": " && ",
    "posix": "; "
  },
  "newConsole": {
    "windows": "start cmd /C \"",
    "posix": "gnome-terminal -x bash -c \""
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
      commandLine = "";
      for i in vartuple:
        commandLine += " "
        commandLine += i
      #print(commands[command][self.OSver] + commandLine)
      result = os.popen(commands[command][self.OSver] + commandLine)
    else:
      result = os.popen(commands[command][self.OSver])
    return result.read()
    
  def getCommand(self, command):
    return commands[command][self.OSver]
    
  def rawCommand(self, command):
    return os.popen(commands["newConsole"][self.OSver] + command + "\"")
    
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
def Getch():
  def _GetchUnix():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
      tty.setraw(sys.stdin.fileno())
      ch = sys.stdin.read(1)
    finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
  def _GetchWindows():
    import msvcrt
    return msvcrt.getch()
  try:
    impl = _GetchWindows()
  except ImportError:
    impl = _GetchUnix()
  return impl
  
if __name__ == "__main__":
  crossSys = CrossSys()
  crossSys.command("runJava", r"C:\Users\Administrator\Programming\MCServerManager\1.12.2\server.jar","-Xmx=" + "512M", "-Xms="+"256M")