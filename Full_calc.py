from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader
from kivy.uix.screenmanager import ScreenManager, Screen
from oval_calc import OvalCalculatorPanel
from spigot_calc import SpigotCalculatorPanel
from offset_calc import OffsetCalculatorPanel

class MainScreen(BoxLayout):
    def __init__(self, screen_manager, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.screen_manager = screen_manager  # Store the ScreenManager instance

        # Create a TabbedPanel
        tabbed_panel = TabbedPanel(do_default_tab=False, tab_pos='top_mid', tab_width=125)

        # Create screens for each calculator option
        oval_screen = Screen(name='oval')
        spigot_screen = Screen(name='spigot')
        offset_screen = Screen(name='offset')

        # Create calculator panels for each screen
        oval_panel = OvalCalculatorPanel()
        spigot_panel = SpigotCalculatorPanel()
        offset_panel = OffsetCalculatorPanel()

        # Add calculator panels to the screens
        oval_screen.add_widget(oval_panel)
        spigot_screen.add_widget(spigot_panel)
        offset_screen.add_widget(offset_panel)

        # Create tabs for each calculator option
        oval_tab = TabbedPanelHeader(text='Oval Calculator')
        oval_tab.content = oval_screen
        tabbed_panel.add_widget(oval_tab)

        spigot_tab = TabbedPanelHeader(text='Spigot Calculator')
        spigot_tab.content = spigot_screen
        tabbed_panel.add_widget(spigot_tab)

        offset_tab = TabbedPanelHeader(text='Offset Calculator')
        offset_tab.content = offset_screen
        tabbed_panel.add_widget(offset_tab)

        # Add the TabbedPanel to the layout
        self.add_widget(tabbed_panel)

class CalculatorApp(App):
    def build(self):
        screen_manager = ScreenManager()  # Create a ScreenManager instance
        return MainScreen(screen_manager)  # Pass ScreenManager instance to MainScreen

if __name__ == '__main__':
    CalculatorApp().run()
