from pywink.devices.base import WinkDevice


class WinkKey(WinkDevice):
    """
    Represents a Wink key.
    """

    def __init__(self, device_state_as_json, api_interface):
        super(WinkKey, self).__init__(device_state_as_json, api_interface)
        self._available = True
        self._unit = None
        self._capability = "activity_detected"

    def state(self):
        return self._last_reading.get(self.capability(), False)

    def parent_id(self):
        return self.json_state.get('parent_object_id')

    def available(self):
        """Keys are virtual therefore they don't have a connection status
        always return True
        """
        return self._available

    def unit(self):
        # Keys are a boolean sensor, they have no unit.
        return self._unit

    def capability(self):
        return self._capability
