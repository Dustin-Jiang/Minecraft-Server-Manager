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