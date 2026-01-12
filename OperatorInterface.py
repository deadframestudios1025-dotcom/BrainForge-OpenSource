class OperatorInterface:
    def __init__(self):
        self.Operator_Interface = [
            "TouchScreen = Function",
            "KeyPad = Function",
            "VoiceCommand = Function",
            "Option: Pressure applied to any key activates Keyboard",
            "Option: Touch anywhere on screen to activate TouchScreen",
            "Voice Command Auto_On when command given at or over 75db"
        ]
    def activate_touchscreen(self, touch_event=None):
        pass
    def activate_keypad(self, pressure=None):
        pass
    def activate_voice_command(self, volume_db=None):
        pass
    def execute_operator_interface_cycle(self, touch_event=None, pressure=None, volume_db=None):
        ts = self.activate_touchscreen(touch_event)
        kp = self.activate_keypad(pressure)
        vc = self.activate_voice_command(volume_db)
        return ts, kp, vc
    def activate_touchscreen(self, touch_event=None):
        pass
    def activate_keypad(self, pressure=None):
        pass
    def activate_voice_command(self, volume_db=None):
        pass
    def execute_operator_interface_cycle(self, touch_event=None, pressure=None, volume_db=None):
        ts = self.activate_touchscreen(touch_event)
        kp = self.activate_keypad(pressure)
        vc = self.activate_voice_command(volume_db)
        return ts, kp, vc
