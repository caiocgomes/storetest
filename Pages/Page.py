from abc import ABCMeta, abstractmethod

class Page(object):
    __metaclass__ = ABCMeta

    def __init__(self, renderer = None, *args, **kwargs):
        super(Page, self).__init__(*args, **kwargs)
        self.renderer = renderer
        self.template = None

    @abstractmethod
    def getData(self):
        return {}

    def render(self):
        self.data = self.getData()
        return self.renderer(self.template, self.data)


