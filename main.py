
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class MainApp(MDApp):
    """Main application class for Mortgage Calculator"""
    
    def build(self):
        """Build the application UI"""
        return MDLabel(
            text="Hello, World",
            halign="center"
        )


if __name__ == '__main__':
    MainApp().run()
