# AI log: попросила надати приклади виклику та перехоплення CustomException
class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg
        with open("logs.txt", "a", encoding="utf-8") as f:
            f.write(f"{self.msg}\n")


try:
    raise CustomException("First error: something went wrong")
except CustomException as e:
    print(f"Caught exception: {e}")


try:
    raise CustomException("Second error: invalid value")
except CustomException as e:
    print(f"Caught exception: {e}")

# Вміст logs.txt:
# First error: something went wrong
# Second error: invalid value

# режим відкриття файлу: "a" додає нові повідомлення в кінець файлу,
# а "w" видаляє попередній вміст