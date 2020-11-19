import sys, os

commands = {
  "pwd": {
    "windows": "cd",
    "posix": "pwd"
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