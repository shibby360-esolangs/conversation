#file
f = open('examples/repeatedinputs.talk')#put antoehr file here
lines = f.readlines()
if not f.name.endswith('.talk'):
  print('Cannot interpret file.')
  exit()

#actual code
import os
import random as r
import pygame as GUI
from pygame.locals import *
import time
from replit import db
import re
GUI.init()
os.system('clear')
def __():
  pass
def show_text(screen, msg, x, y, color, size=20):
  GUI.font.init()
  font = GUI.font.SysFont('monospace', size)
  text = font.render(msg, True, color)
  screen.blit(text, (x, y))
def pyg_ask(screen, question, x, y, end_to_do=__):
  up = {
    '`':'~',
    '1':'!',
    '2':'@',
    '3':'#',
    '4':'$',
    '5':'%',
    '6':'^',
    '7':'&',
    '8':'*',
    '9':'(',
    '0':')',
    '-':'_',
    '=':'+',
    '[':'{',
    ']':'}',
    '\\':'|',
    ';':':',
    "'":'"',
    ',':'<',
    '.':'>',
    '/':'?'
  }
  answer = ''
  upper = False
  breaker = False
  cursor = False
  while True:
    time.sleep(1)
    if breaker:
      end_to_do()
      GUI.window.update()
      break
    screen.fill((0, 0, 0))
    show_text(screen, question, x, y, (255, 255, 255))
    show_text(screen, answer, x, y+32, (255, 255, 255))
    if cursor:
      GUI.font.init()
      font = GUI.font.SysFont('freesans', 20)
      text = font.render('|', True, (167, 167, 167))
      screen.blit(text, (len(answer) * 12, y+32))
    GUI.window.update()
    for event in GUI.event.get():
      if event.type == QUIT:
        GUI.quit()
        exit()
      if event.type == KEYDOWN:
        if event.key == K_RETURN:
          breaker = True
        elif event.key == K_BACKSPACE:
          listed = list(answer)
          try:
            listed[-1] = ''
          except IndexError:
            pass
          answer = ''.join(listed)
        elif 'shift' in GUI.key.name(event.key):
          upper = True
        elif event.key == K_SPACE:
          answer += ' '
        elif len(GUI.key.name(event.key)) > 1:
          pass
        else:
          if upper:
            if GUI.key.name(event.key) in up:
              answer += up[GUI.key.name(event.key)]
            else:
              answer += GUI.key.name(event.key).capitalize()
            upper = False
          else:
            answer += GUI.key.name(event.key)
        screen.fill((0, 0, 0))
        show_text(screen, question, x, y, (255, 255, 255))
        show_text(screen, answer, x, y+32, (255, 255, 255))
        GUI.window.update()
    if cursor:
      cursor = False
    else:
      cursor = True
  return answer
setattr(GUI.draw, 'text', show_text)
setattr(GUI.display, 'input', pyg_ask)
setattr(GUI, 'create_window', GUI.display.set_mode)
del GUI.display.set_mode
setattr(GUI, 'set_title', GUI.display.set_caption)
del GUI.display.set_caption
setattr(GUI, 'window', GUI.display)
del GUI.display
setattr(GUI, 'sounds', GUI.mixer)
del GUI.mixer
yes = True
no = False
neither = None
opers = {
  '==':'!=',
  '>=':'<',
  '<=':'>',
  '!=':'==',
  '<':'>=',
  '>':'<=',
  'in':'not in',
  'not in':'in',
  'True':'False',
  'False':'True'
}
#Data Types
class number(int):
  def __init__(self, x):
    return x.__num__()
  def digits(self):
    return len(str(self))
  __doc__ = """
  number(x) --> x.__num__()
  Create a new number.
  Return x.__num__()
  """
sentence = type('sentence', str.__bases__, dict(str.__dict__))
decimal = type('decimal', float.__bases__, dict(float.__dict__))
letter = type('letter', str.__bases__, dict(str.__dict__))
#Nvm
if 'nevermind\n' in lines or 'nevermind' in lines:
  if lines[len(lines)-1] == 'nevermind\n' or lines[len(lines)-1] == 'nevermind':
    lines = []
  else:
    readit = f.read()
    for i in range(len(lines)):
      lines[i] = lines[i].strip()
    readit = readit.split('nevermind')
    for j in range(len(readit)-2):
      lines.remove(readit[j])
#Errors
class ConversationError(Exception):
  pass
class UnknownNameError(Exception):
  pass
class ConversationUnexpectedlyEndedError(Exception):
  pass
class UnexpectedConversationLineEndedError(Exception):
  pass
#Classes
class shell:
  def do_it(command):
    os.system(command)
class math:
  def round_to_whole(item):
    return round(item)
  def round_to_nearest(item, nearest):
    return round(item/nearest) * nearest
  def random_num(start, stop):
    return r.randint(start, stop)
class builtin_class():
  def __init__(self):
    pass
  def setInfo(self, info):
    self.__doc__ = info
  def __str__(self):
    return str(self)
setattr(builtin_class, '__vars__', dict(builtin_class.__dict__))
del builtin_class.__vars__['__module__']
del builtin_class.__vars__['__init__']
del builtin_class.__vars__['__str__']
del builtin_class.__vars__['__dict__']
del builtin_class.__vars__['__weakref__']
del builtin_class.__vars__['setInfo']
os.environ['TZ'] = 'US/Pacific'
time.tzset()
class timer:
  class ctime:
    def what_year(timeat=time.time()):
      return time.ctime(timeat)[-4:]
    def what_seconds(timeat=time.time()):
      return time.ctime(timeat)[17:19]
    def what_hour(timeat=time.time()):
      return time.ctime(timeat)[15:16]
    def what_mins(timeat=time.time()):
      return time.ctime(timeat)[14:16]
    def what_day_num(timeat=time.time()):
      return time.ctime(timeat)[9:10]
    def what_month(timeat=time.time()):
      return time.ctime(timeat)[5:9]
    def what_day(timeat=time.time()):
      return time.ctime(timeat)[:2]
  wait = time.sleep
  class logging:
    loggedtime = 0
    def logtime():
      global loggedtime
      loggedtime = time.time()
    def timepassedsincelog():
      return time.time() - loggedtime
#Functions
def say(str='', end='\n'):
  print(str, end=end)
def ask(str):
  return input(str)
def file(the_file, mode='r'):
  return open(the_file, mode)
def do_it(source):
  exec(source)
def bye():
  exit()
def info(item):
  print(item.__doc__)
def num_items(obj):
  return len(obj)
def get_parity(item):
  if item % 2 == 0:
    return 'even'
  else:
    return 'odd'
def from_to(fromm, to, step=1):
  return range(fromm, to, step)
def what_type(item):
  if type(item) == str:
    if len(item) == 1:
      return letter
    else:
      return sentence
  elif type(item) == int:
    return number
  elif type(item) == float:
    return decimal
  else:
    return type(item)
def think(**thoughts):
  if 'key' in thoughts:
    db[thoughts['key']] = thoughts['value']
  else:
    thoughtees = db['thoughtStorage']
    thoughtees.append(thoughts['thoughts']['value'])
    db['thoughtStorage'] = thoughtees
#Keywords
for i in range(0, len(lines)):
  if '~~' in lines[i]:
    lines[i] = lines[i].replace('~~ ', '#')
  if ' be ' in lines[i]:
    lines[i] = lines[i].replace(' be ', ' = ')
  if 'let ' in lines[i]:
    lines[i] = lines[i].replace('let ', '')
  if 'commands ' in lines[i]:
    lines[i] = lines[i].replace('commands ', 'def ')
  if '{' in lines[i] and ('def' in lines[i] or 'move' in lines[i] or 'until' in lines[i] or 'if' in lines[i] or 'else' in lines[i] or 'topic' in lines[i] or 'repeat' in lines[i]):
    lines[i] = lines[i].replace('{', ':')
  if 'topic ' in lines[i]:
    lines[i] = lines[i].replace('topic', 'class')
  if 'until ' in lines[i]:
    lines[i] = lines[i].replace('until', 'while not')
    condition = lines[i].strip()[10:-2]
    lines[i] = lines[i].replace(condition, f'not({condition})')
  if 'move ' in lines[i]:
    lines[i] = lines[i].replace('move', 'for')
    if ' through ' in lines[i]:
      lines[i] = lines[i].replace('through', 'in')
  if '--' in lines[i]:
    lines[i] = lines[i].replace('--', '-= 1')
  if '++' in lines[i]:
    lines[i] = lines[i].replace('++', '+= 1')
  if '}' == lines[i].strip():
    lines[i] = '\n'
  if '`s ' in lines[i]:
    lines[i] = lines[i].replace('`s ', '.')
  if 'giveback ' in lines[i]:
    lines[i] = lines[i].replace('giveback', 'return')
  if 'repeat ' in lines[i]:
    countexpression = lines[i].strip()[7:-8]
    lines[i] = lines[i].replace(f'repeat {countexpression} times', f'for i in range({countexpression})')
  '''matchesforvars = re.finditer(r'\${(.+)}', lines[i], flags=re.M)
  for match in matchesforvars:
    lines[i] = lines[i].replace('${' + match.groups()[0] + '}', varslist[match.groups()[0]])''' # unneeded

#parse through
allread = ''.join(lines)
try:
  exec(allread)
except SyntaxError as s:
  if 'EOF' in str(s):
    raise ConversationUnexpectedlyEndedError('Someone\'s social anxiety kicked in and they abruptly quit the conversation')
  elif 'EOL' in str(s):
    raise UnexpectedConversationLineEndedError('Someone got interrupted and a line ended without finishing')
  else:
    raise ConversationError(str(s))
except NameError as n:
  raise UnknownNameError(f'What\'s a "{str(n)[5:-15]}"')
def debugr():
  print(allread)
