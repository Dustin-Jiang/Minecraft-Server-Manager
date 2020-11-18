#!coding=utf8
import os, sys, json

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
    jsonStr = "";
    for i in configs:
      jsonStr += i;
    configStr = json.loads(jsonStr);
    print(configStr["version"][0])
    
  #Function to Get stdout
  def __command(self, command):
    result = os.popen(commands[command][self.OSver]);
    print(result.read())
    return result.read()
    

if __name__ == "__main__": 
  app = App()