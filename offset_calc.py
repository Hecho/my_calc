from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class OffsetCalculatorPanel(BoxLayout):
    def __init__(self, **kwargs):
        super(OffsetCalculatorPanel, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [0, 200]  # Adding padding between children vertically

        self.label1 = Label(text="Enter side A:")
        self.entry1 = TextInput(multiline=False, input_type='number')

        self.label2 = Label(text="Enter side B:")
        self.entry2 = TextInput(multiline=False, input_type='number')

        self.label3 = Label(text="Enter center to center offset:")
        self.entry3 = TextInput(multiline=False, input_type='number')

        self.calculate_button = Button(text="Calculate")
        self.calculate_button.bind(on_press=self.calculate)

        self.add_widget(self.label1)
        self.add_widget(self.entry1)
        self.add_widget(self.label2)
        self.add_widget(self.entry2)
        self.add_widget(self.label3)
        self.add_widget(self.entry3)
        self.add_widget(self.calculate_button)

    def calculate(self, instance):
        try:
            num1 = float(self.entry1.text)
            num2 = float(self.entry2.text)
            num3 = float(self.entry3.text)
            left_offset = round((0 - (num1 / 2)) + num3 + (num2 / 2), 2)
            right_offset = round((0 + (num1 / 2)) + num3 - (num2 / 2), 2)

            # Determine the message for the left offset
            if left_offset > 0:
                left_message = f"Left in {left_offset}"
            else:
                left_message = f"Left out {abs(left_offset)}"

            # Determine the message for the right offset
            if right_offset > 0:
                right_message = f"Right out {right_offset}"
            else:
                right_message = f"Right in {abs(right_offset)}"

            popup_content = Label(text=f"{left_message}\n{right_message}")
            popup = Popup(title='Offset', content=popup_content, size_hint=(None, None), size=(300, 200))
            popup.open()

        except ValueError:
            error_popup = Popup(title='Error', content=Label(text="Invalid input. Please enter valid numbers."), size_hint=(None, None), size=(300, 200))
            error_popup.open()
