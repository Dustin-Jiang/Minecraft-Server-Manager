import main, os
import UI, server

main = main.App()
server = server.Server()
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
    content = ["Selected: " + main.versionSelected, "Running: " + str(server.running)]
    UIkit.drawContentCenter(content)
    
    UIkit.drawEnter()
    UIkit.drawEnter()

    UIkit.drawCenter("[Options]")
    UIkit.drawEnter()
    content = ["Open/Close Server", "Select server version", "Select world", "Change options"]
    UIkit.radio(content)
    
    choice = UIkit.drawChoices()
    
    if choice == 1:
      self.__switchServer()
    if choice == 2:
      self.__changeVersion()
    if choice == 3:
      self.__changeWorld()
    if choice == 4:
      self.__changeOption()
  
  def __switchServer(self):
    main.switchServer()
    self.__main()

  def __changeVersion(self):
    UIkit = UI.UIkit(width, height)

    UIkit.drawHR()
    UIkit.drawCenter("[Minecraft Server Manager]")
    UIkit.drawHR()
    UIkit.drawEnter()

    UIkit.drawCenter("[Change Server Version]")
    UIkit.drawEnter()

    UIkit.radio(main.version)

    UIkit.drawChoices()

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