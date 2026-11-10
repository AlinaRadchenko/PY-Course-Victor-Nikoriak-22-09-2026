# AI log: допоміг розібратися з логікою зберігання каналів у списку та використанням current_index для визначення активного каналу
# також отримала підказки щодо використання оператора % для циклічного переходу між каналами
class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.current_index = 0

    def first_channel(self):
        self.current_index = 0
        return self.channels[self.current_index]

    def last_channel(self):
        self.current_index = len(self.channels) - 1
        return self.channels[len(self.channels) - 1]


    def turn_channel(self, a):
        self.current_index = a - 1
        return self.channels[self.current_index]

    def next_channel(self):
        self.current_index = (self.current_index + 1) % len(self.channels)
        return self.channels[self.current_index]

    def previous_channel(self):
        self.current_index = (self.current_index - 1) % len(self.channels)
        return self.channels[self.current_index]

    def current_channel(self):
        return self.channels[self.current_index]

    def exists(self, value):
        if isinstance(value, int):
            return 1 <= value <= len(self.channels)
        return value in self.channels





CHANNELS = ["BBC", "Discovery", "TV1000"]

controller = TVController(CHANNELS)

print(controller.first_channel() )     # "BBC"
print(controller.last_channel() )      # "TV1000"
print(controller.turn_channel(1) )     # "BBC"
# turn_channel(0) індекс стане -1, це останній елемента списку

# next_channel() буде першим викликаним методом після створення
# контролера, він поверне "Discovery", тому що початковий індекс дорівнює 0
print(controller.next_channel() )      # "Discovery"
print(controller.previous_channel()  ) # "BBC"
print(controller.current_channel()  )  # "BBC"
print(controller.exists(4) )           # False
print(controller.exists("BBC") )       # True