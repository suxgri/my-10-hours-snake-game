import kivy
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics.vertex_instructions import Line, Rectangle

class MyKeyboardListener(Widget):

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
        print("start")

    def _keyboard_closed(self):
        print('My keyboard have been closed!')
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        self.move(keycode[1])
        return True
    
    def move(self,movedirection):
        
        x,y = self.snake.pos

        if movedirection == 'right':
            self.snake.pos = (x+40,y)
        elif movedirection == 'left':
            self.snake.pos = (x-40,y)
        elif movedirection == 'up':
            self.snake.pos = (x,y+40)
        elif movedirection == 'down':
            self.snake.pos = (x,y-40)
        else:
            print("skip")

if __name__ == '__main__':
    from kivy.base import runTouchApp
    runTouchApp(MyKeyboardListener())