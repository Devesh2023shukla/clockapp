from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from datetime import datetime


class ClockLabel(Label):
    def on_start(self):
        pass


class ClockApp(App):
    def build(self):
        self.label = Label(font_size='60sp')
        Clock.schedule_interval(self.update_time, 1)
        self.update_time(0)
        return self.label

    def update_time(self, dt):
        self.label.text = datetime.now().strftime('%H:%M:%S')


if __name__ == '__main__':
    ClockApp().run()