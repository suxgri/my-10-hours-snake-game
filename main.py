import kivy
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics.vertex_instructions import Line, Rectangle
from kivy.clock import Clock
from kivy.graphics import *
import random

class MyKeyboardListener(Widget):

    isPlaying = False
    hasLost = False
    interval = 0.45
    shouldMove = 'right'
    currentDirection = 'horizontal'
    gridItemsOccupiedBySnake = [100,100] 
    gridItems = [[100, 100], [100, 140], [100, 180], [100, 220], [100, 260], [100, 300], [100, 340], [100, 380], [100, 420], [100, 460], [100, 500], [100, 540], [100, 580], [100, 620], [100, 660], [100, 700], [100, 740], [100, 780], [100, 820], [100, 860], [140, 100], [140, 140], [140, 180], [140, 220], [140, 260], [140, 300], [140, 340], [140, 380], [140, 420], [140, 460], [140, 500], [140, 540], [140, 580], [140, 620], [140, 660], [140, 700], [140, 740], [140, 780], [140, 820], [140, 860], [180, 100], [180, 140], [180, 180], [180, 220], [180, 260], [180, 300], [180, 340], [180, 380], [180, 420], [180, 460], [180, 500], [180, 540], [180, 580], [180, 620], [180, 660], [180, 700], [180, 740], [180, 780], [180, 820], [180, 860], [220, 100], [220, 140], [220, 180], [220, 220], [220, 260], [220, 300], [220, 340], [220, 380], [220, 420], [220, 460], [220, 500], [220, 540], [220, 580], [220, 620], [220, 660], [220, 700], [220, 740], [220, 780], [220, 820], [220, 860], [260, 100], [260, 140], [260, 180], [260, 220], [260, 260], [260, 300], [260, 340], [260, 380], [260, 420], [260, 460], [260, 500], [260, 540], [260, 580], [260, 620], [260, 660], [260, 700], [260, 740], [260, 780], [260, 820], [260, 860], [300, 100], [300, 140], [300, 180], [300, 220], [300, 260], [300, 300], [300, 340], [300, 380], [300, 420], [300, 460], [300, 500], [300, 540], [300, 580], [300, 620], [300, 660], [300, 700], [300, 740], [300, 780], [300, 820], [300, 860], [340, 100], [340, 140], [340, 180], [340, 220], [340, 260], [340, 300], [340, 340], [340, 380], [340, 420], [340, 460], [340, 500], [340, 540], [340, 580], [340, 620], [340, 660], [340, 700], [340, 740], [340, 780], [340, 820], [340, 860], [380, 100], [380, 140], [380, 180], [380, 220], [380, 260], [380, 300], [380, 340], [380, 380], [380, 420], [380, 460], [380, 500], [380, 540], [380, 580], [380, 620], [380, 660], [380, 700], [380, 740], [380, 780], [380, 820], [380, 860], [420, 100], [420, 140], [420, 180], [420, 220], [420, 260], [420, 300], [420, 340], [420, 380], [420, 420], [420, 460], [420, 500], [420, 540], [420, 580], [420, 620], [420, 660], [420, 700], [420, 740], [420, 780], [420, 820], [420, 860], [460, 100], [460, 140], [460, 180], [460, 220], [460, 260], [460, 300], [460, 340], [460, 380], [460, 420], [460, 460], [460, 500], [460, 540], [460, 580], [460, 620], [460, 660], [460, 700], [460, 740], [460, 780], [460, 820], [460, 860], [500, 100], [500, 140], [500, 180], [500, 220], [500, 260], [500, 300], [500, 340], [500, 380], [500, 420], [500, 460], [500, 500], [500, 540], [500, 580], [500, 620], [500, 660], [500, 700], [500, 740], [500, 780], [500, 820], [500, 860], [540, 100], [540, 140], [540, 180], [540, 220], [540, 260], [540, 300], [540, 340], [540, 380], [540, 420], [540, 460], [540, 500], [540, 540], [540, 580], [540, 620], [540, 660], [540, 700], [540, 740], [540, 780], [540, 820], [540, 860], [580, 100], [580, 140], [580, 180], [580, 220], [580, 260], [580, 300], [580, 340], [580, 380], [580, 420], [580, 460], [580, 500], [580, 540], [580, 580], [580, 620], [580, 660], [580, 700], [580, 740], [580, 780], [580, 820], [580, 860], [620, 100], [620, 140], [620, 180], [620, 220], [620, 260], [620, 300], [620, 340], [620, 380], [620, 420], [620, 460], [620, 500], [620, 540], [620, 580], [620, 620], [620, 660], [620, 700], [620, 740], [620, 780], [620, 820], [620, 860], [660, 100], [660, 140], [660, 180], [660, 220], [660, 260], [660, 300], [660, 340], [660, 380], [660, 420], [660, 460], [660, 500], [660, 540], [660, 580], [660, 620], [660, 660], [660, 700], [660, 740], [660, 780], [660, 820], [660, 860], [700, 100], [700, 140], [700, 180], [700, 220], [700, 260], [700, 300], [700, 340], [700, 380], [700, 420], [700, 460], [700, 500], [700, 540], [700, 580], [700, 620], [700, 660], [700, 700], [700, 740], [700, 780], [700, 820], [700, 860], [740, 100], [740, 140], [740, 180], [740, 220], [740, 260], [740, 300], [740, 340], [740, 380], [740, 420], [740, 460], [740, 500], [740, 540], [740, 580], [740, 620], [740, 660], [740, 700], [740, 740], [740, 780], [740, 820], [740, 860], [780, 100], [780, 140], [780, 180], [780, 220], [780, 260], [780, 300], [780, 340], [780, 380], [780, 420], [780, 460], [780, 500], [780, 540], [780, 580], [780, 620], [780, 660], [780, 700], [780, 740], [780, 780], [780, 820], [780, 860], [820, 100], [820, 140], [820, 180], [820, 220], [820, 260], [820, 300], [820, 340], [820, 380], [820, 420], [820, 460], [820, 500], [820, 540], [820, 580], [820, 620], [820, 660], [820, 700], [820, 740], [820, 780], [820, 820], [820, 860], [860, 100], [860, 140], [860, 180], [860, 220], [860, 260], [860, 300], [860, 340], [860, 380], [860, 420], [860, 460], [860, 500], [860, 540], [860, 580], [860, 620], [860, 660], [860, 700], [860, 740], [860, 780], [860, 820], [860, 860]]
    


    def __init__(self, **kwargs):
        super(MyKeyboardListener, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(
            self._keyboard_closed, self, 'text')
        if self._keyboard.widget:
            # If it exists, this widget is a VKeyboard object which you can use
            # to change the keyboard layout.
            pass
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

        startGame = Button(text='start game',
                            on_press=self.start,
                            size=(200,50),
                            pos=(750,1050))
        self.add_widget(startGame)
        with self.canvas:
            Line(rectangle = [100, 100, 800, 800],width=3)
            self.snake = Rectangle(pos=(100,100),size=(40,40))
            foodPosition = self.newfoodposition()
            Color(0, 1, 0)
            self.food = Rectangle(pos=(foodPosition[0],foodPosition[1]),size=(40,40))


    def start(self,_):
    
        if self.isPlaying == False:
            self.isPlaying = True
            self.timer = Clock.schedule_interval(self.move, self.interval)

    def _keyboard_closed(self):
        print('My keyboard have been closed!')
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        newDirection = self.getdirectionfromnewkeypress(keycode[1])#horizontal or verical
        
        if(newDirection != self.currentDirection):
            self.currentDirection = newDirection
            self.shouldMove = keycode[1]
    
        return True
    
    def move(self,dt):
        
        x,y = self.snake.pos

        if self.shouldMove == 'right' and x<840:
            self.snake.pos = (x+40,y)
            self.gridItemsOccupiedBySnake = [x+40,y] 
        elif self.shouldMove == 'left' and x>100:
            self.snake.pos = (x-40,y)
            self.gridItemsOccupiedBySnake = [x-40,y] 
        elif self.shouldMove == 'up' and y<840:
            self.snake.pos = (x,y+40)
            self.gridItemsOccupiedBySnake = [x,y+40] 
        elif self.shouldMove == 'down' and y>100:
            self.snake.pos = (x,y-40)
            self.gridItemsOccupiedBySnake = [x,y-40] 
        else:
            self.setLost()

    def setLost(self):
        Clock.unschedule(self.timer)
        self.isPlaying = False
        self.hasLost = True
        
        self.canvas.clear()
        startGame = Button(text='start game',
                            on_press=self.start,
                            size=(200,50),
                            pos=(750,1050))
        lostButton = Button(text='YOU HAVE LOST !',
                            size=(300,70),
                            pos=(250,1050))
        self.add_widget(startGame)
        self.add_widget(lostButton)
        with self.canvas:
            Line(rectangle=[100, 100, 800, 800],width=3)
            self.snake = Rectangle(pos=(100,100),size=(40,40))

    def getdirectionfromnewkeypress(self,key):
        if key not in ['left','right','up','down']:
            return self.currentDirection
        
        if key in ['left','right']:
            return 'horizontal'
        else:
            return 'vertical'
        
    def newfoodposition(self):
        availables = []
        for element in self.gridItems:
            if element not in self.gridItemsOccupiedBySnake:
                availables.append(element)
        return random.choice(availables)
    
if __name__ == '__main__':
    from kivy.base import runTouchApp
    runTouchApp(MyKeyboardListener())