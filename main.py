#!coding=utf8
import os, sys, json
import crossSystem

class App:
  def __init__(self):
    self.crossSys = crossSystem.CrossSys()
    #Get WorkDir
    self.workDir = self.crossSys.command("pwd")
    self.workDir = self.workDir[0:-1] #Erase \n

    #Deal with config
    fileLocation = self.crossSys.getFileLocation(self.workDir, "config.json")
    configFile = open(fileLocation, mode="r", encoding="utf8")
    configStr = self.crossSys.readJSON(configFile)
    self.version = configStr["version"]
    self.versionSelected = configStr["selected_version"]
    self.launchOption = {}
    if configStr["launch_option"]["silent"] == "true":
      self.launchOption["silent"] = True
    else:
      self.launchOption["silent"] = False
    self.launchOption["max-ram"] = configStr["launch_option"]["max-ram"]
    self.launchOption["min-ram"] = configStr["launch_option"]["min-ram"]

  def switchServer(self):
    version = self.versionSelected
    path = self.crossSys.getFileLocation(self.workDir, version)
    path = self.crossSys.getFileLocation(self.workDir, "server.jar")
    print(path)

if __name__ == "__main__": 
  app = App()
  app.switchServer()