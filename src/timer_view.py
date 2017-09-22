import datetime
from kivy.properties import NumericProperty, Clock
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen

from training_data import PlankData


class SetTimerWidget(Popup):
    value = NumericProperty()

    def on_press_ok(self, *args):
        self.dismiss()
        return False

    def on_press_cancel(self, *args):
        self.dismiss()
        return False


class TrainingtimerScreen(Screen):
    counter = NumericProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.running = False

    def on_enter(self, **kwargs):
        print("TrainingtimerScreen: on_enter")
        super().on_enter(**kwargs)

    def on_leave(self, **kwargs):
        print("TrainingtimerScreen: on_leave")
        super().on_leave(**kwargs)

    def set_timer(self):
        popup = SetTimerWidget()
        popup.open()

    def on_start(self):
        self.counter = 0
        Clock.schedule_interval(self.increment_counter, 0.1)
        self.running = True
        self.start_stop_button.text = "STOP"

    def on_stop(self):
        Clock.unschedule(self.increment_counter)
        self.running = False
        self.start_stop_button.text = "START"
        datum = datetime.datetime.now()
        datum_string = datum.strftime("%d. %b %Y   %H:%M")
        new_item = dict(datum=datum_string, counter=self.timer_display.text)
        plank_data = PlankData()
        plank_data.add(new_item)
        plank_data.save()

    def on_start_stop(self):
        if self.running:
            self.on_stop()
        else:
            self.on_start()

    def increment_counter(self, something):
        self.counter += 1
