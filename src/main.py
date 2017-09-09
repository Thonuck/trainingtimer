from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


# Config.set("graphics", "width", "200")
# Config.set("graphics", "height", "200")


class MyScreenManager(ScreenManager):
    pass


class TrainingtimerApp(App):
    def build(self):
        return MyScreenManager()


if __name__ == "__main__":
    TrainingtimerApp().run()
