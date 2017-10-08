import uuid

class Alarm:
    def __init__(self, event):
        self.alarm_id = str(uuid.uuid4())
        self.event_id = event.event_id
        self.home_monitor_id = event.home_monitor_id
        self.sensor_id = event.sensor_id
        self.time_of_event = event.time_of_event
        self.description = event.description
        self.state = event.state
        self.state_history = [""]*10
        self.acknowledged_by = ""
        self.acknowledged_at = ""

