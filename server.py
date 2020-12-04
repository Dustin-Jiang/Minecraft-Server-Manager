import crossSystem
import os, threading

class Server:
  def __init__(self, command):
    self.crossSys = crossSystem.CrossSys()
    self.running = False
    self.command = command
  
  def run(self):
    if self.running:
      proc = threading.Thread(target=self.closeServer)
      proc.start()
      proc.join()
    else:
      self.openServer()
    
  def openServer(self):
    print(self.command)
    
if __name__ == "__main__":
  server = Server()