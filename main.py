from kivy.app import App
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout



class BoxLayoutExample(BoxLayout):
    pass
    # This is how to declare some buttons in Python Syntax
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.orientation = "vertical"
    #     b1 = Button(text="A")
    #     b2 = Button(text="B")
    #     b3 = Button(text="C")
    #     self.add_widget(b1)
    #     self.add_widget(b2)
    #     self.add_widget(b3)

class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "lr-tb"
        for i in range(0,100):
            b = Button(
                text=str(i+1), 
                size_hint= (None, None), 
                size=(dp(100), dp(100)))
            self.add_widget(b)

class TheLabApp(App):
    pass

TheLabApp().run()