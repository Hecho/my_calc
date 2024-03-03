import wx

class BoxFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(BoxFrame, self).__init__(*args, **kw)

        self.panel = wx.Panel(self)
        self.box_length_label = wx.StaticText(self.panel, label="Box Length:")
        self.box_width_label = wx.StaticText(self.panel, label="Box Width:")
        self.box_length_text = wx.TextCtrl(self.panel)
        self.box_width_text = wx.TextCtrl(self.panel)
        
        # Set default values for box dimensions
        self.box_length_text.SetValue("1.0")
        self.box_width_text.SetValue("1.0")

        self.box_canvas = BoxCanvas(self.panel)

        self.Bind(wx.EVT_TEXT, self.on_text_update, self.box_length_text)
        self.Bind(wx.EVT_TEXT, self.on_text_update, self.box_width_text)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.box_length_label, 0, wx.ALL, 5)
        sizer.Add(self.box_length_text, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.box_width_label, 0, wx.ALL, 5)
        sizer.Add(self.box_width_text, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(self.box_canvas, 1, wx.EXPAND | wx.ALL, 5)

        self.panel.SetSizer(sizer)
        self.Center()
        self.Show()

    def on_text_update(self, event):
        try:
            length = float(self.box_length_text.GetValue())
            width = float(self.box_width_text.GetValue())
            self.box_canvas.set_dimensions(length, width)
            self.box_canvas.Refresh()
        except ValueError:
            wx.MessageBox("Please enter valid numerical values for length and width.", "Error", wx.OK | wx.ICON_ERROR)

class BoxCanvas(wx.Panel):
    def __init__(self, parent):
        super(BoxCanvas, self).__init__(parent)
        self.length = 1.0
        self.width = 1.0

        self.Bind(wx.EVT_PAINT, self.on_paint)

    def set_dimensions(self, length, width):
        self.length = length
        self.width = width

    def on_paint(self, event):
        dc = wx.PaintDC(self)
        dc.Clear()

        # Set text color to black
        dc.SetTextForeground(wx.BLACK)

        # Set font size to 12
        dc.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))

        # Get the size of the panel
        panel_width, panel_height = self.GetSize()

        # Calculate the scale factor
        scale_factor = min(panel_width, panel_height) / max(self.length, self.width)

        # Adjust the scale factor to leave room for annotations
        scale_factor *= 0.6

        # Calculate the box dimensions
        box_width = int(self.width * scale_factor)
        box_length = int(self.length * scale_factor)

        # Calculate the box position
        box_x = (panel_width - box_width) // 2
        box_y = (panel_height - box_length) // 2

        dc.DrawRectangle(box_x, box_y, box_width, box_length)

        # Annotate the sides
        dc.DrawText(f"Length: {self.length}", box_x + box_width + 10, int(box_y + box_length/2))
        dc.DrawText(f"Width: {self.width}", int(box_x + box_width/2), box_y - 20)

if __name__ == '__main__':
    app = wx.App(False)
    frame = BoxFrame(None, title="Box Drawer", size=(600, 400))
    app.MainLoop()
