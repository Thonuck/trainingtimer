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
from src.training_data import save_data


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

    def add_item(self):
        self.list_data.data.append({"datum": "{}".format(datetime.datetime.now()),
                                    "counter": "{}".format("5")})
                                    #'selectable': True})

    def print_items(self):
        print(self.list_data.data)
        print(self.controller.selected_nodes)

    def del_item(self):
        selected_nodes = self.controller.selected_nodes
        new_nodes = [x for i, x in enumerate(self.list_data.data) if i not in selected_nodes]
        self.list_data.data = new_nodes

    def save_data(self):
        save_data(self.list_data.data)


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

    def set_timer(self):
        popup = SetTimerWidget()
        popup.open()
    
    def on_start(self):
        Clock.schedule_interval(self.increment_counter, 1)

    def on_stop(self):
        Clock.unschedule(self.increment_counter)

    def increment_counter(self, something):
        self.counter += 1

class MyScreenManager(ScreenManager):
    pass

class TrainingtimerApp(App):
    def build(self):
        return MyScreenManager()

if __name__ == "__main__":
    TrainingtimerApp().run()
