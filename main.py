#!coding=utf8
import os, sys, json
import crossSystem

class App:
  def __init__(self):
    self.crossSys = crossSystem.CrossSys()
    #Get WorkDir
    self.workDir = self.crossSys.command("pwd")
    self.workDir = self.workDir[0:-1]

    #Deal with config
    fileLocation = self.crossSys.getFileLocation(self.workDir, "config.json")
    fileLocation = self.workDir + "\\" + "config.json"
    configFile = open(fileLocation, mode="r", encoding="utf8")
    configs = configFile.readlines()
    jsonStr = "";
    for i in configs:
      jsonStr += i;
    configStr = json.loads(jsonStr)
    self.version = configStr["version"][0]
    self.launchOption = {}
    if configStr["launch_option"]["silent"] == "true":
      self.launchOption["silent"] = True
    else:
      self.launchOption["silent"] = False
    self.launchOption["max-ram"] = configStr["launch_option"]["max-ram"]
    self.launchOption["min-ram"] = configStr["launch_option"]["min-ram"]
    configFile.close()
    

if __name__ == "__main__": 
  app = App()