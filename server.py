import crossSystem
import os, threading

class Server:
  def __init__(self):
    self.crossSys = crossSystem.CrossSys()
    self.running = False
  
  def run(self, command):
    self.command = command
    if self.running:
      closeServer(proc)
    else:
      proc = threading.Thread(target=self.openServer)
      proc.start()
      proc.join()
      #self.openServer()
    
  def openServer(self):
    self.running = True
    self.crossSys.rawCommand(self.command)
  
  def closeServer(self, proc):
    print(self.command)
    
if __name__ == "__main__":
  server = Server()
  server.run("pause")