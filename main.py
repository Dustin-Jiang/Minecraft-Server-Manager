#!coding=utf8
import os, sys

commands = {
  "pwd": {
    "windows": "cd",
    "posix": "pwd"
   }
}

class App:
  def __init__(self):
    #Get System Version (windows/posix)
    if 'win' in sys.platform:
      self.OSver = 'windows'
    else: 
      self.OSver = 'posix'
    #Get WorkDir
    self.workDir = self.__command("pwd")
    #Deal with config
    self.configFile = open("./config.json", mode="r", encoding="utf8")
    configs = self.configFile.readlines();
    print(configs)
    print(self.OSver)
    
  #Function to Get stdout
  def __command(self, command):
    result = os.popen(commands[command][self.OSver]);
    print(result.read())
    return result.read()
    

if __name__ == "__main__": 
  app = App()