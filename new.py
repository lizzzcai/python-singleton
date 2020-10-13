from threading import Lock, Thread
import time

class Singleton:
    _lock: Lock = Lock()
    _instance = None

    def __init__(self, value=None):
        self.value = value
        time.sleep(1)

    def __new__(cls, *args, **kwargs):
        if Singleton._instance == None:
            with Singleton._lock:
                if Singleton._instance == None:
                    Singleton._instance = super().__new__(cls)
        
        return Singleton._instance




def test_singleton(value: str) -> None:
    singleton = Singleton(value)
    print(singleton, singleton.value)

if __name__ == "__main__":

    print("If you see the same value, then singleton was reused (yay!)\n"
          "If you see different values, "
          "then 2 singletons were created (booo!!)\n\n"
          "RESULT:\n")
          
    process1 = Thread(target=test_singleton, args=("FOO",))
    process2 = Thread(target=test_singleton, args=("BAR",))
    process1.start()
    process2.start()