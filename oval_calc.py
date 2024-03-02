import wx
import math

class OvalCalculatorPanel(wx.Panel):
    def __init__(self, parent):
        super(OvalCalculatorPanel, self).__init__(parent)

        self.label1 = wx.StaticText(self, label="Enter restricted size:")
        self.entry1 = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        
        self.label2 = wx.StaticText(self, label="Enter required size:")
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
            box = float(self.entry1.GetValue())
            num1 = (box - 15)
            num2 = float(self.entry2.GetValue())
            major_axis = math.floor(num1 + (3.142/2) * (num2 - num1))
            minor_axis = math.floor(num1)

            wx.MessageBox(f"Major axis: {major_axis}\nMinor axis: {minor_axis}", "Oval", wx.OK | wx.ICON_INFORMATION)
        except ValueError:
            wx.MessageBox("Invalid input. Please enter valid numbers.", "Error", wx.OK | wx.ICON_ERROR)
