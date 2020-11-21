import main, os
import UI

main = main.App()
width = os.get_terminal_size()[0] - 1
height = os.get_terminal_size()[1]
UIkit = UI.UIkit(width, height)

class Window:
  def __init__(self):
    self.__main()

  def __main(self):
    UIkit = UI.UIkit(width, height)

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
    
    choice = UIkit.drawChoices()
    if choice == 1:
      self.__changeVersion()
    if choice == 2:
      self.__changeWorld()
    if choice == 3:
      self.__changeOption()
  
  def __changeVersion(self):
    UIkit = UI.UIkit(width, height)

    UIkit.drawHR()
    UIkit.drawCenter("[Minecraft Server Manager]")
    UIkit.drawHR()
    UIkit.drawEnter()

    UIkit.drawCenter("[Change Server Version]")

    UIkit.finish()

  def __changeWorld(self):
    UIkit = UI.UIkit(width, height)
    
    UIkit.drawHR()
    UIkit.drawCenter("[Minecraft Server Manager]")
    UIkit.drawHR()
    UIkit.drawEnter()

    UIkit.drawCenter("[Change World]")

    UIkit.finish()

  def __changeOption(self):
    UIkit = UI.UIkit(width, height)
    
    UIkit.drawHR()
    UIkit.drawCenter("[Minecraft Server Manager]")
    UIkit.drawHR()
    UIkit.drawEnter()

    UIkit.drawCenter("[Change Options]")

    UIkit.finish()
    
if __name__ == "__main__":
  app = Window()