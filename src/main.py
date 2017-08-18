from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.properties import NumericProperty
from kivy.config import Config
from kivy.clock import Clock

Config.set("graphics", "width", "200")
Config.set("graphics", "height", "200")

class SetTimerWidget(Popup):
    value = NumericProperty()
    
    def on_press_ok(self, *args):
        self.dismiss()
        
        return False

    def on_press_cancel(self, *args):
        self.dismiss()
        return False


class TrainingtimerWidget(BoxLayout):
    counter = NumericProperty()

    def set_timer(self):
        popup = SetTimerWidget()
        popup.open()
    
    def on_start(self):
        Clock.schedule_interval(self.increment_counter, 1)

    def on_stop(self):
        Clock.unschedule(self.increment_counter)

    def increment_counter(self, something):
        self.counter += 1


class TrainingtimerApp(App):
    def build(self):
        return TrainingtimerWidget()

if __name__ == "__main__":
    TrainingtimerApp().run()
