from json import loads

def get_data():
    with open("logger.json", "a") as f:
        data = f.read()
    return loads(data)

def happiest():
    data = get_data()
    max_happiness = 0
    for key in data.keys():
        if data[key]["happiness"] > max_happiness:
            max_happiness = data[key]["happiness"]
            date = key
    return date

def most():
    data = get_data()
    actions = {"eat": 0, "sleep": 0, "play": 0}
    for key in data.keys():
        if data[key]["action"] == "play":
            actions["play"] += 1
        if data[key]["action"] == "sleep":
            actions["sleep"] += 1
        if data[key]["action"] == "eat":
            actions["eat"] += 1
    maximum = max(actions["eat"], actions["play"], actions["sleep"])
    for act in actions.keys():
        if actions[act] == maximum:
            return act

def lower_than_50():
    data = get_data()
    counter = 0
    for key in data.keys():
        if data[key]["points"] < 50:
            counter += 1
    return counter