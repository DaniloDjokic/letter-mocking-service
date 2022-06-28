from threading import Lock

class MockingLogic:
    def __init__(self):
        self.mockingEnabled = True
        self.lock = Lock()

    def isMockingEnabled(self):
        return self.mockingEnabled

    def setMockingEnabled(self, mockingEnabled):
        self.lock.acquire()
        try:
            self.mockingEnabled = mockingEnabled
        finally:
            self.lock.release()