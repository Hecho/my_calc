import wx
import math

class SpigotCalculatorPanel(wx.Panel):
    def __init__(self, parent):
        super(SpigotCalculatorPanel, self).__init__(parent)

        self.label1 = wx.StaticText(self, label="Enter number of spigots:")
        self.entry1 = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        
        self.label2 = wx.StaticText(self, label="Enter size of lid:")
        self.entry2 = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        
        self.calculate_button = wx.Button(self, label="Calculate")
        self.calculate_button.Bind(wx.EVT_BUTTON, self.calculate)

        # Bind the Enter key in entry1 to move focus to entry2
        self.entry1.Bind(wx.EVT_TEXT_ENTER, lambda event: self.entry2.SetFocus())

        # Bind the Enter key press in the last TextCtrl to the calculate method
        self.entry2.Bind(wx.EVT_TEXT_ENTER, self.calculate)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.label1, 0, wx.ALL, 5)
        self.sizer.Add(self.entry1, 0, wx.EXPAND|wx.ALL, 5)
        self.sizer.Add(self.label2, 0, wx.ALL, 5)
        self.sizer.Add(self.entry2, 0, wx.EXPAND|wx.ALL, 5)
        self.sizer.Add(self.calculate_button, 0, wx.ALL, 5)

        self.SetSizer(self.sizer)
        self.Layout()

    def calculate(self, event):
        try:
            num_spigots = int(self.entry1.GetValue())
            num_lid = float(self.entry2.GetValue())

            num_offsets = math.ceil(num_spigots / 2)  # Increase the number of offsets for odd spigots

            if num_spigots % 2 == 0:
                offset_values = [math.floor(num_lid / (2 * num_spigots) * (2 * i + 1)) for i in range(num_offsets)]
            else:
                offset_values = [0] + [math.floor(num_lid / (num_spigots) * i) for i in range(1, num_offsets + 1)]

            message = "\n".join([f"Offset {i + 1}: {offset_values[i]}" for i in range(num_offsets)])

            wx.MessageBox(message, "Offsets", wx.OK | wx.ICON_INFORMATION)

        except ValueError:
            wx.MessageBox("Invalid input. Please enter valid numbers.", "Error", wx.OK | wx.ICON_ERROR)

