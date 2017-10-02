import json


class Event:
    def __init__(self, event_id, state, description, time_of_event, home_monitor_id, sensor_id):
        self.event_id = event_id
        self.state = state
        self.description = description
        self.time_of_event = time_of_event
        self.home_monitor_id = home_monitor_id
        self.sensor_id = sensor_id

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)
