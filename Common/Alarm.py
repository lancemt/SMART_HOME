class Alarm:
    def __init__(self, alarm_id, event_id, home_monitor_id, sensor_id, time_of_event, description, state, state_history):
        self.alarm_id = alarm_id
        self.event_id = event_id
        self.home_monitor_id = home_monitor_id
        self.sensor_id = sensor_id
        self.time_of_event = time_of_event
        self.description = description
        self.state = state
        self.state_history = state_history[10]


