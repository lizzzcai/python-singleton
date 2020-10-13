from threading import Lock, Thread
import time

class Singleton:
    _instances: dict = {}
    _lock: Lock = Lock()

    def __init__(self, value=None):
        self.value = value
        time.sleep(1)

    @classmethod
    def instance(cls, *args, **kwargs):
        if cls not in Singleton._instances:
            with Singleton._lock:
                if cls not in Singleton._instances:
                    Singleton._instances[cls] = cls(*args, **kwargs)
        
        return Singleton._instances[cls]




def test_singleton(value: str) -> None:
    singleton = Singleton.instance(value)
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