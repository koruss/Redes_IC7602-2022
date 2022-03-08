from prueba import *
class Controller(object):
    def __init__(self):
        self.recorder = Recorder(channels=2)
        self.file = self.recorder.open('nonblocking.wav', 'wb')
        
    def start(self):
        pass

        

    def pause(self,root):
        pass

    def resume(self, root):
        pass

    def record(self,root):
        pass