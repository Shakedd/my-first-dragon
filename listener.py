import json
import functools
from time import asctime

LOG_JSON = {}

# listening to the call of eat, play, sleep and log them to a json file
def logger(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        tmp = self
        func(tmp, *args, **kwargs)
        data = {
            "action": func.__name__,
            "hunger": tmp.hunger,
            "energy": tmp.energy,
            "happiness": tmp.happiness}
        LOG_JSON[asctime()] = data
        with open("logger.json", "w") as f:
            json.dump(LOG_JSON, f)
        return func(self, *args, **kwargs)
    return wrapper
        
        