from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class FirstScr(Screen):
    def __init__(self, name="first"):
        super().__init__(name=name)
        hbox = BoxLayout(orientation="horizontal")
        vbox = BoxLayout(orientation="vertical")

        txt = Label(text="Виберіть екран")
        btn1 = Button(text="екран 1")
        btn1.bind(on_press=self.goToUkrScreen1)
        btn2 = Button(text="екран 2")
        btn2.bind(on_press=self.goToUkrScreen2)
        btn3 = Button(text="екран 3")
        btn3.bind(on_press=self.goToUkrScreen3)

        vbox.add_widget(btn1)
        vbox.add_widget(btn2)
        vbox.add_widget(btn3)

        hbox.add_widget(txt)
        hbox.add_widget(vbox)

        self.add_widget(hbox)

    def goToUkrScreen1(self, instance):
        self.manager.current = "екран 1"

    def goToUkrScreen2(self, instance):
        self.manager.current = "екран 2"

    def goToUkrScreen3(self, instance):
        self.manager.current = "екран 3"


class UkrScreen1(Screen):
    def __init__(self, name="екран 1"):
        super().__init__(name=name)
        hbox = BoxLayout(orientation="horizontal")
        btn_back = Button(text="Назад")
        btn_back.bind(on_press=self.goBackToFirst)
        hbox.add_widget(btn_back)

        self.add_widget(hbox)

    def goBackToFirst(self, instance):
        self.manager.current = "first"


class UkrScreen2(Screen):
    def __init__(self, name="екран 2"):
        super().__init__(name=name)
        hbox = BoxLayout(orientation="horizontal")
        btn_back = Button(text="Назад")
        btn_back.bind(on_press=self.goBackToFirst)
        hbox.add_widget(btn_back)

        self.add_widget(hbox)

    def goBackToFirst(self, instance):
        self.manager.current = "first"


class UkrScreen3(Screen):
    def __init__(self, name="екран 3"):
        super().__init__(name=name)
        hbox = BoxLayout(orientation="vertical")

        btn_back = Button(text="Назад")
        btn_back.bind(on_press=self.goBackToFirst)

        txt_input = TextInput(hint_text="Введіть текст")
        Writhe = Label(text="Привіт!")

        hbox.add_widget(btn_back)
        hbox.add_widget(txt_input)
        hbox.add_widget(Writhe)
        self.add_widget(hbox)

    def goBackToFirst(self, instance):
        self.manager.current = "first"


class MyApp(App):
    def build(self):
        sm = ScreenManager()

        first_screen = FirstScr()
        ukr_screen_1 = UkrScreen1()
        ukr_screen_2 = UkrScreen2()
        ukr_screen_3 = UkrScreen3()

        sm.add_widget(first_screen)
        sm.add_widget(ukr_screen_1)
        sm.add_widget(ukr_screen_2)
        sm.add_widget(ukr_screen_3)

        return sm

if __name__ == "__main__":
    MyApp().run()
