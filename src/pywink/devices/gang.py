from pywink.devices.base import WinkDevice


class WinkGang(WinkDevice):
    """
    Represents a Wink relay gang.
    """

    def __init__(self, device_state_as_json, api_interface):
        super(WinkGang, self).__init__(device_state_as_json, api_interface)
        self._unit = None

    def unit(self):
        # Gang has no unit
        return self._unit

    def state(self):
        # Gang has no state, reporting it's connection status
        return self.available()
