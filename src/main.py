import csv
import datetime

import os
from kivy.app import App
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.properties import NumericProperty, StringProperty, BooleanProperty
from kivy.config import Config
from kivy.clock import Clock
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior

from kivy.uix.screenmanager import ScreenManager, Screen

#Config.set("graphics", "width", "200")
#Config.set("graphics", "height", "200")
from src.training_data import PlankData


class ResultItem(RecycleDataViewBehavior, BoxLayout):
    index = None

    """properties used for data to be displayed"""
    datum = StringProperty()
    counter = StringProperty()

    """ depending on this property, the item is highlighted as
    selected or not"""
    selected = BooleanProperty(False)

    def refresh_view_attrs(self, rv, index, data):
        """ Catch and handle the view changes """
        self.index = index
        return super(ResultItem, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        """ Add selection on touch down """
        if super(ResultItem, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos):
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        """ Respond to the selection of items in the view. """
        self.selected = is_selected
        if is_selected:
            print("selection changed to {0}".format(rv.data[index]))
        else:
            print("selection removed for {0}".format(rv.data[index]))


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    """Needs to be implemented, so the items of the recycle view can
    be selected"""
    pass


class ResultTableScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.plank_data = None
        # self.list_data.data = self.plank_data.data

    def on_enter(self, **kwargs):
        print("ResultTableScreen: on_enter")
        self.plank_data = PlankData()
        self.list_data.data = self.plank_data.data
        super().on_enter(**kwargs)

    def on_leave(self, **kwargs):
        print("ResultTableScreen: on_leave")
        self.plank_data = None
        super().on_leave(**kwargs)

    def add_item(self):
        datum = datetime.datetime.now()
        datum_string = datum.strftime("%d.%m.%Y %H:%M")
        self.plank_data.add({"datum": "{}".format(datum_string),
                             "counter": "{}".format("5")})
        self.list_data.data = self.plank_data.data

    def print_items(self):
        print(self.list_data.data)
        print(self.controller.selected_nodes)

    def del_item(self):
        selected_nodes = self.controller.selected_nodes
        self.plank_data.remove_by_indices(self.controller.selected_nodes)
        self.plank_data.save()

        # new_nodes = [x for i, x in enumerate(self.list_data.data) if i not in selected_nodes]
        self.list_data.data = self.plank_data.data

    def save_data(self):
        self.plank_data.save()


class SetTimerWidget(Popup):
    value = NumericProperty()
    
    def on_press_ok(self, *args):
        self.dismiss()
        return False

    def on_press_cancel(self, *args):
        self.dismiss()
        return False


class ResultTableScreen(Screen):
    pass


class TrainingtimerScreen(Screen):
    counter = NumericProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

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
        Clock.schedule_interval(self.increment_counter, 0.1)

    def on_stop(self):
        Clock.unschedule(self.increment_counter)
        datum = datetime.datetime.now()
        datum_string = datum.strftime("%d.%m.%Y %H:%M")
        new_item = dict(datum=datum_string, counter=self.timer_display.text)
        plank_data = PlankData()
        plank_data.add(new_item)
        plank_data.save()

    def increment_counter(self, something):
        self.counter += 1


class MyScreenManager(ScreenManager):
    pass

class TrainingtimerApp(App):
    def build(self):
        return MyScreenManager()

if __name__ == "__main__":
    TrainingtimerApp().run()
