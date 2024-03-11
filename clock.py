from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock as kivy_clock
from datetime import datetime


class ClockApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.label = Label(text='', font_size='50sp', halign='center')
        self.layout.add_widget(self.label)

        # Update the time every second
        kivy_clock.schedule_interval(self.update_time, 1)
        return self.layout

    def update_time(self, dt):
        current_time = datetime.now().strftime("%H:%M:%S")
        self.label.text = f"Current Time: {current_time}"


if __name__ == '__main__':
    ClockApp().run()

