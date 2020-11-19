import main, os
import UI

main = main.App()
UIkit = UI.UIkit(width = os.get_terminal_size()[0] - 1, height = os.get_terminal_size()[1])

class Window:
  def __init__(self):
    self.__main()

  def __main(self):
    UIkit.drawHR()
    UIkit.drawCenter("[Minecraft Server Manager]")
    UIkit.drawHR()
    UIkit.drawEnter()
    UIkit.drawCenter("[Status]")
    
    #content = ["Selected: 1.12.2", "Running: True"]
    #UIkit.drawContentCenter(content)
    UIkit.drawEnter()
    UIkit.drawCenter("Version: 1.12.2")
    UIkit.drawCenter("World: Server World")
    
    UIkit.drawEnter()
    UIkit.drawEnter()
    
    UIkit.drawCenter("[Options]")
    UIkit.drawEnter()
    UIkit.drawCenter("1. Select server version")
    UIkit.drawCenter("2. Select world")
    UIkit.drawCenter("3. Change options")
    
    UIkit.finish()
    
    
    
if __name__ == "__main__":
  app = Window()