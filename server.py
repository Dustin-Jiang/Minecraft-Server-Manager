import crossSystem
import os, threading

class Server:
  def __init__(self):
    self.crossSys = crossSystem.CrossSys()
    self.running = False
  
  def run(self, command):
    self.command = command
    if self.running:
      proc = threading.Thread(target=self.closeServer)
      proc.start()
      proc.join()
    else:
      self.openServer()
    
  def openServer(self):
    print(self.command)
    self.crossSys.rawCommand(self.command)
  
  def closeServer(self):
    print(self.command)
    
if __name__ == "__main__":
  server = Server()
  server.run("cd")