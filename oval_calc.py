from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import math

class OvalCalculatorPanel(BoxLayout):
    def __init__(self, **kwargs):
        super(OvalCalculatorPanel, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [0, 200]  # Adding padding between children vertically

        self.label1 = Label(text="Enter restricted size:")
        self.entry1 = TextInput(multiline=False, input_type='number')

        self.label2 = Label(text="Enter required size:")
        self.entry2 = TextInput(multiline=False, input_type='number')

        self.calculate_button = Button(text="Calculate")
        self.calculate_button.bind(on_press=self.calculate)

        self.add_widget(self.label1)
        self.add_widget(self.entry1)
        self.add_widget(self.label2)
        self.add_widget(self.entry2)
        self.add_widget(self.calculate_button)

    def calculate(self, instance):
        try:
            box = float(self.entry1.text)
            num1 = (box - 15)
            num2 = float(self.entry2.text)
            major_axis = math.floor(num1 + (3.142/2) * (num2 - num1))
            minor_axis = math.floor(num1)

            popup_content = f"Major axis: {major_axis}\nMinor axis: {minor_axis}"
            popup = Popup(title='Oval', content=Label(text=popup_content), size_hint=(None, None), size=(300, 200))
            popup.open()
        except ValueError:
            error_popup = Popup(title='Error', content=Label(text="Invalid input. Please enter valid numbers."), size_hint=(None, None), size=(300, 200))
            error_popup.open()
