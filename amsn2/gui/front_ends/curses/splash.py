from amsn2.gui import base

class aMSNSplashScreen(base.aMSNSplashScreen):
    """This is the splashscreen for ncurses"""
    def __init__(self, amsn_core, parent):
        """Initialize the interface. You should store the reference to the core in here
        as well as a reference to the window where you will show the splash screen
        """
        # Is it needed in ncurses?
        pass

    def show(self):
        """ Draw the splashscreen """
        pass

    def hide(self):
        """ Hide the splashscreen """
        pass

    def setText(self, text):
        """ Shows a different text inside the splashscreen """
        pass

    def setImage(self, image):
        """ Set the image to show in the splashscreen. This is an ImageView object """
        pass
