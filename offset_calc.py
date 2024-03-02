import wx
import math

class OffsetCalculatorPanel(wx.Panel):
    def __init__(self, parent):
        super(OffsetCalculatorPanel, self).__init__(parent)

        self.label1 = wx.StaticText(self, label="Enter side A:")
        self.entry1 = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        
        self.label2 = wx.StaticText(self, label="Enter side B:")
        self.entry2 = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)

        self.label3 = wx.StaticText(self, label="Enter center to center offset:")
        self.entry3 = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)

        self.calculate_button = wx.Button(self, label="Calculate")
        self.calculate_button.Bind(wx.EVT_BUTTON, self.calculate)

        # Bind the Enter key in entry1 to move focus to entry2
        self.entry1.Bind(wx.EVT_TEXT_ENTER, lambda event: self.entry2.SetFocus())

        # Bind the Enter key in entry2 to move focus to entry3
        self.entry2.Bind(wx.EVT_TEXT_ENTER, lambda event: self.entry3.SetFocus())

        # Bind the Enter key press in the last TextCtrl to the calculate method
        self.entry3.Bind(wx.EVT_TEXT_ENTER, self.calculate)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.label1, 0, wx.ALL, 5)
        self.sizer.Add(self.entry1, 0, wx.EXPAND|wx.ALL, 5)
        self.sizer.Add(self.label2, 0, wx.ALL, 5)
        self.sizer.Add(self.entry2, 0, wx.EXPAND|wx.ALL, 5)
        self.sizer.Add(self.label3, 0, wx.ALL, 5)  # Adding label3 to the sizer
        self.sizer.Add(self.entry3, 0, wx.EXPAND|wx.ALL, 5)  # Adding entry3 to the sizer
        self.sizer.Add(self.calculate_button, 0, wx.ALL, 5)

        self.SetSizer(self.sizer)
        self.Layout()


    def calculate(self, event):
        try:
            num1 = float(self.entry1.GetValue())
            num2 = float(self.entry2.GetValue())
            num3 = float(self.entry3.GetValue())
            Left_offset = ((0 -(num1 / 2)) + num3 + (num2 / 2))
            Right_offset = ((0 +((num1 / 2))) + num3 - (num2 / 2))

            # Determine the message for the left offset
            if Left_offset > 0:
                left_message = f"Left in {math.floor(Left_offset)}"
            else:
                left_message = f"Left out {math.floor(abs(Left_offset))}"

            # Determine the message for the right offset
            if Right_offset > 0:
                right_message = f"Right out {math.floor(Right_offset)}"
            else:
                right_message = f"Right in {math.floor(abs(Right_offset))}"

            wx.MessageBox(f"{left_message}\n{right_message}", "Offset", wx.OK | wx.ICON_INFORMATION)
        except ValueError:
            wx.MessageBox("Invalid input. Please enter valid numbers.", "Error", wx.OK | wx.ICON_ERROR)


