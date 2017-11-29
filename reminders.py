import redis
class reminders:

    def __init__(self, inventory):
        self.r = redis.Redis()