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
    configFile = open("./config.json", mode="r", encoding="utf8")
    configs = configFile.readlines()
    jsonStr = "";
    for i in configs:
      jsonStr += i;
    configStr = json.loads(jsonStr)
    self.version = configStr["version"][0]
    self.launchOption = {}
    if configStr["launch_option"]["silent"] = "true":
      self.launchOption["silent"] = True
    else:
      self.launchOption["silent"] = False
    self.launchOption["max-ram"] = configStr["launch_option"]["max-ram"]
    self.launchOption["min-ram"] = configStr["launch_option"]["min-ram"]
    configFile.close()
    
    return self
    
  #Function to Get stdout
  def __command(self, command):
    result = os.popen(commands[command][self.OSver]);
    print(result.read())
    return result.read()
    

if __name__ == "__main__": 
  app = App()