import kivy
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics.vertex_instructions import Line, Rectangle
from kivy.clock import Clock

class MyKeyboardListener(Widget):

    isplaying = False
    haslost = False
    INTERVAL = 0.45
    shouldmove = 'right'
    currentdirection = 'horizontal'

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

    def start(self,_):
    
        if self.isplaying == False:
            self.isplaying = True
            self.timer = Clock.schedule_interval(self.move, self.INTERVAL)

    def _keyboard_closed(self):
        print('My keyboard have been closed!')
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        
        return True
    
    def move(self,dt):
        
        x,y = self.snake.pos

        if self.shouldmove == 'right' and x<840:
            self.snake.pos = (x+40,y)
        elif self.shouldmove == 'left' and x>100:
            self.snake.pos = (x-40,y)
        elif self.shouldmove == 'up' and y<840:
            self.snake.pos = (x,y+40)
        elif self.shouldmove == 'down' and y>100:
            self.snake.pos = (x,y-40)
        else:
            self.setLost()

    def setLost(self):
        Clock.unschedule(self.timer)
        self.isplaying = False
        self.haslost = True
        
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


if __name__ == '__main__':
    from kivy.base import runTouchApp
    runTouchApp(MyKeyboardListener())