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
    UIkit.drawEnter()
    content = ["Selected: 1.12.2", "Running: True"]
    UIkit.drawContentCenter(content)
    
    UIkit.drawEnter()
    UIkit.drawEnter()

    UIkit.drawCenter("[Options]")
    UIkit.drawEnter()
    content = ["Select server version", "Select world", "Change options"]
    UIkit.radio(content)
    
    UIkit.drawChoices()   
    
if __name__ == "__main__":
  app = Window()