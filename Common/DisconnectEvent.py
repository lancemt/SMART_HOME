import json


class DisconnectEvent:
    def __init__(self, reconnect_ip_address):
        self.reconnect_ip_address = reconnect_ip_address

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)
