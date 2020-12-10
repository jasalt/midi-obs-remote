''' Midi OBS Remote by Jarkko Saltiola
Version 0.0.1 (pre-development) - MIT License - See README.md'''

import toga
import os
from toga.style.pack import COLUMN, ROW, Pack, CENTER
import time

import asyncio
import tinydb

class MyApp(toga.App):
    ### Utility Functions

    ### GUI HANDLERS

    def mock_switch_handler(self, widget, **kwargs):
        print(f"mock_switch is_on = {self.mock_switch.is_on}")

    def update_index_stats(self, artists):
        self.index_stats_label.text = f"Indexed {artists} artists."

    ### BUILD GUI

    def startup(self):
        # Controls

        self.index_stats_label = toga.Label('No tracks loaded, please index.', style=Pack(padding=10))

        self.reindex_button = toga.Button('Index Collection', on_press=self.re_index)
        self.reindex_button.style.padding = 10
        self.reindex_button.style.flex = 1

        self.mock_switch = toga.Switch('Enable mock Sender', on_toggle=self.mock_switch_handler)
        self.mock_switch.style.padding = 10
        self.mock_switch.style.flex = 1

        top_box = toga.Box(style=Pack(direction=ROW), children=[self.reindex_button, self.mock_switch])

        # Cover Art Image Preview

        self.img = toga.Image(os.getcwd() + "/resources/testcard720.png")
        self.img_view = toga.ImageView(id='img_view', image=self.img, 
                                style=Pack(flex=1))

        self.img_label = toga.Label('Waiting for mock information...', style=Pack(padding=10))

        bottom_box = toga.Box(children=[self.img_label, self.img_view], 
                            style=Pack(flex=1, direction=COLUMN))


        main_box = toga.Box(style=Pack(direction=COLUMN),
                            children=[self.index_stats_label, top_box, bottom_box])


        self.main_window = toga.MainWindow(title=self.name, size=(400,500))
        self.main_window.content = main_box
        self.main_window.show()

        self.cache_file = os.getcwd() + "/tracks.p"

        self.mapping = {"A": {"play": False, "updated_at": 0},
                      "B": {"play": False, "updated_at": 0},
                      "C": {"play": False, "updated_at": 0},
                      "D": {"play": False, "updated_at": 0}
        }

def main():
    the_app = MyApp('Midi OBS Remote', 'com.saltiolacode.midiobsremote')
    return the_app

if __name__ == '__main__':
    app = main()
    app.main_loop()
