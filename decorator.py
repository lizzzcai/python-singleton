from threading import Lock, Thread

def Singleton(cls):
    _instances: dict = {}
    _lock: Lock = Lock()

    def _singleton(*args, **kwargs):
        if cls not in _instances:
            with _lock:
                if cls not in _instances:
                    _instances[cls] = cls(*args, **kwargs)
        
        return _instances[cls]
    
    return _singleton



@Singleton
class A:
    value = 1

    def __init__(self, x=0):
        self.value = x
    
@Singleton
class B:
    value = 1

    def __init__(self, x=0):
        self.value = x

def test_singleton(value: str) -> None:
    singleton = A(value)
    print(singleton, singleton.value)

def test_singleton2(value: str) -> None:
    singleton = B(value)
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

    process1 = Thread(target=test_singleton2, args=("BAR",))
    process2 = Thread(target=test_singleton2, args=("FOO",))
    process1.start()
    process2.start()