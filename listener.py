import json
from my_first_dragon import Pet
import functools

LOG_JSON = {}

# listening to the call of eat, play, sleep and log them to a json file
def logger(func):
    @functools.wraps(func)
    def wrapper(p: Pet, *args, **kwargs):
        data = {
            "action": func.__name__,
            "hunger": p.hunger,
            "energy": p.energy,
            "happiness": p.happiness}
        LOG_JSON["%(asctime)"].append(data)
        with open("logger.json", "w") as f:
            json.dump(LOG_JSON, f)
        return func(p, *args, **kwargs)
    return wrapper
        
        