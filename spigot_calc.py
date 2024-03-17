from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import math

class SpigotCalculatorPanel(BoxLayout):
    def __init__(self, **kwargs):
        super(SpigotCalculatorPanel, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [0, 200]  # Adding padding between children vertically

        self.label1 = Label(text="Enter number of spigots:")
        self.entry1 = TextInput(multiline=False, input_type='number')

        self.label2 = Label(text="Enter size of lid:")
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
            num_spigots = int(self.entry1.text)
            num_lid = float(self.entry2.text)

            num_offsets = math.ceil(num_spigots / 2)  # Increase the number of offsets for odd spigots

            if num_spigots % 2 == 0:
                offset_values = [math.floor(num_lid / (2 * num_spigots) * (2 * i + 1)) for i in range(num_offsets)]
            else:
                offset_values = [0] + [math.floor(num_lid / (num_spigots) * i) for i in range(1, num_offsets + 1)]

            message = "\n".join([f"Offset {i + 1}: {offset_values[i]}" for i in range(num_offsets)])

            popup_content = Label(text=message)
            popup = Popup(title='Offsets', content=popup_content, size_hint=(None, None), size=(300, 200))
            popup.open()

        except ValueError:
            error_popup = Popup(title='Error', content=Label(text="Invalid input. Please enter valid numbers."), size_hint=(None, None), size=(300, 200))
            error_popup.open()
