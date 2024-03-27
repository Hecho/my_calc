import wx
import oval_calc
import spigot_calc
import offset_calc
import frustrum_calc

class MainFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MainFrame, self).__init__(*args, **kw)
        self.InitUI()

    def InitUI(self):
        self.notebook = wx.Notebook(self)
        self.oval_panel = oval_calc.OvalCalculatorPanel(self.notebook)
        self.spigot_panel = spigot_calc.SpigotCalculatorPanel(self.notebook)
        self.offset_panel = offset_calc.OffsetCalculatorPanel(self.notebook)
        self.frustrum_panel = frustrum_calc.FrustrumCalculatorPanel(self.notebook)

        self.notebook.AddPage(self.oval_panel, "Oval Calculator")
        self.notebook.AddPage(self.spigot_panel, "Spigot Calculator")
        self.notebook.AddPage(self.offset_panel, "Offset Calculator")
        self.notebook.AddPage(self.frustrum_panel, "Frustrum Calculator")

        self.SetTitle("Multi Calculator")
        self.Centre()

def main():
    app = wx.App(False)
    frame = MainFrame(None, title='Multi Calculator', size=(500, 450))
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
