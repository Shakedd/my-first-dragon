from json import load
import time

def get_data():
    with open("logger.json", "r") as f:
        data = load(f)
    return data

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

def avg_happiness():
    data = get_data()
    count = 0
    sum = 0
    for key in data.keys():
        count += 1
        sum += data[key]["happiness"]
    return sum/count

def avg_time():
    data = get_data()
    prev_time = time()
    sum = 0
    count = 0
    for key in data.keys():
        if count == 0:
            prev_time = key
            count += 1
        else:
            sum += (key - prev_time)
            count += 1
            prev_time = key
    return sum/count

def main():
    print(avg_time())
    
if __name__ == "__main__":
    main()