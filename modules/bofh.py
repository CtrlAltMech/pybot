import urllib2
class Example:
  def __init__(self, events=None, printer_handle=None, bot=None):
    self.events = events
    self.printer = printer_handle
    self.interests = ['__.bofh__']
    for event in events:
      if event._type in self.interests:
	event.subscribe(self)

  def handle(self, event):
    try:
      url = "http://zero9f9.com/api/bofh"
      response = urllib2.urlopen(url)
      text = response.read()
      bofhquote = text.splitlines()[2]
      self.printer("PRIVMSG " + event.channel + " :BOFH: " + bofhquote + '\n')
    except TypeError:
      pass
