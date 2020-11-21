import crossSystem

class UIkit:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.counter = 0
  def drawHR(self):
    i = 0
    hr = ""
    while(i < self.width):
      hr += "="
      i += 1
    self.__drawFinish()
    print(hr)
    
  def drawCenter(self, text):
    length = (self.width - len(text)) / 2
    i = 0
    content = ""
    while i < length:
      content += " "
      i += 1
    content += text
    while len(content) < self.width:
      content += " "
    self.__drawFinish()
    print(content)
    
  def drawContentCenter(self, text):
    maxWidth = 0
    content = ""
    
    for i in text:
      if len(i) > maxWidth:
        maxWidth = len(i)
    
    for i in text:
      length = (self.width - maxWidth) / 2
      j = 0
      content = ""
      while j < length:
        content += " "
        j += 1
      content += i
      while len(content) < self.width:
        content += " "
      self.__drawFinish()
      print(content)

  def drawEnter(self):
    print(" ")
    self.__drawFinish()

  def __drawFinish(self):
    self.counter += 1

  def finish(self):
    i = self.counter
    while i < self.height:
      self.drawEnter()
      i += 1
      
class Controlkit(UIkit):
  def __init__(self, obj):
    self.UIkit = obj
    self.allChoices = []
    self.choiceRange = []
  def radio(self, choices):
    i = len(self.allChoices)
    for j in choices:
      i += 1
      text = str(i) + ". "
      self.choiceRange.append(i)
      self.allChoices.append(text + j)
    UIkit.drawContentCenter(self.UIkit,self.allChoices)
    return self.__getKey(self.choiceRange)
    
  def __getKey(self, range):
    while True:
      pressKey = crossSystem.Getch();
      pressKey = pressKey.decode("ascii")
      if int(pressKey) in range:
        return pressKey

if __name__ == "__main__":
  UIkit = UIkit(80,24)
  content = ["Hello", "World!!!"]
  UIkit.drawContentCenter(content)