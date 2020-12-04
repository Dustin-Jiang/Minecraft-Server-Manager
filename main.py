#!coding=utf8
import os, sys, json
import crossSystem, server

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
    command = self.crossSys.getCommand("cd") + " " + "\"" + path + "\"" +  self.crossSys.getCommand("seperator")
    
    path = "\"" + path + self.crossSys.getCommand("/") + "server.jar" + "\""
    command += self.crossSys.getCommand("runJava") + " " + path
    
    command += " " + "-Xmx " + self.launchOption["max-ram"]
    command += " " + "-Xms " + self.launchOption["min-ram"]
    if self.launchOption["silent"] == True:
      command +=  " " + "-nogui"
      
    self.server = server.Server(command)

if __name__ == "__main__": 
  app = App()
  app.switchServer()