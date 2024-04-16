from model import Model
from view import View
from typing import Optional

class Controller:
    text = "Hello, world!"

    def __init__(self):
        # self.model = Model("Hello, world!")
        self.view: Optional[View] = None

    def main(self, app):
        # ! Don't use view a __init function
        # ! it leads to leak in memory which leads to crashing
        self.view = View(self)
        self.view.main(app)

    # def get_text(self):
    #     return "Hello, world!"
